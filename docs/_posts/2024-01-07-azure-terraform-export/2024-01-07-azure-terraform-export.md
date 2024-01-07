---
title: "Exporting Azure Resources into Terraform with aztfexport"
date: 2024-01-07
author: dataGriff
description: Exporting Azure Resources into Terraform with aztfexport
image:
  path: /assets/2024-01-07-azure-terraform-export/link.png
tags: Azure Terraform
---

The hungovercoders [template.azure.terraform repo](https://github.com/hungovercoders/template.azure.terraform) is now an absolute beast and one the template I frequently use as a starting point for any codebases that will deploy infrastructure to Azure. However, I wanted to know if there was a way to fastrack anyone who doesn't want to convert their ARM or bicep from first principles... The answer is yes and it is [aztfexport](https://github.com/Azure/aztfexport)! Lets crack open a can and automate those terraform files!

- [Prerequisites](#prerequisites)
- [Import the Resources](#import-the-resources)
- [Validate Terraform Resources with Plan](#validate-terraform-resources-with-plan)
- [Apply to a New Resource Group](#apply-to-a-new-resource-group)
- [Use the Template](#use-the-template)

## Prerequisites

You can either:

- Use the hungovercoders [template.azure.terraform repo](https://github.com/hungovercoders/template.azure.terraform) in a cloud developer environment that will come with absolutely everything you need to get started. See tje README for detailed instructions of how to use. The section [importing existing azure resources into terraform](https://github.com/hungovercoders/template.azure.terraform#importing-existing-azure-resources-into-terraform) is essentially the root of this blog post.

OR you will need to install:

- [VS Code](https://code.visualstudio.com/)
- [VS Code Terraform Extension](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform)
- [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
- [aztfexport](https://github.com/Azure/aztfexport/releases)

For these last three I used brew to install as part of the docker container for the cloud developer environment that the template produces, see [here](https://github.com/hungovercoders/template.azure.terraform/blob/main/.cde.Dockerfile).

I certainly prefer option (1) as its all done for me. The methods and screenshots below will be based on the template cloud developer environment, but it will still all be relevant to if you perform the tasks locally.

## Import the Resources

First ensure you have an empty directory and navigate to that directory by running the following in a terminal:

```bash
mkdir tfexport
cd tfexport
```

You'll then want to select a resource group that you have permissions on with the account your authenticated with. If you're using the template repo this will be the account that you have setup with. If you want to do this locally or if you want to change to your individual account for the import, execute the following to change the context to you and the appropriate subscription the resource group resides in, otherwise carry on to the next step.

```bash
az login --use-device-code
az account set --subscription "your_subcription_name"
az account show
```

The resource group I have chose contains:

- A hello world container app
- A key vault
- A serverless cosmos database

![Resource Group Original](images/resource_group_original.png)

Run the following command from that directory with the rg parameter taking in the resource group you want to import. The below imports a resource group called "dev-containerapp-rg-hngc" from the subscription we have authenticated against in the previous setup steps.

```bash
aztfexport rg lrn-containerapp-rg-hngc
```

You should see "initializing" in the terminal.

![Aztfexport Initializing](images/aztfexport_initialising.PNG)

Sometimes there are a load of "skips" you might see as it does not have the ability to import absolutely everything, but this hasn't been a problem for me so far as they are usually "behind the scenes" type resources. There are a number of options present though and so for now I choose "w" which is just the import all option.

![Aztfexport Options](images/aztfexport_options.png)

You'll then see "importing" if it has kicked off correctly.

![Aztfexport Importing](images/aztfexport_importing.png)

After a period you should see the appropriate terraform files in the directory that you can use as a starting point.

![Aztfexport Imported](images/aztfexport_imported.png)

## Validate Terraform Resources with Plan

You can then run a terraform plan from the tfexport directory to validate the infrastructure is as you expect with "no changes" in the output.

```bash
terraform plan
```

![Terraform Plan](images/terraform_plan.png)

## Apply to a New Resource Group

We'll keep this simple and pretend we're going to take this resource group from learning environment (lrn) to the production environment. To do this we're going to create an environment variable and allow us to pass that in to change anything referencing "lrn" to "prd".

We'll first need to delete the terraform files and migrate the state so that the local state knows that we are going to start referencing brand new resources.

Delete the following files and directories:

- import.tf
- .terraform.locl.hcl
- .terraform directory

Then migrate the state:

```bash
terraform init -migrate-state
```

![Terraform Migrate](images/terraform_migrate.png)

Then amend the main.tf file to take in the variable and amend all the resources to reference this:

e.g.

```hcl
variable "environment_shortcode" {
  type        = string
  description = "The is the environment shortcode for resources"
  validation {
    condition     = contains(["lrn", "dev", "prd"], var.environment)
    error_message = "The environment shortcode is not valid, it should be lrn, dev or prd."
  }
}

resource "azurerm_resource_group" "res-0" {
  location = "northeurope"
  name     = "${var.environment_shortcode}-containerapp-rg-hngc"
  tags = {
    team = "hungovercoders"
  }
}

##repeat for all resources referencing "lrn"
```

We now run terraform plan and we can see that resources are going to be added.

```bash
terraform plan
```

![Terraform Plan New](images/terraform_plan_new.png)

Run terraform apply and watch the new resource group get created identical to the learning environment but in "production".

```bash
terraform apply
```

![Terraform Apply](images/terraform_apply_new.png)

In this example the resource group at the end looks like this:

![Resource Group New](images/resource_group_new.png)

## Use the Template

If you're using the [template](https://github.com/hungovercoders/template.azure.terraform) you can move the imported code into the terraform folder and start tweaking it to meet your needs. This becomes a really quick start to import azure resources into terraform, utilise a cloud developer environment with all the tooling ready and a github actions pipeline ready for you to deploy. Now that is a happy new year!
