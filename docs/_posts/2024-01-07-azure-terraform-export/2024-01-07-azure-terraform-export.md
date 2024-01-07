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
- [Apply to New Resource Group](#apply-to-new-resource-group)
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

You'll then want to select a resoure group that you have permissions on with the account your authenticated with. If you're using the template this will be the account that you have setup with. If you want to do this locally or if you want to change to your individual account for the import, execute the following to change the context to you and the appropriate subscription the resource group resides in, otherwise carry on to the next step.

```bash
az login --use-device-code
az account set --subscription "your_subcription_name"
az account show
```

Run the following command from that directory with the rg parameter taking in the resource group you want to import. The below imports a resource group called "dev-containerapp-rg-hngc" from the subscription we have authenticated against in the previous setup steps.

```bash
aztftexport rg dev-containerapp-rg-hngc
```

You should see "initializing" in the terminal. 

![Aztfexport Initializing](images/aztfexport_initialising.PNG)

Often there are a load of "skips" you might see as it does not import everything. There are a number of options present though and so I choose "w" which is the import all option.

![Aztfexport Options](images/aztfexport_options.png)

You'll then see "importing" if it has kicked off correctly.

![Aztfexport Importing](images/aztfexport_importing.png)

After a period you should see the appropriate terraform files in the directory that you can use as a starting point.

![Aztfexport Imported](images/aztfexport_imported.png)

## Validate Terraform Resources with Plan

You can then run a terraform plan to validate the infrastructure is as you expect with "no changes" in the output.

```bash
terraform plan
```

![Aztfexport Plan](images/aztfexport_plan.png)

From here you can move the files into the template "terraform" location and leverage everything that has already been setup in this repo, running terraform plan and apply as you would normally while you develop.

I recommend reading further the [microsoft documentation](https://learn.microsoft.com/en-us/azure/developer/terraform/azure-export-for-terraform/export-terraform-overview) and the github [repo](https://github.com/Azure/aztfexport) for the tool to understand how to use it further and for any updates.

## Apply to New Resource Group

## Use the Template
