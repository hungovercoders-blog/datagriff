---
title: ".Net API Container on Gitpod | .Net containers in cloud developer environments"
date: 2023-09-09
author: dataGriff
description: Dotnet containers in cloud developer environments
image:
  path: /assets/2023-09-09-dotnet-api-container-gitpod/link.png
tags: API .Net Container Gitpod
---

Recently I decided to learn docker and all things containers. I dived deep into the deepest darkest spaces of my windows laptops configuration... My laptop suddenly got very angry with me and decided that the C drive was too full, or that suddenly docker desktop and the dotnet framework would disappear from my machine! I desperately wanted to just code and run the [whiskey api](https://github.com/hungovercoders/whiskey.reviews) in a container without wasting time configuring my machine. Well, everyone, there is a way, and that way is using the cloud developer environment [gitpod](https://www.gitpod.io)...

- [Prerequisites](#prerequisites)
- [Gitpod](#gitpod)
- [Run Dotnet API Container](#run-dotnet-api-container)
- [Gitpod Configuration File](#gitpod-configuration-file)
- [Create Workspace](#create-workspace)
- [Configure Prebuild](#configure-prebuild)
- [What Next??](#what-next)

## Prerequisites

- [Github Account](https://www.github.com) - If you haven't already get yourself a github account, this is how you're going to host code and open up gitpod.
- [~~Docker Desktop~~](https://www.docker.com/products/docker-desktop/) - Not needed!
- [~~.Net Frameworks~~](https://dotnet.microsoft.com/en-us/download/dotnet-framework) - Not needed!
- [~~Git~~](https://git-scm.com/) - Not needed!
- [Visual Studio Code](https://code.visualstudio.com/) - Actually optional as you can do it all in the browser or in the desktop IDE.
- Decent Laptop - Not needed. You can use gitpod to run this on a tablet or even your [mobile phone](https://www.gitpod.io/guides/getting-started-with-gitpod-in-android)!

## Gitpod

Gitpod is a cloud developer environment

## Run Dotnet API Container

The first thing I wanted to do was run the whiskey api in a container. This was in a bit to make the API cloud native, allowing it to run and deploy consistently on any cloud. I added the file below to the repo and at first had the container running from my laptop, post a lot of docker and .net framework configuration setup.

```bash
FROM mcr.microsoft.com/dotnet/aspnet:7.0 AS base
WORKDIR /app
EXPOSE 3000

ENV ASPNETCORE_URLS=http://+:3000
# Allows for swagger
ENV ASPNETCORE_ENVIRONMENT=Development 

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-dotnet-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

FROM mcr.microsoft.com/dotnet/sdk:7.0 AS build
ARG configuration=Release
WORKDIR /src
COPY ["WhiskeyAPI/WhiskeyAPI.csproj", "WhiskeyAPI/"]
RUN dotnet restore "WhiskeyAPI/WhiskeyAPI.csproj"
COPY . .
WORKDIR "/src/WhiskeyAPI"
RUN dotnet build "WhiskeyAPI.csproj" -c $configuration -o /app/build

FROM build AS publish
ARG configuration=Release
RUN dotnet publish "WhiskeyAPI.csproj" -c $configuration -o /app/publish /p:UseAppHost=false

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "WhiskeyAPI.dll"]
```

The Dockerfile performs the following:

1. It brings in dotnet as a base image.
2. It sets environment variables for the port to expose and environment to development so that swagger will be exposed.
3. It creates a user to access the app folder.
4. It copies the relevant files of the API into a src folder and builds it.
5. It publishes the built project.
6. It creates a dotnet entry point for the image.

At this point if you have your own hardware environment configured you could run the following to build the image.

Then run the container with this command.

However after some falling out with my laptop, this is what led me to using gitpod as my development environment instead...

## Gitpod Configuration File

To run your codebase in a gitpod container you first need to add a [.gitpod.yml configuration file](). You can do this with the following [gitpod CLI]() command:

```bash
gp init
```

I then added the following to the .gitpod.yml file in my dotnet repo.

```yaml
image:
  file: .gitpod.Dockerfile

tasks:
  - name: Build & Run Container
    init: docker build -t whiskeyapi 
    command: |
      gp sync-done dockerrun
      docker run -d -p 8000:3000 --name whiskeyapi whiskeyapi
  - name: Open Swagger
    command: |
      gp sync-await dockerrun
      gp preview $(gp url 8000)/swagger/index.html 
      

vscode:
  extensions:
    - muhammad-sammy.csharp
    - ms-dotnettools.csharp
    - ms-azuretools.vscode-docker
```

This gitpod configuration file will perform the following:

1. Create the development environment based on the image in the customer dockerfile (see below).
2. The init task which will run first, and as part of prebuilds, will build the API image.
3. The command will run after the init which will run the container as an image. This also has a sync-done command which is referenced in step 4.
4. This step opens up a preview of the swagger in a simple browser. This has the sync-await command which means that the container must be set to run first before this endpoint can open.
5. The last section shows some examples of how you can add vscode extensions to your workspace. The microsoft ones will only work if you open the gitpod environment in visual studio code as the browser does not have a license to automtically install these.

I also added the gitpod.Dockerfile that the above was referencing for a dotnet image instead of the workspace full image that usually comes with gitpod. That dockerfile looked as follows.

```bash
FROM gitpod/workspace-dotnet:latest
```

I am not sure if I could actually use the standard workspace image for gitpod as I am running dotnet in a container anyway for the application, but this is still useful to debug in a dotnet environment (that I didn't have to configure!).

To see the up to date layout of the repository go to the hungovercoders [whiskey reviews repo](https://github.com/hungovercoders/whiskey.reviews).

## Create Workspace

## Configure Prebuild

## What Next??
