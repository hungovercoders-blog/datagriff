---
title: "Deploying Containerised React App with Runtime Environment Variables"
date: 2024-04-27
author: dataGriff
description: Deploying Containerised React App with Runtime Environment Variables
image:
  path: /assets/2024-04-27-container-react-runtime-variables/link.png
tags: React Docker Azure Containers Terraform
---

React is a fickle beast when it comes to runtime environment variables and after visiting some of the distilleries on [whiskey.hungovercoders.com](https://whiskey.hungovercoders.com){:target="_blank"} it becomes an even trickier prospect to handle... My goal was to ensure that I could reference the appropriate API url for each react application at runtime with the appropriate argument in each environment as I deployed them with terraform in Azure container apps. After reading this extremely helpful [post](https://www.freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70/){:target="_blank"} from the awesome [freecodecamp.org](https://www.freecodecamp.org/){:target="_blank"}, that did all the work for me, and then adding a little of my own brand of hungovercoding, the outcome was a success! My source code for all of this can be found in [hungovercoders/whiskey.inventory](https://github.com/hungovercoders/whiskey.inventory){:target="_blank"}.

- [Pre-Requisites](#pre-requisites)
- [React Runtime Environment Variables](#react-runtime-environment-variables)
- [Containerise React App with Runtime Environment Variables](#containerise-react-app-with-runtime-environment-variables)
- [Deploying Dynamic API URL Runtime Variable with Terraform](#deploying-dynamic-api-url-runtime-variable-with-terraform)
  - [Managing CORS](#managing-cors)
  - [Demonstrating Working in Each Deployment](#demonstrating-working-in-each-deployment)

## Pre-Requisites

- I am again using [gitpod](https://gitpod.io){:target="_blank"} as my development environment with all of the requirements found in the [gitpod yaml file](https://github.com/hungovercoders/whiskey.inventory/blob/main/.gitpod.yml){:target="_blank"} and the [supporting docker container](https://github.com/hungovercoders/whiskey.inventory/blob/main/.cde.Dockerfile){:target="_blank"} of the whiskey inventory solution.
- I'd recommend reading my [previous blog post](https://blog.hungovercoders.com/datagriff/2024/03/31/shift-left-with-scripts.html){:target="_blank"} on setting up a basic container app deployment.
- You'll need to have an API and a react app to test this with or you can utilise what I have setup at [hungovercoders/whiskey.inventory](https://github.com/hungovercoders/whiskey.inventory){:target="_blank"} which came from [create-react-app.dev](https://create-react-app.dev/){:target="_blank"}.

## React Runtime Environment Variables

**The source of this section can be found on freecodecamp [here](https://www.freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70/){:target="_blank"}. I am stealing and summarising below.** Hopefully the latter sections leveraging this solution in deployment absolves me of the stolen material. The best developers steal right? 

Local to your react application you're going to need a .env file to store the runtime variable that you're interested in passing in as a parameter. In this instance we want to pass in the API_URL at runtime so it uses the appropriate API implementation per environment. The below shows the default local host which will be overridden with the environment specific API by the methods we put in place.

```env
API_URL=http://localhost:5240/api
```

In our distillery react application we'll then call the distillery API via the runtime environment variable. For example see the window._env_.API_URL in the script below:

```javascript
  useEffect(() => {
    const fetchData = async () => {
      try {
        const apiUrl = window._env_.API_URL || 'http://localhost:5240/api';
        console.log(apiUrl); // temporary to show environment specific solution!
        const response = await axios.get(`${apiUrl}/distilleries?page=${page}&pageSize=${pageSize}&country=${countryFilter}`);
        setDistilleries(response.data);
        setHasMore(response.data.length === pageSize); // Check if there are more pages
        setLoading(false); // Set loading to false after data is fetched
      } catch (error) {
        console.error('Error fetching data:', error);
        setError('It seems our servers have drunk a little too much and they can\'t seem to find your whiskey!');
        setLoading(false); // Set loading to false in case of error
      }
    };
```

Note that the console.log line is going to be temporary just to demonstrate the capability for this blog. You'll likely want to remove afterwards for "security by obfuscation" purposes.

Now add the following bash script as env.sh at the root of your react application along side the .env file:

```bash
#!/bin/bash

# Recreate config file
rm -rf ./env-config.js
touch ./env-config.js

# Add assignment 
echo "window._env_ = {" >> ./env-config.js

# Read each line in .env file
# Each line represents key=value pairs
while read -r line || [[ -n "$line" ]];
do
  # Split env variables by character `=`
  if printf '%s\n' "$line" | grep -q -e '='; then
    varname=$(printf '%s\n' "$line" | sed -e 's/=.*//')
    varvalue=$(printf '%s\n' "$line" | sed -e 's/^[^=]*=//')
  fi

  # Read value of current variable if exists as Environment variable
  value=$(printf '%s\n' "${!varname}")
  # Otherwise use value from .env file
  [[ -z $value ]] && value=${varvalue}
  
  # Append configuration property to JS file
  echo "  $varname: \"$value\"," >> ./env-config.js
done < .env

echo "}" >> ./env-config.js
```

This creates a runtime specific env-config.js file that reads the .env file you have in place and creates the key value pairs of the environment variables. If one is being passed in at runtime it will use this, otherwise it will use the value being passed in at runtime.

In order for your react application to use this file that gets generated from the bash script, you need to add this at the top of your index.html file.

```html
<script src="%PUBLIC_URL%/env-config.js"></script>
```

In order to not store these temporary generated environment variables in our source control, we'll want to add the following to our gitignore:

```text
/public/env-config.js
env-config.js
```

## Containerise React App with Runtime Environment Variables

Next we create a dockerfile to run our react application:

```dockerfile
# => Build container
FROM node:alpine as builder
WORKDIR /app
COPY package.json .
COPY yarn.lock* ./
RUN yarn install --frozen-lockfile
COPY . .
RUN yarn build

# => Run container
FROM nginx:1.15.2-alpine

# Nginx config
RUN rm -rf /etc/nginx/conf.d
COPY conf /etc/nginx

# Static build
COPY --from=builder /app/build /usr/share/nginx/html/

# Default port exposure
EXPOSE 80

# Copy .env file and shell script to container
WORKDIR /usr/share/nginx/html
COPY ./env.sh .
COPY .env .

# Add bash
RUN apk add --no-cache bash

# Make our shell script executable
RUN chmod +x env.sh

# Start Nginx server
CMD ["/bin/bash", "-c", "/usr/share/nginx/html/env.sh && nginx -g \"daemon off;\""]
```

You can see at the bottom of the dockerfile we have our env.sh script that gets run. This will occur when the react container is run and therefore override any environment variables we pass in that match the .env file, and are then used via the %PUBLIC_URL%/env-config.js reference we pass in via the index.html file.

Therefore if we now build and run this docker container with an valid API URL as a runtime variable:

```bash
docker build . -t hungovercoders/distillery:test
docker run -p 8080:80 -e API_URL=http://localhost:5240/api -t hungovercoders/distillery:test
```

We will see the correct local api being used logged to our console:

![Local Correct API Console]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/console_api_url.png)

and the local website works:

![Local Correct API Web]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/web_working_local.png)

If we now build and run this docker container with an invalid API URL as a runtime variable:

```bash
docker build . -t hungovercoders/distillery:test
docker run -p 8080:80 -e API_URL=http://badurl:666/api -t hungovercoders/distillery:test
```

We will see the incorrect local api being used logged to our console:

![Local InCorrect API Console]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/console_api_url_bad.png)

and the local website doesn't work:

![Local InCorrect API Web]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/web_not_working_local.png)

We can also add the environment variable to a docker-compose file in conjunction with our API so that the whole solution works in tandem when developing locally e.g.

```yaml
version: '3.4'

services:

  api:
    # image: ${APP}
    build:
      context: ./api
      dockerfile: Dockerfile
    ports:
      - 5240:5240
    environment:
    - CORS_ORIGINS=http://localhost:8080
  web:
    # image: $APP
    build:
      context: ./web
      dockerfile: Dockerfile
    ports:
      - 8080:80
    environment:
    - API_URL=http://localhost:5240/api

```

If we then run:

```bash
docker-compose up
```

We again get our API and Web application working in conjunction with the environment variables passed in at runtime. What a glorious time to be alive!

![Docker Compose]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/docker_compose.png)

## Deploying Dynamic API URL Runtime Variable with Terraform

Next we want to ensure we can inject the correct API URL per environment as we deploy our web application. This is now straight forward as we just want to pass in an environment variable that references the API container app deployed as part of the same solution. Below is the complete example of the API container app and the Web container app referencing the URL of this resource to utilise as a runtime environment variable.

```hcl
resource "azurerm_container_app" "api" {
  name                         = local.container_app_api_name
  container_app_environment_id = data.azurerm_container_app_environment.app_environment.id
  resource_group_name          = azurerm_resource_group.rg.name
  tags                         = local.tags
  revision_mode                = "Single"
  template {
    container {
      name   = local.container_api_name
      image  = local.container_api_image_name
      cpu    = 0.25
      memory = "0.5Gi"
      env {
        name  = "APP_ENVIRONMENT"
        value = var.environment
      }
      env {
        name  = "CORS_ORIGINS"
        value = "https://${local.custom_domain}"
      }
    }
  }
  ingress {
    external_enabled = true
    target_port      = var.port_api
    traffic_weight {
      latest_revision = true
      percentage      = 100
    }
  }
}

resource "azurerm_container_app" "web" {
  name                         = local.container_app_web_name
  container_app_environment_id = data.azurerm_container_app_environment.app_environment.id
  resource_group_name          = azurerm_resource_group.rg.name
  tags                         = local.tags
  revision_mode                = "Single"
  template {
    container {
      name   = local.container_web_name
      image  = local.container_web_image_name
      cpu    = 0.25
      memory = "0.5Gi"
      env {
        name  = "API_URL"
        value = "https://${azurerm_container_app.api.ingress[0].fqdn}/api"
      }
    }
  }
  ingress {
    external_enabled = true
    target_port      = var.port_web
    traffic_weight {
      latest_revision = true
      percentage      = 100
    }
  }
  lifecycle {
    ignore_changes = [
      ingress[0].custom_domain // Ignore changes to the custom domain until terraform can manage it - https://github.com/hashicorp/terraform-provider-azurerm/issues/21866
    ]
  }
}
```

### Managing CORS

Its worth noting that to manage the API CORS requirements of the API I am also passing in a custom domain of the Web API per environment. This means that each API in each environment is also more secure as it will only expect web calls from the correct web address as well.

As a result of me using the custom web domains, [devwhiskey.hungovercoders.com](https://devwhiskey.hungovercoders.com/){:target="_blank"} and [whiskey.hungovercoders.com](https://whiskey.hungovercoders.com/){:target="_blank"}, I have had to tell the terraform lifecyle to ignore these changes in the custom domain at the end of the terraform as I could only manage this manually.

### Demonstrating Working in Each Deployment

Once this is deployed to the development environment you can see that the application works and the development web application references the development API URL in the console logs:

![Dev Environment]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/dev_environment.png)

Once this is deployed to the production environment you can see that the application works and the production web application references the development API URL in the console logs:

![Prod Environment]({{ site.baseurl }}/assets/2024-04-27-container-react-runtime-variables/prd_environment.png)

At the end of this demonstration I removed the API being logged to the URL just to clean up my code.

If you have managed to follow along checkout the [whiskey.hungovercoders.com](https://whiskey.hungovercoders.com/){:target="_blank"} for some celebratory tipple! It might be a little slow as I allow it to scale to zero when not in use. I think the solution is great for me to demonstrate this solution, but I will likely look to present a static website to users simply searching for whiskey distilleries and keep the react interactive application for a future CRUD solution only for true hungovercoders...
