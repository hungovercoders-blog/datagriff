---
title: "Developing locally with cosmos emulator in a container"
date: 2024-06-29
author: dataGriff
description: Developing locally with cosmos emulator in a container
image:
  path: /assets/2024-06-29-cosmos-emulator-docker/link.png
tags: Docker Azure Cosmos
---

A problem came up recently whereby we needed to run the cosmos emulator in a docker container for local development and subsequently in the CI stage of our deployment pipeline to reduce the need for a permanent environment. This was a right head scratcher and started to make me feel worse than a classic hungovercoder hangover. There was only way to cure myself of this... Solve the problem with my favourite of all hangover cures - doggos! Lets jump in and demonstrate how we can create a local developer experience with a dotnet app and the cosmo emulator running docker.

- [Pre-Requisites](#pre-requisites)
- [Compose your Cosmos Emulator](#compose-your-cosmos-emulator)
- [Create your Console App](#create-your-console-app)
- [Dockerise your Console App](#dockerise-your-console-app)
  - [Magic Entry Script!](#magic-entry-script)
  - [Docker File](#docker-file)
- [Compose your Console App](#compose-your-console-app)
- [Run your Application](#run-your-application)

## Pre-Requisites

In order to carry out this walkthrough you'll need the following:

- [Github Account](https://github.com/){:target="_blank"}
- [VS Code](https://code.visualstudio.com/download){:target="_blank"}

For development on your local machine your going to need the following tools installed:

- [DotNet](https://dotnet.microsoft.com/en-us/download/dotnet-framework){:target="_blank"}
- [Git](https://git-scm.com/downloads){:target="_blank"}
- [Docker Desktop](https://www.docker.com/products/docker-desktop/){:target="_blank"}
- [Curl](https://help.ubidots.com/en/articles/2165289-learn-how-to-install-run-curl-on-windows-macosx-linux){:target="_blank"}

However, I am again using the mighty [gitpod](https://gitpod.io/) to cater for these needs and my docker file looks like this (I'm using this as a base for other Azure dotnet work which is why there are other things in there - handy though right??).

```Dockerfile
FROM gitpod/workspace-dotnet

USER gitpod

# Install Homebrew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc

# Update Homebrew, Install Terraform & Azure CLI
RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && \
    brew update && \
    brew tap hashicorp/tap && \
    brew install hashicorp/tap/terraform && \
    brew upgrade terraform && \
    brew install azure-cli  && \
    brew install aztfexport && \
    brew install maven

# Install Azure Functions Core Tools
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg && \
    sudo mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg && \
    sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/microsoft-ubuntu-$(lsb_release -cs)-prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list' && \
    sudo apt-get update && \
    sudo apt-get install azure-functions-core-tools-4
```

And my gitpod yaml looks like this

```yaml
image:
  file: .cde.Dockerfile

vscode:
  extensions:
    - hashicorp.terraform
    - ms-azuretools.vscode-azureresourcegroups
    - formulahendry.code-runner
    - gitpod.gitpod-desktop
    - ms-dotnettools.csdevkit
    - patcx.vscode-nuget-gallery
    - ms-vscode.azurecli
```

Now that was so easy. Did I mention I love [gitpod](https://gitpod.io/)?

## Compose your Cosmos Emulator 

The first thing we want to do is get the cosmos emulator running in a docker container. Full disclosure this blog post was made significantly easier by the discover of these [emulator recipes](https://github.com/Azure/cosmosdb-emulator-recipes/tree/main) provided by Microsoft... Therefore in order to pull and run the cosmos emulator in a container we're going to use the following docker compose file (the app will come later).

```yaml
networks:
  default:
    external: false
    ipam:
      driver: default
      config:
        - subnet: "172.16.238.0/24"

services:
  cosmosdb:
    restart: always
    container_name: "azure-cosmos-emulator-latest"
    hostname: "azurecosmosemulator"
    image: 'mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest'
    mem_limit: 4GB
    tty: true
    ports:
    - '8081:8081' # Data Explorer
    - '8900:8900'
    - '8901:8901'
    - '8902:8902'
    - '10250:10250'
    - '10251:10251'
    - '10252:10252'
    - '10253:10253'
    - '10254:10254'
    - '10255:10255'
    - '10256:10256'
    - '10350:10350'
    expose:
    - "8081"
    environment:
      - AZURE_COSMOS_EMULATOR_PARTITION_COUNT=11
      - AZURE_COSMOS_EMULATOR_ENABLE_DATA_PERSISTENCE=true
      - AZURE_COSMOS_EMULATOR_IP_ADDRESS_OVERRIDE=172.16.238.246
    volumes:
      - cosmosdb-dog_adopter_console-data:/var/lib/cosmosdb
    networks:
      default:
        ipv4_address: 172.16.238.246

volumes:
  cosmosdb-dog_adopter_console-data:
```

The compose file is pretty self explanatory. We are pulling the latest cosmos emulator image from the Microsoft container registry and exposing the ports that the cosmos explorer uses. We are also setting the environment variables for the emulator and creating a volume for the data persistence. A network is also created ready for the app to connect to the emulator. Its also worth noting the hostname as this what we will be using in the URL of the application when running in the docker environment instead of localhost. This tripped me for ages so that will teach me to read the documentation properly!

Run this following bash command with detach to start the cosmos emulator in a container. 

```bash
docker compose up --detach 
```

Its important to use the detach for the cosmos emulator as it take ages to start and so you want to make sure you don't accidentally cancel if you ran it interactively, which would bring down the container. Pretty much when you get the cosmos emulator running you want to leave it running to save time! Later on we will see how we rebuild solely on the app when performing docker compose so we leave the slow starting cosmos emulator running.

You can then run this command to see the logs of the cosmos emulator. This can be safely cancelled without bringing down the emulator. Phew.

```bash
docker compose logs --follow
```

Once the emulator is up and running you can then navigate to the cosmos explorer at [https://localhost:8081/_explorer/index.html](https://localhost:8081/_explorer/index.html) as we exposed port 8081 in the docker compose file.

Don't panic when you see the unsafe message...

![Cosmos Proceed Unsafe]({{ site.baseurl }}/assets/2024-06-29-cosmos-emulator-docker-local/cosmos-proceed-unsafe.png)

Just proceed and you will see the cosmos explorer.

![Cosmos Explorer]({{ site.baseurl }}/assets/2024-06-29-cosmos-emulator-docker-local/cosmos-explorer.png)

## Create your Console App

Lets create our dog adopter dotnet console app with the following command

```bash
dotnet new console --name dog_adopter
```

Next create a Models directory and add a class called RescueDog.cs with the following code

```csharp
using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace dog_adopter.Models
{
    public class RescueDog
    {
        public RescueDog(string name, Breed breed, Status status, Guid id, DateTime timestamp)
        {
            Name = name;
            Breed = breed;
            Status = status;
            Id = id;
            Timestamp = timestamp;
        }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("id")]
        public Guid Id { get; set;}

        [JsonProperty("breed")]
        public Breed Breed { get; set; }

        [JsonProperty("status")]
        public Status Status { get; set; }

        [JsonProperty("timestamp")]
        public DateTime Timestamp { get; set;}
    }
}

 [JsonConverter(typeof(StringEnumConverter))]
public enum Breed
{
    Beagle,
    Boxer,
    Bulldog,
    Chihuahua,
    Dalmatian,
    GermanShepherd,
    GoldenRetriever,
    GreatDane,
    LabradorRetriever,
    Poodle,
    Rottweiler,
    SiberianHusky,
    YorkshireTerrier
}

[JsonConverter(typeof(StringEnumConverter))]
public enum Status
{
    Adopted,
    Available,
    Fostered,
    Reserved
}
```

The class creates a simple model for a rescue dog with a name, breed, status, id and timestamp. It's important to note that I had to fallback to use the Newtonsoft.Json library as the System.Text.Json library does not support serializing enums to strings. This is a bit of a pain but I'm sure it will be resolved in the future - see this ongoing gihub issue [here](https://github.com/dotnet/runtime/issues/74385).

Next create a Data directory and add an IDataAdapter.cs file with the following contents:

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using dog_adopter.Models;

namespace dog_adopter.Data
{
    public interface IDatabaseAdapter
    {
        Task<bool> CreateRescueDog(RescueDog rescueDog);

        Task<bool> UpdateRescueDog(RescueDog rescueDog);

        Task<List<RescueDog>> GetRescueDogs();

        Task<RescueDog> GetRescueDog(Breed breed, Guid id);

    }
}
```

This interface uses the rescue dog model and defines the methods for creating, updating, getting all and getting a single rescue dog. When we create out code to interface with the Cosmos database we'll need to implement these methods to satisfy the interface.

Without further ado add a CosmosSQLDatabase.cs file to the same Data directory with the following contents:

```csharp
using Microsoft.Azure.Cosmos;
using dog_adopter.Models;
// using System.Text.Json;
// using System.Text.Json.Serialization;

namespace dog_adopter.Data
{
    public class CosmosSQLDatabase : IDatabaseAdapter
    {
        public CosmosClient _cosmosClient;
        private Database _database;
        private Container _container;

        string cosmos_conn = Environment.GetEnvironmentVariable("COSMOS_CONN");

        string environment = Environment.GetEnvironmentVariable("ASPNETCORE_ENVIRONMENT");

        public CosmosSQLDatabase()
        {


            // Initialize CosmosClient
            _cosmosClient =  new CosmosClient(cosmos_conn, new CosmosClientOptions
            {
                SerializerOptions = new CosmosSerializationOptions
                {
                    PropertyNamingPolicy = CosmosPropertyNamingPolicy.CamelCase
                },
                HttpClientFactory = () =>
                {
                    if(environment != "Development")
                    {
                        return new HttpClient(new HttpClientHandler());
                    }
                    /*                               *** WARNING ***
                        This code is for development purposes only. It should not be used in production.
                    */
                    HttpMessageHandler httpMessageHandler = new HttpClientHandler
                    {
                        ServerCertificateCustomValidationCallback = HttpClientHandler.DangerousAcceptAnyServerCertificateValidator
                    };
                    return new HttpClient(httpMessageHandler);
                },
                ConnectionMode = ConnectionMode.Direct
               });

        }

        public async Task InitializeAsync()
        {
            _database = await _cosmosClient.CreateDatabaseIfNotExistsAsync("dog_adopter");
            _container = await _database.CreateContainerIfNotExistsAsync("rescue_dogs", "/breed");
            Console.WriteLine("Cosmos DB and Container initialized successfully.");
        }

        public async Task<RescueDog> GetRescueDog(Breed breed, Guid id)
        {
            try
            {
                ItemResponse<RescueDog> response = await _container.ReadItemAsync<RescueDog>(id.ToString(), new PartitionKey(breed.ToString()));
                return response.Resource;
            }
            catch (CosmosException ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
            {
                return null;
            }
        }

        public async Task<List<RescueDog>> GetRescueDogs()
        {
            var query = new QueryDefinition("SELECT * FROM c");
            FeedIterator<RescueDog> resultSet = _container.GetItemQueryIterator<RescueDog>(query);

            List<RescueDog> results = new List<RescueDog>();
            
            while (resultSet.HasMoreResults)
            {
                FeedResponse<RescueDog> response = await resultSet.ReadNextAsync();
                results.AddRange(response.ToList());
            }

            return results;
        }

        public async Task<bool> CreateRescueDog(RescueDog rescueDog)
        {
            try
            {
                ItemResponse<RescueDog> response = await _container.CreateItemAsync<RescueDog>(rescueDog);

                return true;
            }
            catch (Exception)
            {
                Console.WriteLine("Failed to create rescue dog.");
                throw;
                return false;
            }
        }

        public async Task<bool> UpdateRescueDog(RescueDog rescueDog)
        {
            try
            {
                ItemResponse<RescueDog> response = await _container.UpsertItemAsync<RescueDog>(rescueDog);

                return true;
            }
            catch (Exception)
            {
                return false;
            }
        }
    }
}
```

## Dockerise your Console App


### Magic Entry Script!

```bash
#!/bin/bash
#set -e 

echo "$ASPNETCORE_ENVIRONMENT environment..."

if [ "$ASPNETCORE_ENVIRONMENT" == "Development" ]; then

    cosmosHost=azurecosmosemulator
    cosmosPort=8081

    # Wait for CosmosDB to be available, a health check from the container that is connecting to CosmosDB
    echo "Waiting for local dev CosmosDB emulator at $cosmosHost:$cosmosPort..."
    until [ "$(curl -k -s --connect-timeout 5 -o /dev/null -w "%{http_code}" https://$cosmosHost:${cosmosPort}/_explorer/emulator.pem)" == "200" ]; do
        sleep 5;
        echo "Waiting for CosmosDB at $cosmosHost:$cosmosPort..."
    done;
    echo "CosmosDB is available."

    # Download the CosmosDB Cert and add it to the Trusted Certs
    echo "Downloading CosmosDB Cert..."
    curl -k https://$cosmosHost:${cosmosPort}/_explorer/emulator.pem > emulatorcert.crt

    echo "Adding CosmosDB Cert to Trusted Certs..."
    cp emulatorcert.crt /usr/local/share/ca-certificates/
    update-ca-certificates
fi

echo "Running Dog Adopter console app using .NET SDK.."
dotnet dog_adopter.dll
```

### Docker File

```Dockerfile
FROM mcr.microsoft.com/dotnet/aspnet:8.0 AS base
WORKDIR /app

LABEL author="datagriff"

USER app

#RUN chmod +x entrypoint.sh

FROM --platform=$BUILDPLATFORM mcr.microsoft.com/dotnet/sdk:8.0 AS build
ARG configuration=Release
WORKDIR /dog_adopter_console
COPY ["dog_adopter.csproj", "dog_adopter_console/"]
RUN dotnet restore "dog_adopter_console/dog_adopter.csproj"
COPY . .
WORKDIR "/dog_adopter_console"
RUN dotnet build "dog_adopter.csproj" -c $configuration -o /app/build

FROM build AS publish
ARG configuration=Release
RUN dotnet publish "dog_adopter.csproj" -c $configuration -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app

COPY --from=publish /app/publish .

ARG environment=Production
ENV ASPNETCORE_ENVIRONMENT=$environment

# Install curl to check for CosmosDB Emulator in Development
USER root
RUN if [ "$ASPNETCORE_ENVIRONMENT" = "Development" ]; then \
    apt-get update && apt-get install -y curl; \
    fi

COPY ["entrypoint.sh", "entrypoint.sh"]

USER root
ENTRYPOINT ["./entrypoint.sh" ]
```


## Compose your Console App

```yaml
networks:
  default:
    external: false
    ipam:
      driver: default
      config:
        - subnet: "172.16.238.0/24"

services:
  cosmosdb:
    restart: always
    container_name: "azure-cosmos-emulator-latest"
    hostname: "azurecosmosemulator"
    image: 'mcr.microsoft.com/cosmosdb/linux/azure-cosmos-emulator:latest'
    mem_limit: 4GB
    tty: true
    ports:
    - '8081:8081' # Data Explorer
    - '8900:8900'
    - '8901:8901'
    - '8902:8902'
    - '10250:10250'
    - '10251:10251'
    - '10252:10252'
    - '10253:10253'
    - '10254:10254'
    - '10255:10255'
    - '10256:10256'
    - '10350:10350'
    expose:
    - "8081"
    environment:
      - AZURE_COSMOS_EMULATOR_PARTITION_COUNT=11
      - AZURE_COSMOS_EMULATOR_ENABLE_DATA_PERSISTENCE=true
      - AZURE_COSMOS_EMULATOR_IP_ADDRESS_OVERRIDE=172.16.238.246
    volumes:
      - cosmosdb-dog_adopter_console-data:/var/lib/cosmosdb
    networks:
      default:
        ipv4_address: 172.16.238.246

  app:
    container_name: dog_adopter_console
    build:
      context: .
      dockerfile: .Dockerfile
      args:
      - environment=Development
    depends_on:
      - cosmosdb
    environment:
      - COSMOS_CONN=AccountEndpoint=https://azurecosmosemulator:8081/;AccountKey=C2y6yDjf5/R+ob0N8A7Cgv30VRDJIWEHLM+4QDU5DE2nQ9nDuVTqobD4b8mGGyPMbIZnqyMsEcaGQy67XIw/Jw==; 
    networks:
      default:
        ipv4_address: 172.16.238.242

volumes:
  cosmosdb-dog_adopter_console-data:
```

## Run your Application