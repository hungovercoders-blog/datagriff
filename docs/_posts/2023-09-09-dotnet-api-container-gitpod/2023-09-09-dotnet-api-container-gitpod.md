---
title: ".Net API Container on Gitpod | Great developer experience in a cloud developer environment"
date: 2023-09-09
author: dataGriff
description: Dotnet containers in cloud developer environments for a great developer experience
image:
  path: /assets/2023-09-09-dotnet-api-container-gitpod/link.png
tags: API .Net Container Gitpod
---

Recently I decided to learn docker and all things containers. I dived deep into the deepest darkest spaces of my windows laptops configuration... My laptop suddenly got very angry with me and decided that the C drive was too full, or that suddenly docker desktop and the dotnet framework would disappear from my machine! I desperately wanted to just code and run the [whiskey api](https://github.com/hungovercoders/whiskey.reviews){:target="\_blank"} in a container without wasting time configuring my machine. Well, everyone, there is a way, and that way is using the cloud developer environment [gitpod](https://www.gitpod.io){:target="\_blank"}...

- [Prerequisites](#prerequisites)
- [Run Dotnet API Container](#run-dotnet-api-container)
- [What is Gitpod?](#what-is-gitpod)
- [Setup Gitpod](#setup-gitpod)
- [Gitpod Configuration File](#gitpod-configuration-file)
- [Containers on Containers](#containers-on-containers)
- [Create Workspace](#create-workspace)
- [Configure Prebuild](#configure-prebuild)
- [What Next??](#what-next)

## Prerequisites

- [Github Account](https://www.github.com){:target="\_blank"} - If you haven't already get yourself a github account, this is how you're going to host code and open up gitpod.
- [~~Docker Desktop~~](https://www.docker.com/products/docker-desktop/){:target="\_blank"} - Not needed!
- [~~.Net Frameworks~~](https://dotnet.microsoft.com/en-us/download/dotnet-framework){:target="\_blank"} - Not needed!
- [~~Git~~](https://git-scm.com/){:target="\_blank"} - Not needed!
- [Visual Studio Code](https://code.visualstudio.com/){:target="\_blank"} - Actually optional as you can do it all in the browser or in the desktop IDE.
- ~~Top Spec Laptop~~ - Not needed. You can use gitpod to run this on a tablet or even your [mobile phone](https://www.gitpod.io/guides/getting-started-with-gitpod-in-android){:target="\_blank"}!

## Run Dotnet API Container

The first thing I wanted to do was run the [whiskey api](https://github.com/hungovercoders/whiskey.review){:target="\_blank"} in a container. This was in a bid to make the API cloud native, allowing it to run and deploy consistently on any cloud (and developer environment). I added the file below to the repo and at first had the container running from my laptop. This was however after a lot of docker and .net framework configuration setup.

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

At this point if you have your own hardware environment configured to run containers you could run the following to build the image.

```bash
docker build -t whiskeyapiimage .
```

Then run the container with this command.

```bash
docker run -d -p 3000:3000 --name whiskeyapi whiskeyapiimage
```

However after some falling out with my laptop I decided to use gitpod as my development environment instead...

## What is Gitpod?

[Gitpod](https://gitpod.io){:target="\_blank"} is a [cloud developer environment](https://www.gitpod.io/cde){:target="\_blank"} that aims to remove the need for people to configure their own machines for development. This should also solve the "it works on my machine" statement as the code specifying the machine environment is also held with the code, therefore every developer using the codebase also gets the same environment. This is an awesome place to be and one I am now fervently behind with a view to never look back. The [documentation](https://www.gitpod.io/docs/introduction){:target="\_blank"} is excellent and be prepared to stare slack-jawed at your screen after a few [quickstarts](https://www.gitpod.io/docs/introduction/getting-started/quickstart){:target="\_blank"} when you realise the magnitude of time this tool will save. Gitpod is not alone with its cloud development offering with [github codespaces](https://github.com/features/codespaces){:target="\_blank"} for example offering a similar service and one I will also need to explore.

Gitpod leverages containers as the developer environment and you can work completely in the browser if you wish. The interface is based completely on VS code so you get a very familiar look and feel as well as the extensions, command pallete etc.

![Gitpod Browser Experience]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-browser-experience.PNG)

Gitpod can also work with other [tools](https://www.gitpod.io/docs/references/ides-and-editors){:target="\_blank"}. There are a good number of these tools in beta including [rider](https://www.gitpod.io/docs/references/ides-and-editors/rider){:target="\_blank"} as a more substantial IDE for your work if you wanted to.

You can only install extensions from [open visual studio registry](https://open-vsx.org/){:target="\_blank"} in the actual browser, to open microsoft extensions you have to open in desktop VS code. This is fine though as you can still continue running your container cloud developer environment from your desktop. Awesome!

![Gitpod VS Code]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-vs-code.PNG)

You get 50 free hours in the [free plan](https://www.gitpod.io/pricing?plan=cloud){:target="\_blank"} which I am using and then you can also expand that to other tiers as well as [hosting yourself](https://www.gitpod.io/pricing?plan=dedicated){:target="\_blank"} if you have security concerns or want more control. I have managed to control how much I use quite well so far by monitoring usage in my [account](https://gitpod.io/usage){:target="\_blank"}. I also ensure I don't have parallel workspaces running and also because after 30 minutes of no activity gitpod close it for you anyway AND they terminate after 3 minutes if you just close down the browser tab or local VS code window. Magic!

![Gitpod Usage]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-usage.PNG)

The default workspace itself is this [docker workspace full image](https://hub.docker.com/r/gitpod/workspace-full){:target="\_blank"} which is chock to the brim with [useful language and installs](https://www.gitpod.io/docs/introduction){:target="\_blank"} such as python, ruby, go, **docker**, to name but a few, that I no longer have to manage on my machine! This is hungovercoder bliss as oftentimes we have quite diminished capacity and simply need to code, so without further ado, lets get gitpod going!

## Setup Gitpod

[Setting up gitpod](https://www.gitpod.io/docs/introduction/getting-started){:target="\_blank"} is really easy, all you need is your github account to start with, then link the third party application and install the browser extension.

The first time you want to use gitpod you can first just use the appropriate URL address extended with your github repo name, e.g.

- [https://gitpod.io/#https://github.com/hungovercoders/whiskey.reviews](https://gitpod.io/#https://github.com/hungovercoders/whiskey.reviews){:target="\_blank"}

To make this even easier, install the [browser extension](https://www.gitpod.io/docs/configure/user-settings/browser-extension){:target="\_blank"} and then you get a nice button in github that you just have to click to open up your workspace.

![Gitpod Browser Extension]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-browser-extension.PNG)

You'll notice this on all github repos you visit now as the gitpod configuration file is not mandatory for a workspace, that just sets up your specific config for that codebase. You still get the default image to work on no matter what repo you open. What a glorious day to be alive! A good place to look, and just to prove this will be on all github repos you have access to, is the [gitpod samples github](https://github.com/gitpod-samples){:target="\_blank"}.

You'll then end up with a [gitpod dashboard](https://gitpod.io/workspaces){:target="\_blank"}, a place you can view your current workspaces, setup preferences and settings. Your global development settings becomes yours to configure and you can spin it up on demand, anywhere, on nearly any machine!

![Gitpod Dashboard]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-dashboard.PNG)

## Gitpod Configuration File

To run your codebase in a gitpod container you first need to add a [.gitpod.yml configuration file](https://www.gitpod.io/docs/references/gitpod-yml){:target="\_blank"}. You can do this with the following [gitpod CLI](https://www.gitpod.io/docs/references/gitpod-cli){:target="\_blank"} command:

```bash
gp init
```

I then added the following to the .gitpod.yml file in my dotnet repo.

```yaml
image:
  file: .gitpod.Dockerfile

tasks:
  - name: Build & Run Container
    init: docker build -t whiskeyapi .
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

To see the up to date layout of the repository go to the hungovercoders [whiskey reviews repo](https://github.com/hungovercoders/whiskey.reviews){:target="\_blank"}.

## Containers on Containers

Lets just pause a moment... We're about to do what?

Yes that's right we're going to run a container on a container. To be fair I have skipped a few steps ahead of the standard gitpod setup, which as per the [quickstarts](https://www.gitpod.io/docs/introduction/getting-started/quickstart){:target="\_blank"} is usually utilising language specific setups.

However, I wanted a simple way to run containers, as I want a language agnostic and cloud native way of running my applications, which containers provide. The way to do this turned out to be was to run my containers... on a container that hosted the dev environment too! The cool thing about gitpod is that it comes with a workspace image that has docker pre-installed so I don't have to worry about configuring anything on my machine. In minutes you can have an extremely powerful cloud developer environment that you can run your containers on too. It also means my codebase can be run by anyone and anywhere with no effort whatsoever. Did I mention how awesome this is? Lets see it in action...

![Gitpod Works on my Machine]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-works-my-machine.png)

## Create Workspace

Creating the workspace is now easy, you can do it from the [dashboard](https://gitpod.io/workspaces){:target="\_blank"} by selecting new workspace and choosing the repo you want to open.

![Gitpod New Workspace]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-new-workspace.PNG)

OR...

You can just navigate to the [whiskey reviews github repo](https://github.com/hungovercoders/whiskey.review){:target="\_blank"} and open using the browser extension you've installed by clicking "gitpod".

![Gitpod Browser Extension]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-browser-extension.PNG)

When you open the workspace the magic will begin to happen. The developer environment will run on the dotnet image we've specified, it will build the container whiskey api image, it will then run the api container and finally it will open the swagger page of the api as a nice convenience to prove to you it works. This is the developer experience dream.

![Gitpod Open API]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-open-api.PNG)

All of this this is based on the configuration file we supplied described above and you can see the commands having run in the terminal windows that open in your workspace.

![Gitpod Open Terminal]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-open-terminal.PNG)

"It works on my machine!". Damn straight.

## Configure Prebuild

To make these workspaces even quicker you can configure [prebuilds](https://www.gitpod.io/docs/configure/projects/prebuilds#prebuilds){:target="\_blank"}. These actually execute the before and init components of tasks in your configuration as well as ensure the workspace image is ready to rock when you call it.

You create these in projects in your [gitpod dashboard](https://gitpod.io/projects){:target="\_blank"} with a 1:1 mapping to a repo and configure them to trigger off a particular branch if you wish.

![Gitpod Projects]({{ site.baseurl }}/assets/2023-09-09-dotnet-api-container-gitpod/gitpod-projects.PNG)

The workspaces I have done so far have been so quick prebuilds have been great but not mandatory, however I can imagine as workflows and development gets more complex, these are going to be a lifesaver.

## What Next??

I'll likely be following up with more blogs but I also recommend just going through some [quickstarts](https://www.gitpod.io/docs/introduction/getting-started/quickstart){:target="\_blank"} to fully appreicate the simplicity and magnitude of the effort being reduced in your development efforts from this day forwards.

My plans now are:

- Go all in and remove all of the bloat on my machine that I require for development. That's right I have decided to completely commit to cloud developer environments and never look back. Value focus for the win!
- I am likely going to checkout [github codespaces](https://github.com/features/codespaces){:target="\_blank"} to do a comparison and understand the capabilities of multiple cloud developer environments.
- [Gitpodify](https://www.gitpod.io/guides/gitpodify){:target="\_blank"} all the things including this [blog](https://github.com/hungovercoders-blog/datagriff){:target="\_blank"} - which I already have and am writing to you from a workspace that has ruby and jekyll installed with a live browser within my browser refreshing to the right of me as I write this!
- Combine gitpod with github actions for the whiskey review to make a complete cloud hosted software development lifecycle.
- I want to look at bringing in the [cosmos db emulator container](https://hub.docker.com/r/microsoft/azure-cosmosdb-emulator){:target="\_blank"} into the whiskey review codebase and utilise cosmos within gitpod, hopefully turning this into a really useful template, including seeding with test data as part of the workspace starting.
- I want to look at creating a FARM stack template based on the work I've done with FastAPI, Mongo and React.
- I'll probably take a few steps back and do a blog on a hello world configuration for gitpod.
- I'll continue to keep this [gitpod cheatsheet](https://blog.hungovercoders.com/cheatsheets/gitpod/gitpod.html){:target="\_blank"} up to date for gitpod as part of the hungovercoders [cheatsheets](https://blog.hungovercoders.com/cheatsheets/){:target="\_blank"} and ensure it looks a bit prettier in future!

Well all of that has left me breathless and excited. If you want to know more come and speak to me or get on the [discord community](https://discord.com/channels/816244985187008514){:target="\_blank"} for gitpod which has plenty of other enthusiasts too.

I really hope this has changed your development world as much as it has changed mine. Mind blown.
