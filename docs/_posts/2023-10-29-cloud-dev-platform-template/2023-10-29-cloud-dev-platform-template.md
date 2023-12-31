---
title: "Azure Terraform Gitpod Cloud Developer Template | Creating a Github template to deploy azure infrastructure with terraform in Azure using Gitpod"
date: 2023-10-29
author: dataGriff
description: Creating a Github template to deploy azure infrastructure with terraform in Azure using gitpod
image:
  path: /assets/2023-10-29-cloud-dev-platform-template/link.png
tags: Azure Gitpod Github Terraform CDE
---

I wanted to make some Github templates using cloud developer environments to solve my ongoing configuration and development needs for infrastructure deployment. This has led to an awesome experience for myself as I can now rapidly develop and test against an Azure cloud environment in seconds using this [template.azure.platform](https://github.com/hungovercoders/template.azure.terraform){:target="_blank"} repo! Read on to find out how I did this with github, gitpod and Terraform!  

- [Prerequisites](#prerequisites)
- [Why Terraform?](#why-terraform)
- [Why Cloud Developer Environment?](#why-cloud-developer-environment)
- [Create base image with prebuild](#create-base-image-with-prebuild)
  - [Declare docker file](#declare-docker-file)
  - [Configure prebuild](#configure-prebuild)
- [Create Azure CLI Initialisation](#create-azure-cli-initialisation)
  - [Create Azure Application Registration](#create-azure-application-registration)
  - [Add Azure Configuration to Gitpod](#add-azure-configuration-to-gitpod)
  - [Create Azure startup scripts](#create-azure-startup-scripts)
- [Create Terraform Initialisation](#create-terraform-initialisation)
  - [Create storage account](#create-storage-account)
  - [Complete Terraform files](#complete-terraform-files)
  - [Create Terraform startup scripts](#create-terraform-startup-scripts)

## Prerequisites

- [Github Account](https://www.github.com){:target="_blank"} - If you haven't already get yourself a github account.
- [Gitpod](https://www.gitpod.io){:target="_blank"} - To save worrying about configuring your developer machine, I recommend using [Gitpod](https://www.gitpod.io) or [github codespaces](https://github.com/features/codespaces).
- [Azure Account](https://www.portal.azure.com){:target="_blank"} - A could environment to deploy your assets.

## Why Terraform?

Yes I have forsaken all other infrastructure as code methods and gone all in on [Terraform](https://registry.terraform.io/){:target="_blank"}. The reason is that Terraform is truly could native, and pretty much "any infrastructure" native ([see Terraform providers here](https://registry.terraform.io/browse/providers){:target="_blank"}).

![Terraform Providers]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/terraform_providers.PNG)

It seems to be the tooling with the most coverage and so simply makes sense to become well versed in this language and its methods. A common criticism of Terraform is that "you need specialist infrastructure" knowledge to use it. It is only specialist knowledge when you have made a local proprietary choice with your infrastructure as code methods in your specific area. I see infrastructure or resource deployment code as a part of every developers arsenal and a universal point in that "t" across the infamous "t" shaped developer. Terraform therefore is an excellent choice for organisations and individuals who want to make cross functional and cross platform infrastructure deployment discussions easier, either with their community or within their team. These are the reasons I have decided to commit to Terraform.

## Why Cloud Developer Environment?

Cloud developer environments I believe are the future of how we will be developing code ([see Gartner report here](https://www.gartner.com/en/articles/what-s-new-in-the-2023-gartner-hype-cycle-for-emerging-technologies){:target="_blank"}).

![Gartner 2023]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/gartner.PNG)

They go one step further than docker providing the environment for your software to run, as they actually provide the environment that the software was built on in the first place. This truly solves the "it runs on my machine" issue. Another reason is that I hate configuring my machine, or more to the point I hate remembering HOW to configure my machine. Cloud develop environments allow you to wrap your configuration in an automated code solution which me it works exactly the same for whoever opens it, and you can go back to see your configuration in source control. 

I think as a hungovercoder it is more important that it solves the problem of "that's how I got it to work on my machine!!!" as well as the classic "it runs on my machine...". I have started dabbling with both [github codespaces](https://github.com/features/codespaces){:target="_blank"} and [gitpod](https://www.gitpod.io/cde){:target="_blank"} for cloud developer environment experiences and I would recommend you do the same to make the choice that suits you. I started my journey with gitpod, which is why the current blog sticks to this at the moment, but if you check out the [repo](https://github.com/hungovercoders/template.azure.terraform){:target="_blank"} referenced throughout it will also have the configuration mostly setup for codespaces too. They both leverage a common container setup so its very easy to make your code function for both. I fully expect the repo to keep evolving so keep an eye...

I am aiming to do a fair comparison between the two when I think I am ready towards the end of the year. At the moment my summary would be that github codespaces have a huge amount of functionality, co-pilot(!), quickstarts, Microsoft extensions in the browser, and I get to leverage more compute credits as I already have github pro. Gitpod, while less bells and whistles, seems to still be a smoother and quicker experience, as well as not abstracting too much away so that it takes away the knowledge of how you configured your machine. I find codespaces provide more of a template quickstart and would be the best choice for beginners, but gitpod has allowed me to figure out "how it worked on my machine" and place that in code, without me not knowing how I got it to work in the first place, which is still an important thing at least at this point for developers to understand. I am looking forward to comparing the two in more detail and from a fairer perspective in the future.*

**Edit:** During the writing of this particular blog post I used github codespaces as I had started using [github.dev](https://github.dev/github/dev){:target="_blank"} (who knew??) to make some simple markdown edits, and then I had an issue with the gitpod API, saying I had hit a limit on requests. The experience of codespaces was actually very slick and co-pilot completed a lot of work for me, which was nice. It's so tough to call!

## Create base image with prebuild

First create as much of the environment as you can in your docker file. This means you can use it across cloud environments and you can configure prebuilds to make your environments quicker to startup.

### Declare docker file

I initially tried to install the Azure CLI and Terraform as part of the gitpod configuration file. I thought this was adding too much time to when I opened up my environment. My environment was also all based on the [gitpod full image](https://hub.docker.com/layers/gitpod/workspace-full/latest/images/sha256-811f72def04ed647cb4cb991771db8d3c6d9ceeec2f164fadda3db703eb54469?context=explore){:target="_blank"} and I thought that this 2.5 GB image was far too large for what I needed specifically for this environment, simply a linux distribution, [brew](https://brew.sh/) (to provide me easy ability to install terraform and azure cli), terraform and the azure cli. After speaking to the lovely people on the [gitpod discord community](https://discord.com/channels/816244985187008514){:target="_blank"} they then recommended that I put all these installations into the docker file itself and use the [workspace-base image](https://hub.docker.com/layers/gitpod/workspace-base/latest/images/sha256-7bc9afe251dc71cd50b7aaeebfd1ed80690a9080c43322e39a57fc9959f6af6d?context=explore){:target="_blank"}, which is only around 600 MB in size. This made my docker image a third of the size and cut the environment startup time to a few seconds once I had configured prebuilds (see next section). The docker file I called ".cde.Dockerfile" and added to the root of my git repo with this code. 

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

This initiates a container from the gitpod base image, installs [brew](https://brew.sh/){:target="_blank"}, then uses brew to install terraform and the azure cli. I made a "standardised" decision to start prefixing files and directories with "cde" to represent "cloud developer environment" with a view to hopefully use common configuration across the multiple tools (gitpod, github codespaces, ANother).

### Configure prebuild

You can take advantage of [prebuilds](https://www.gitpod.io/docs/configure/projects/prebuilds){:target="_blank"} in gitpod which basically... well pre-build your environment so that when you open it next time it will be faster. This prebuild creates whatever the image is for your docker file and also runs any init tasks that you have in your configuration. I didn't have any init tasks planned but having the container ready made and the tools installed once up-front is a massive time saver. Using this it now take seconds to open up the environment for this template.

![Gitpod Prebuilds]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/gitpod_prebuilds.PNG)

## Create Azure CLI Initialisation

### Create Azure Application Registration

Initially when I setup this environment I used my own credentials to login to Azure when the environment opened using this command in the gitpod configuration.

```bash
az login --use-device-code
```

This however this involved me having to look at the terminal, copy a code and login externally. It was all part of the process... but I wanted to integrate into Azure in a completely automated manner... I have no time for this manual interaction! This was just my developer environment after all. I therefore decided to use a an application registration and see if I could use that to automatically login, with the aspiration to be able to allow the Terraform validation and plan to all occur as part of the environment startup too (see later sections).

You can either create an Azure application registration in the portal like this:

![Azure App Reg]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/azure_app_reg.PNG)

Or you can use the cloud shell in the Azure portal using this command:

```bash
az ad app create --display-name aprg-hungovercoders-lrn-admin
```

The values you are going to need from your Azure environment and application registration to plug into your gitpod configuration are:

- Tenant ID
- Subscription Name
- Client ID
- Client Secret

I also granted this application registration the "Owner" role on my subscription so that it could do anything just to get it working. I am not sure if this is the best role to use, but it worked for me. I am sure there is a more granular role that could be used. Oops! Hic(!)...

![Azure Role]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/azure_app_reg_role.PNG)

### Add Azure Configuration to Gitpod

You can add variables to gitpod either at a user level or at an individual project level. An individual project essentially maps to a repository in github. I decided to add the variables at the user level so that I could reuse these credentials against my developer environment for any repository I wanted to use. I scoped the variables to be for "hungovercoders/*" though so that these environment variables only appeared in projects/repos prefixed with this organisation.

![Gitpod Variables]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/gitpod_variables.PNG)

The reason I used the naming convention of "ARM_..." in upper case is because during my experimentation with this I found that the variables named like this were native to Terraform and they picked them up automatically.

### Create Azure startup scripts

In order to continue down my route of being cloud developer environment agnostic, I created external scripts to run the Azure CLI installation commands. I created a directory called "cde" in the root of my git repo and added the following script called "azure.sh" to it.

```bash
az login --service-principal -u $ARM_CLIENT_ID -p $ARM_CLIENT_SECRET --tenant $ARM_TENANT_ID
az account set --subscription "$ARM_SUBSCRIPTION_NAME"
az account show
```

I then referenced this script in the .gitpod.yml configuration file like this.

```bash
image:
  file: .cde.Dockerfile

tasks:
  - name: Azure CLI
    command: |
      sh ./cde/azure.sh
```

When you open up the environment now you will see that the Azure CLI is installed and you are logged in from the "Azure CLI" terminal.

![Azure CLI]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/azure_cli.PNG)

## Create Terraform Initialisation

### Create storage account

I wanted to store my Terraform state in Azure so that I could share it across multiple environments. I created a storage account in Azure called "stateeundgrf" in a resource group called "state-rg" and then created a container called "state" in it.
This was all a bit rushed so please change these to be more suitable names!

![Storage Account]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/storage_account.PNG)

I then created a file called "versions.tf" in a terraform directory of my git repo with the following code. This sets the version of the terraform providers as well as stating that I am going to hold my state in Azure storage. The Azure CLI initialisation in the previous step and the permissions we gave the application registration means this all works fine.

```hcl
terraform {


  backend "azurerm" {
    resource_group_name  = "state-rg"
    storage_account_name = "stateeundgrf"
    container_name       = "state"
    key                  = "terraform.tfstate"
  }

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.62.1"
    }
  }

  required_version = ">= 1.2.3"

}

provider "azurerm" {
  features {}
}
```

### Complete Terraform files

Add another three files in the terraform directory to make a resource group in Azure. This simple template can be used and modified when they want to add any other resources to Azure then.

**Variables.tf**
```hcl
variable "region" {
  type        = string
  default     = "northeurope"
  description = "The is the Azure region the resources will be deployed into."
  validation {
    condition     = contains(["northeurope", "westeurope"], var.region)
    error_message = "The region is not in the correct region."
  }
}

variable "environment" {
  type        = string
  default     = "learning"
  description = "The is the environment the resources belong to. e.g. learning, development, production."
  validation {
    condition     = contains(["learning", "development", "production"], var.environment)
    error_message = "The environment is not valid."
  }
}

variable "team" {
  type        = string
  default     = "hungovercoders"
  description = "The is the team that own the resources."
  validation {
    condition     = contains(["datagriff", "hungovercoders", "dogadopt"], var.team)
    error_message = "The team is not valid."
  }
}

variable "organisation" {
  type        = string
  default     = "hungovercoders"
  description = "The is the organisation that owns the resources."
  validation {
    condition     = contains(["datagriff", "hungovercoders", "dogadopt"], var.organisation)
    error_message = "The organisation is not valid."
  }
}

variable "domain" {
  type        = string
  default     = "platform"
  description = "The is the business problem domain being solved by the resources."
}

variable "azure_namespace" {
  type        = string
  default     = "hngc"
  description = "The is the unique namespace added to resources."
}

locals {
  region_shortcode      = (var.region == "northeurope" ? "eun" : var.region == "westeurope" ? "euw" : "unk")
  environment_shortcode = (var.environment == "learning" ? "lrn" : var.environment == "development" ? "dev" : var.environment == "production" ? "prd" : "unk")
  resource_group_name   = "${local.environment_shortcode}-${var.domain}01-rg"

  tags = {
    environment  = var.environment
    organisation = var.organisation
    team         = var.team
    domain       = var.domain
  }
}
```

**Main.tf**
```hcl
resource "azurerm_resource_group" "rg" {
  name     = local.resource_group_name
  location = var.region
  tags     = local.tags
}
```

**Output.tf**
```hcl
output "resource_group_id" {
  value = azurerm_resource_group.rg.id
}
```

### Create Terraform startup scripts

Just like I did with the Azure CLI, I created an external bash script called "terraform.sh" to run the Terraform commands to initialise, format, validate and plan in the cde directory.

```bash
cd  terraform
terraform init
terraform fmt
terraform validate
terraform plan
```

I then referenced this script in the .gitpod.yml configuration file like this. Notice that I added a "gp sync-await waitonazurecli" on the Terraform task so that it would wait for the Azure CLI task to complete before running, which has the corresponding "gp sync-done waitonazurecli" in the Azure CLI task. I also added the hashicorp terraform visual studio code extension so this will always be available too.

```bash

```bash
image:
  file: .cde.Dockerfile

tasks:
  - name: Terraform
    command: |
      gp sync-await waitonazurecli
      sh ./cde/terraform.sh
  - name: Azure CLI
    command: |
      sh ./cde/azure.sh
      gp sync-done waitonazurecli

vscode:
  extensions:
    - hashicorp.terraform
```

When you open up the environment now you will see that the Terraform tasks run after the Azure CLI has completed.

![Azure CLI]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/terraform.PNG)

Bingo! Everything is hooked up and whenever anyone opens up this project they're good to with some terraforming in Azure in seconds. A perfect template repo to start any of your infrastructure as code ventures.

![Github Template]({{ site.baseurl }}/assets/2023-10-29-cloud-dev-platform-template/use_template.PNG)
