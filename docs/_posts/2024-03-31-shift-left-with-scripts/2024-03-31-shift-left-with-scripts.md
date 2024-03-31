---
title: "Shift Left with Scripts"
date: 2024-03-31
author: dataGriff
description: Shift your deployment left by using scripts that you can reuse for deployment pipelines and cloud developer environments
image:
  path: /assets/2024-03-31-shift-left-with-scripts/link.png
tags: Terraform Docker Azure Containers Gitpod
---

Being an impatient coder due to the constant headaches the night before often brings upon me, I need to make sure I find out as early as possible whether my deployment pipeline is working. For years I have committed my code and waited for some proprietary tooling embedded within Azure devops or github actions to tell me the answer... I have changed my ways and have now brought the scripts for deployment into my codebase that I can simulate easily locally in my cloud developer environment AND then use the exact same scripts for my deployment pipeline! Read on fellow hungovercoder and find out how to shift left with scripts...

- [Quick OKR and Agile Recap](#quick-okr-and-agile-recap)
- [Why Integrate OKRs with Agile](#why-integrate-okrs-with-agile)
- [Making OKRs Everything](#making-okrs-everything)
  - [Objective Zero](#objective-zero)
- [Team OKRs Should not Link to Individual Remuneration](#team-okrs-should-not-link-to-individual-remuneration)
- [The Football Analogy](#the-football-analogy)
- [OKR and Agile Cycle](#okr-and-agile-cycle)
- [OKR Ceremonies](#okr-ceremonies)
  - [OKR Scene Setting](#okr-scene-setting)
    - [Categories of Concern](#categories-of-concern)
  - [OKR Creation](#okr-creation)
  - [OKR Impact Planning](#okr-impact-planning)
  - [OKR Retrospective](#okr-retrospective)
- [Iteration Ceremonies](#iteration-ceremonies)
  - [Daily Stand-ups](#daily-stand-ups)
  - [Zero Tolerance](#zero-tolerance)
  - [Backlog Refinement](#backlog-refinement)
  - [Iteration Planning](#iteration-planning)
  - [Iteration Review](#iteration-review)
  - [Iteration Retrospective](#iteration-retrospective)
- [Stay Agile](#stay-agile)

## Shifting Left with Scripts

## Goal: Deploying a Container App in Azure

## Prerequisites

You're going to need the following platforms in order to follow along with the demonstrations in this blog:

- [Azure Account](https://portal.azure.com)
- [Docker Hub Account](https://hub.docker.com)
- [Github Account](https://github.com/)
- [VS Code](https://code.visualstudio.com/download)

For development on your local machine your going to need the following tools installed:

- [DotNet](https://dotnet.microsoft.com/en-us/download/dotnet-framework)
- [Git](https://git-scm.com/downloads)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Terraform](https://developer.hashicorp.com/terraform/install)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [Curl](https://help.ubidots.com/en/articles/2165289-learn-how-to-install-run-curl-on-windows-macosx-linux)

These VS code extensions are also useful for the development methods used.

- [Terraform Extension](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)
- [Azure Tools Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-node-azure-pack)
- [C# Dev Kit Extension](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csdevkit)
- [Github Actions Extension](https://marketplace.visualstudio.com/items?itemName=GitHub.vscode-github-actions)
- [Docker Extension](https://code.visualstudio.com/docs/containers/overview)

OR... you can just sign up and use [Gitpod](https://gitpod.io) and utilise the [configuration below](#configure-cloud-developer-startup) I used to create this which installs all of the above for you!!!

- [Gitpod](https://gitpod.io)

**Spoiler alert** the demos below are going to be using [Gitpod](https://gitpod.io) as a cloud developer environment because its **so much easier**...

## Love Environment Variables

I am a big fan of environment variables. I think their power is criminally overlooked by developers. Whenever I am setting up my development capabilities I want my local development environment to have identical capabilities and outcomes to my actual environment development and production environments. The only thing I want to potentially change are my environment variables. In the following demonstrations the following environment variables will be configured in my gitpod and github actions environments, with my local domain.env file dictating static environment variables held in the codebase and reused throughout.

### Dynamic Environment Variables

| Variable Name | Purpose |
|--|--|
| ARM_CLIENT_ID | Used along with client secret and Tenant ID to authenticate with an application registration against Azure. |
| ARM_CLIENT_SECRET | Used along with client ID and Tenant ID to authenticate with an application registration against Azure. |
| ARM_TENANT_ID | Used along with client ID and client secret to authenticate with an application registration against Azure. |
| ARM_SUBSCRIPTION_ID | Used to provide subscription that the resource deployment will take place in.  |
| ARM_REGION | Dictates the region the resources will be deployed into e.g. north europe |
| DOCKER_USERNAME | Docker username to login and push or pull images. |
| DOCKER_PASSWORD | Docker password to login and push or pull images.  |
| ENVIRONMENT | Whether the action is taking place in development, uat or production environment. |
| ORGANISATION | The name of the orgaisation deploying e.g. hungovercoders. |
| UNIQUE_NAMESPACE | A unique namespace to postfix Azure assets with e.g. hngc. |

### Static Environment Variables

| Variable Name | Purpose |
|--|--|
| TEAM | The name of the team that owns the asset used in tagging resources for example. |
| DOMAIN | The business domain that incorporates the asset used in tagging resources for example. |
| APP | The name of the application. |
| PORT | The port number tha application will expose itself on through docker. Makes it easy to reuse where needed.  |

The following is held in a domain.env file like the following:

```env
TEAM=hungovercoders
DOMAIN=dotnet
APP=dotnet-api
PORT=5050
```

I have started a number of [cheatsheets](https://blog.hungovercoders.com/cheatsheets/) for hungovercoders and one of them is for my [configurations](https://blog.hungovercoders.com/cheatsheets/configuration/configuration.html) which is useful reference for myself and may give you some ideas too.

## Smoke Test Driven Development

Lets get this straight I am no tester. This is something I definitely need in my arsenal and I hope to reach some modicum of knowledge soon... However I do know how to request an endpoint using curl and so I thought to myself... Lets do that. I will start development with a simple goal of requiring a successful 200 response from a health endpoint and in later sessions I will improve my tests - but at least I have something telling me if my API endpoint is there. I created a "tests" directory at the root of my git repository and added two files.

```
test/smoke_test.sh
test/test.sh
```

The first test file which calls the URL I pass it as a parameter is a simple smoke test that confirms I get a 200 from the URL designated. I defaulted this URL to a localhost value with the port number I have in my domain environment variable file that I eventually expect to be the one opened for my application along with the endpoint "health". I added some retries into the behaviour as I noticed later my application can sometimes take a second or so to startup when I run this as part of a container build and run process.

```bash
echo "Starting script: $0..."

set -a
. ./domain.env
set +a

URL=${1:-http://localhost:$PORT/health}
echo "Url to be smoke tested is $URL..."

retries=5
wait=1
timeout=$(($wait*5))

echo "Test configured with time between retries of $wait second with a maximum of $retries retries resulting in a timeout of $timeout seconds."

counter=1
while [ $counter -le $retries ]; do
    echo "Attempt $counter..."
    echo "Requesting response..."
    response=$(curl -s -o /dev/null -w "%{http_code}" $URL)
    if [ "$response" -eq 200 ]; then
        echo "\e[32mSuccess: HTTP status code is 200\e[0m"
        exit 0
    elif [ "$response" -eq 000 ]; then
        echo "\e[33mPending: HTTP status code is 000\e[0m"
    else
        echo -e "\e[31mError: HTTP status code is $response\e[0m"
        exit 1
    fi

    sleep $wait
    echo "Waiting $wait second to ensure container is up before trying again..."
    counter=$(expr $counter + 1)
    done
echo "\e[31mTimed out after $retries retries over a period of $timeout seconds.\e[0m"
exit 1
```

I introduced a couple of components I wanted of my script files here which is to have good print messages, appropriate colouring for success and failure, and wrap my scripts with:

```bash
echo "Starting script: $0..."
...
echo "Completed script: $0."
```

This simply prints out the script file that has started and completed which makes it really easy to debug. 

I then added the parent test.sh script file simply to have one thing to reference from my local development environment and my eventual pipelines. This means even if I mess around with test files my integration layer to my test scripts will be consistent. The file simply looks like the following with scope for more tests when needed.

```bash
set -e  # Exit immediately if a command exits with a non-zero status.

echo "Starting script: $0..."

sh ./test/smoke_test.sh

echo "Completed script: $0."

```

If I run this now I get the expected failure as I have not built nor run an API to satisfy this smoke test yet. Hence smoke test driven development... Hey we got to start somewhere!

![Test Fail]({{ site.baseurl }}/assets/2024-03-31-shift-left-with-scripts/test_fail.png)

## Local Application Development

### Quick Start

I quickly need an API to pass my test! As I am using dotnet I can quickly use the following command to get myself a dotnet API working, imaginitively called "api".

```bash
dotnet new webapi --name api
```

This generates all the simple API code I need which is the weather forecast example Microsoft provides. If you navigate to the Program.cs file you will see something like the following:

```csharp
...
var summaries = new[]
{
    "Freezing", "Bracing", "Chilly", "Cool", "Mild", "Warm", "Balmy", "Hot", "Sweltering", "Scorching"
};

app.MapGet("/weatherforecast", () =>
{
    var forecast =  Enumerable.Range(1, 5).Select(index =>
        new WeatherForecast
        (
            DateOnly.FromDateTime(DateTime.Now.AddDays(index)),
            Random.Shared.Next(-20, 55),
            summaries[Random.Shared.Next(summaries.Length)]
        ))
        .ToArray();
    return forecast;
})
.WithName("GetWeatherForecast")
.WithOpenApi();

app.Run();
...
```

You can build this applicaton to make sure its all working:

```bash
cd api
dotnet build
dotnet run
```

You should be given a URL...

and then see the weather forecast when you got the link and append "/weatherforecast" to the URL.

Right that's the basics done, but we want this running in a docker container so we can work with it locally in an environment that exactly reflects that in the destined Azure container app!

### Containerize the API

We can add the following basic Docker file to our application directory.

```dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app
EXPOSE 5050

LABEL       author="datagriff"

ENV ASPNETCORE_URLS=http://+:5050

USER app
FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG configuration=Release
WORKDIR /src
COPY ["api/api.csproj", "api/"]
RUN dotnet restore "api/api.csproj"
COPY . .
WORKDIR "/src/api"
RUN dotnet build "api.csproj" -c $configuration -o /app/build

FROM build AS publish
ARG configuration=Release
RUN dotnet publish "api.csproj" -c $configuration -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "api.dll"]
```

The port number must match up with your environment file in order for everything to work accordingly. Its really important to note that **your Dockerfile is your applications CI build!** You can see contained within this very simple Dockerfile the **RUN dotnet build** task. Therefore we do not need to add any other complexity to our CI process as the Dockerfile encapsulates all this logic. This is step 1 in consistency between your local development and the eventual deployment pipeline, the Dockerfile consistency ensures the pipeline is the same for the application.

Next you can do a simple docker build, run, test and push to your container registry as you wish... I have written the **docker_build.sh** script below which allows me to do all this very easily from my local machine, utilising environment variables where necessary.

```bash
set -e  # Exit immediately if a command exits with a non-zero status.

RUN=${1:-False}
PUSH=${2:-False}

echo "Starting script: $0..."

set -a
. ./domain.env
set +a

if [ $RUN = True ]; then
    echo "You have chosen to run the image as a container once built."
fi
if [ $RUN = False ]; then
    echo "You have chosen not to run the image as a container once built."
fi

if [ $PUSH = True ]; then
    echo "You have chosen to push the image once built, run and tested."
fi
if [ $PUSH = False ]; then
    echo "You have chosen not to push the image once built, run and tested."
fi

echo "Organisation is $ORGANISATION."
echo "App name is $APP."
CONTAINERNAME=$APP
echo "Container name is $CONTAINERNAME."
BRANCH=$(git rev-parse --abbrev-ref HEAD)
VERSION=$BRANCH-$(git log -1 --format="%h-%B" | sed 's/ /-/g')
echo "Version is $VERSION."
IMAGENAME=$ORGANISATION/$APP:$VERSION
echo "Image name is $IMAGENAME."

echo "Changing to application directory to interact with docker file..."
cd api
echo "Changed to application directory to interact with docker file."
echo "Building $IMAGENAME..."
docker build -t $IMAGENAME .
echo "Built $IMAGENAME."
echo "Changing to back to root directory..."
cd ..
echo "Changed to back to root directory."


if [ "$(docker inspect -f '{{.State.Running}}' "$CONTAINERNAME" 2>/dev/null)" = "true" ]; then
    echo "Stopping container: $CONTAINERNAME"
    docker stop $CONTAINERNAME
    echo "Container stopped successfully."
else
    echo "Container $CONTAINERNAME is not currently running."
fi

if [ "$RUN" = "True" ] || [ "$PUSH" = "True" ]; then
    sh ./tools_app/docker_containers_clear.sh
    echo "Run container $CONTAINERNAME from image $IMAGENAME..."
    docker run -d -p $PORT:$PORT --name $CONTAINERNAME $IMAGENAME
    echo "Running container $CONTAINERNAME from image $IMAGENAME."
    sh ./test/tests.sh
fi

sh ./tools_app/docker_list.sh

if [ $PUSH = True ]; then
    echo "Logging in to Docker..."
    docker login --username $DOCKER_USERNAME --password $DOCKER_PASSWORD ##--password-stdin - how to use?
    echo "Logged in to Docker."
    echo "Pushing image $IMAGENAME..."
    docker push $IMAGENAME
    echo "Pushed image $IMAGENAME."
fi

echo "Completed script: $0."
```

- The script takes in two booleans of whether you want to RUN or PUSH as well as the container build.
- The script will only push if the container has run locally successfully including the tests on the running container.
- The script uses some basic semantic versioning for my image tags by using the branch name, commit id and message. I need to refine this further but ultimately this stopped me from accidentally pushing to latest whilst my production API was still referencing it! Its a bit noisey with regards to number of images and tags, but it will do me for now.
- The script leverages all of our lovely environment variables.
- The script also leverages 2 other scripts that I find useful for local development to speed things along...

docker_containers_clear.sh

```bash
echo "Starting script: $0..."
echo "Removing all stopped containers..."
docker container prune --force
echo "All stopped containers removed."
echo "Completed script: $0."
```

docker_list.sh

```bash
echo "Starting script: $0..."
echo "Listing all images..."
docker images
echo "Listed all images."
echo ""
echo "Listing all containers..."
docker ps --all
echo "Listed all containers."
echo "Completed script: $0."
```

Right if we run the docker build script to run and push our docker image:

```bash
 sh ./tools_app/docker_build.sh True True
```

We still get the failing test, which luckily also stops us pushing a bad image up to Docker Hub that will be of no use to anyone...


Of course we need to add the health endpoint to the API. If we add the following line of code to our Program.cs file we will now get the health endpoint, so if we run:

```bash
 sh ./tools_app/docker_build.sh True True
```

We get a passing test:

And we can see our latest image in line with our current commit 

## Local Infrastructure Development

## Configure Cloud Developer Startup

## Reuse for Deployment

## To be Continued...

There are a number of add-ons I want to include in this method of development such as far better testing, security and complexity measures. Ultimately though my development experience is now a dream come true and there are a number of champagne bottles littering my hungovercoder office in celebration.

