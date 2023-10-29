---
title: "Azure Terraform Cloud Developer Template | Creating a template to deploy azure infrastructure with terraform on a cloud developer environment"
date: 2023-10-29
author: dataGriff
description: Creating a template to deploy azure infrastructure with terraform on a cloud developer environment
image:
  path: /assets/2023-10-29-cloud-dev-platform-template/link.png
tags: Azure Gitpod Github Terraform CDE
---

I wanted to make some Github templates using cloud developer environments to solve my ongoing configuration and development needs. This has led to an awesome experience for myself as I can now rapidly develop and test against an Azure cloud environment in seconds using this [template.azure.platform](https://github.com/hungovercoders/template.azure.terraform) repo! Read on to find out how I did this with github, gitpod and Terraform!  

- [Prerequisites](#prerequisites)

## Prerequisites

- [Github Account](https://www.github.com) - If you haven't already get yourself a github account.
- [Gitpod](https://www.gitpod.io) - To save worrying about configuring your developer machine, I recommend using [Gitpod](https://www.gitpod.io) or [github codespaces](https://github.com/features/codespaces).
- [Azure Account](https://www.portal.azure.com) - A could environment to deploy your assets.

## Why Terraform?

Yes I have forsaken all other infrastructure as code methods and gone all in on [Terraform](https://registry.terraform.io/). The reason is that Terraform is truly could native, and pretty much "any infrastructure" native ([see Terraform providers here](https://registry.terraform.io/browse/providers)). 

**pic all providers**

It seems to be the tooling with the most coverage and so simply makes sense to become well versed in this langugage and its methods. A common criticism of Terraform is that "you need specialist infrastucture" knowledge to use it. It is only specialist knowledge when you have made a local proprietary choice with your infrastructure as code methods in your specific area. I see infrastructure or resource deployment code as a part of every developers arsenal and a universal point in that "t" across the infamous "t" shaped developer. Terraform therefore is an excellent choice for organisations and individuals who want to make cross functional and cross platform infrastructure deployment discussions easier, either with their community or within their team. These are the reasons I have decided to commit to Terraform.

## Why Cloud Developer Environment?

Cloud developer environments I believe are the future of how we will be developing code ([see Gartner report here](https://www.gartner.com/en/articles/what-s-new-in-the-2023-gartner-hype-cycle-for-emerging-technologies)).

**pic gartner**


They go one step further than docker providing the environment for your software to run, as they actually provide the environment that the software was built on in the first place. This truly solves the "it runs on my machine" issue. Another reason is that I hate configuring my machine, or more to the point I hate remembering HOW to configure my machine. Cloud develop environments allow you to wrap your configuration in an automated code solution which me it works exactly the same for whoever opens it, and you can go back to see your configuration in source control. I think as a hungovercoder it is more important that it solves the problem of "that's how I got it to work on my machine!!!" as well as the classic "it runs on my machine...". I have started dabbling with both [github codespaces]() and [gitpod](https://www.gitpod.io/cde) for cloud developer environment experiences and I would recommend you do the same to make the choice that suits you. I started my journey with gitpod, which is why the current blog sticks to this at the moment, but if you check out the repo referenced throughout it will also have the configuration mostly setup for codespaces too. They both leverage a common container setup so its very easy to make your code function for both.
I am aiming to do a fair comparison between the two when I think I am ready towards the end of the year. At the moment my summary would be that github codespaces have a huge amount of functionality, quickstarts and I get to leverage more compute credits as I already have [github pro](). Gitpod, while less bells and whistles, seems to still be a far smooth and quicker experience, as well as not abstracting too much away so that it takes away the knowledge of how you configured your machine. I find codespaces provide more of a template quickstart and would be the best choice for beginners, but gitpod has allowed me to figure out "how it worked on my machine" and place that in code, without me not knowing how I got it to work in the first place, which is still an important thing at least at this point for developers to understand.

## Create base image with prebuild

### Declare docker file

I initially tried to install the Azure CLI and Terraform as part of the gitpod configuration file. I thought this was adding too much time to when I opened up my environment. My environment was also all based on the [gitpod full image](https://hub.docker.com/layers/gitpod/workspace-full/latest/images/sha256-811f72def04ed647cb4cb991771db8d3c6d9ceeec2f164fadda3db703eb54469?context=explore) and I thought that this 2.5 GB image was far too large for what I need specifically for this environment, simply a linux distribution, [brew](https://brew.sh/) (to provide me easy ability to install terraform and azure cli), terraform and the azure cli. After speaking to the lovely people on the [gitpod discord community](https://discord.com/channels/816244985187008514) they then recommended that I put all these installations into the docker file itself and use the [workspace-base image](https://hub.docker.com/layers/gitpod/workspace-base/latest/images/sha256-7bc9afe251dc71cd50b7aaeebfd1ed80690a9080c43322e39a57fc9959f6af6d?context=explore), which is only around 600 MB in size. This made my docker image a third of the size and cut the environment startup time to a few seconds once I had configured prebuilds (see next section). The docker file I called ".cde.Dockerfile" and added to the root of my git repo with this code. This initaites a container from the gitpod base image, installs [brew](https://brew.sh/), then uses brew to install terraform and the azure cli.

```bash
FROM gitpod/workspace-base

USER gitpod

# Install Homebrew
RUN /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
    echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc

# Update Homebrew, Install Terraform & Azure CLI
RUN eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)" && \
    brew update && \
    brew tap hashicorp/tap && \
    brew install hashicorp/tap/terraform && \
    brew install azure-cli
```

### Configure prebuild

You can take advantage of [prebuilds](https://www.gitpod.io/docs/configure/projects/prebuilds) in gitpod which basically... well pre-build your environment so that when you open it next time it will be faster. This prebuild creates whatever the image is for your docker file and also runs any init tasks that you have in your configuration. I didn't have any init tasks planned but having the container ready made and the tools installed once up-front is a massive time saver.

## Create Azure CLI Initialisation

### Create app reg

### Add configuration

### Create Azure startup scripts

## Create Terraform Initialisation

### Create storage account

### Create Terraform startup scripts

## Deploy a Resource Group

## Clone Template for Azure Container Environment

## What next?
