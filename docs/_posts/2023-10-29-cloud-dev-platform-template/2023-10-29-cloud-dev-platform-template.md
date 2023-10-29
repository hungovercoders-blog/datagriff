---
title: "Azure Terraform Cloud Developer Template | Creating a template to deploy azure infrastructure with terraform on a cloud developer environment"
date: 2023-10-29
author: dataGriff
description: Creating a template to deploy azure infrastructure with terraform on a cloud developer environment
image:
  path: /assets/2023-10-29-cloud-dev-platform-template/link.png
tags: Azure Gitpod Github Terraform CDE
---

After the disappoint of the rugby and the need to distract myself from the lingering hangover I decided to throw down myself a challenge... To deploy a dotnet API hosted on a container app in Azure as quickly as possible with all my favourite tools like docker, terraform, gitpod and github actions. That's it. Nice and simple. Lets dooo eeet!

- [Prerequisites](#prerequisites)
- [Create the Platform](#create-the-platform)
  - [Manual](#manual)
  - [Terraform](#terraform)
- [Create the Template API](#create-the-template-api)
- [Create the Container App](#create-the-container-app)
- [Use Deployment Centre to Create Automated Deployment](#use-deployment-centre-to-create-automated-deployment)
- [Lets Turn this into a Template](#lets-turn-this-into-a-template)
- [Summary](#summary)

## Prerequisites

- [Github Account](https://www.github.com) - If you haven't already get yourself a github account.
- [Gitpod](https://www.gitpod.io) - To save worrying about configuring your developer machine, I recommend using [Gitpod](https://www.gitpod.io) or [github codespaces](https://github.com/features/codespaces).
- [Azure Account](https://www.portal.azure.com) - A could environment to deploy your assets.

## Why Terraform?

Yes I have forsaken all other infrastructure as code methods and gone all in on Terraform. [The reason is that Terraform is truly could native, and pretty much "any infrastructure" native](https://registry.terraform.io/browse/providers). It seems to be the tooling with the most coverage and so simply makes sense to become well versed in this langugage and its methods. A common criticism of Terraform is that "you need specialist infrastucture" knowledge to use it. It is only specialist knowledge when you have made a local proprietary choice with your infrastructure as code methods in your specific area. I see infrastructure or resource deployment code as a part of every developers arsenal and a universal point in that "t" across the infamous "t" shaped developer. Terraform therefore is an excellent choice for organisations and individuals who want to make cross functional and cross platform infrastructure deployment discussions easier, either with their community or within their team. These are the reasons I have decided to commit to Terraform.

## Why Cloud Developer Environment?

Cloud developer environments I believe are the future of how we will be developing code. They go one step further than docker providing the environment for your software to run and actually provide the environment that the software was built on in the first place. This truly solves the "it runs on my machine" issue. I also hate configuring my machine, or more the point I hate remembering HOW to configure my machine. Cloud develop environments allow you to wrap your configuration in an automated code solution which me it works exactly the same for whoever opens it, and you can go back to see your configuration in source control. I think as a hungovercoder it more importantly solves the problem of "that's how I got it to work on my machine!!!" as well as the classic "it runs on my machine...". I have started dabbling with both github codespaces and gitpod for cloud developer environment experiences and I would recommend you do the same to make the choice that suits you. I started my journey with gitpod, which is why the current blog sticks to this at the moment, but if you check out the repo referenced throughout it will also have the configuration mostly setup for codespaces too. They both leverage a common container setup so its very easy to make your code function for both.
I am aiming to do a fair comparison between the two when I think I am ready towards the end of the year. At the moment my summary would be that github codespaces have a huge amount of functionality, quickstarts and I get to leverage more compute credits as I already have github pro. Gitpod, while less bells and whistles, seems to still be a far smooth and quicker experience, as well as not abstracting too much away so that it takes away the knowledge of how you configured your machine. I find codespaces provide more of a template quickstart and would be the best choice for beginners, but gitpod has allowed me to figure out "how it worked on my machine" and place that in code, without me not knowing how I got it to work in the first place, which is still an important thing at least at this point for developers to understand.

## Create base image with prebuild

### Declare docker file

### Configure prebuild

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
