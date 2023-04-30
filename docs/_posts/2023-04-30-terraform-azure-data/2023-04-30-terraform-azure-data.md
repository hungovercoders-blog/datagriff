---
title: "Terraform Azure Data Learning Platform"
date: 2023-04-30

author: dataGriff
---

I am quite often creating various data assets like data lake storage, databricks etc on Azure for learning. I want to automate the provision of these to make my life easier and so I decided to crack open a can and learn some [terraform on Azure](https://developer.hashicorp.com/terraform/tutorials/azure-get-started) with github actions to make this repeatable!

- [Pre-Requisites](#pre-requisites)
- [Diagram](#diagram)
- [Terraform an Azure Resource Group with Local State](#terraform-an-azure-resource-group-with-local-state)
- [Setup Terraform Cloud](#setup-terraform-cloud)
- [Deploy Resource Group with Github Action](#deploy-resource-group-with-github-action)
- [Deploy Databricks Workspace and Data Lake Storage](#deploy-databricks-workspace-and-data-lake-storage)

## Pre-Requisites

- You'll need an [azure subscription](portal.azure.com) to host your data infrastructure.
- You'll need an IDE like  [visual studio code](https://code.visualstudio.com/).
- You'll need to install [terraform](https://developer.hashicorp.com/terraform/downloads).
- You'll need a [github account](https://github.com/) for source control and deployment with github actions. 
- You'll want a [hashicorp developer account](https://developer.hashicorp.com/) and [terraform cloud account](https://app.terraform.io/) to host your state files.

## Diagram

1. We're going to be deploying our infrastructure assets to Azure.
1. We're going to be storing the state of our infrastructure in terraform cloud.
1. We're going to be leveraging github for source control and deployment with github actions.

## Terraform an Azure Resource Group with Local State

First lets create the simplest possible deployment possible using local state. Create a new directory on your local machine called azure.platform and initialise a git repo with a README.md. The end file structure is going to look like the following:

```file
azure.platform
│   README.md
|   .gitignore    
|   main.tf
|   outputs.tf
|   variables.tf
|   versions.tf
```

First add a [.gitignore file for terraform](https://github.com/github/gitignore/blob/main/Terraform.gitignore) which can be found at the useful [.gitnore](https://github.com/github/gitignore) repository at github.

Create a versions.tf file and add the following code:

```hcl
terraform {

  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.10.0"
    }
  }

  required_version = ">= 1.2.3"
}

provider "azurerm" {
  features {}
}
```

This file sets the providers required for this particular deploy which is Azure. You can see the huge amount of providers available at the [terraform registry](https://registry.terraform.io/browse/providers).

Create a variables.tf file and add the following code:

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
  default     = "lrn"
  description = "The is the environment the resources belong to. e.g. lrn, dev, prd."
  validation {
    condition     = contains(["lrn", "dev", "prd"], var.environment)
    error_message = "The environment is not valid."
  }
}

variable "team" {
  type        = string
  default     = "myteam1"
  description = "The is the team that own the resources."
  validation {
    condition     = contains(["myteam1","myteam2"], var.team)
    error_message = "The team is not valid."
  }
}

variable "organisation" {
  type        = string
  default     = "myorganisation1"
  description = "The is the organisation that owns the resources."
  validation {
    condition     = contains(["myorganisation1","myorganisation2"], var.organisation)
    error_message = "The organisation is not valid."
  }
}

variable "domain" {
  type        = string
  default     = "learning"
  description = "The is the business problem domain being solved by the resources."
}

locals {
  resource_group_name = "${var.environment}-${var.domain}-rg"
  tags = {
    environment = var.environment
    team        = var.team
    domain      = var.domain
  }
}
```

Take a look at the variables in the file and change any of them to suit your needs. This may include the region if you need to deploy somewhere other than the european regions and the team or organisation may need amending. I usually leave these tags even when testing as it keeps my mind focused on the boundaries I need in my infrastructure, but feel free to take them out entirely.

This variables file will feed into our main.tf file to make them reusable and keep the resource logic quite clean. Notice at the bottom we have declared "locals" which are construction some common resource component names and tags that we want to be consistent everywhere.

Create a main.tf file and add the following code:

```hcl
resource "azurerm_resource_group" "rg" {
  name     = local.resource_group_name
  location = var.region
  tags     = local.tags
}
```

This file now has a really simple structure for an azure resource group, taking its configuration from the variables.tf file. The alias of the resource group "rg" will come in useful later when we reference its variables for subsequent resources.

Create an outputs.tf file and add the following code:

```hcl
output "resource_group_id" {
  value = azurerm_resource_group.rg.id
}
```

Next run the following terraform commands:

```bash
terraform init
terraform fmt
terraform validate
```

The terraform init will register the required provider files locally, much like a python library or .net package, but because of our .gitignore file these will not be committed to source. It will also created a terraform lock file which will remain under source control that states the required versions of the providers.
The terraform fmt command will format all your terraform files to ensure they are correct and return a list of any its needed to format.
The terraform validate command will then check that your terraform code is valid and return any issues it finds.

You'll now need to login to your azure subscription using the CLI and set the subscription you want to deploy your infrastructure into.

```bash
az login
az account set --subscription "%AZURE_SUBSCRIPTION%"
az account show
```

Next run the following terraform command

```bash
terraform plan
```

Finally terraform plan will generate a plan for the action that the terraform deploy will take. During this command you'll see some transient state files get created locally and then disappear. Terraform plan is a great feature as it helps you understand what state changes are going to occur.

Now you are ready to deploy your resource group with the following command:

```bash
terraform apply -auto-approve
```

The -auto-approve parameter removes the need for you to have to manually input "yes" in the console when deploying. Once this command has finished you should see your resource group in the portal with all the lovely tag goodness we gave it.



You'll also notice a state file has been created locally called "terraform.tfstate". If you look in this file it basically contains the ARM template for the resource group you deployed. This file is also not included in source control as it is part of the .gitgnore configuration. This is because this is how terraform manages the state of the resources you want to deploy, source control should only contain the mechanisms of the desired state declaration, so we need to manage the actual state of the resources in external files somewhere else. Traditionally this state file management will have been managed by bespoke external stores such as [Azure storage](https://developer.hashicorp.com/terraform/language/state/remote), but now it is recommended you store you infrastructure state in Terraform cloud...

## Setup Terraform Cloud

## Deploy Resource Group with Github Action

## Deploy Databricks Workspace and Data Lake Storage