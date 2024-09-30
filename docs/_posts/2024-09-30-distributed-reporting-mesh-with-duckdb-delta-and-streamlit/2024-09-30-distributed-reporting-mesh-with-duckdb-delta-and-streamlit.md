---
title: "Distributed Reporting Mesh with Duckdb Delta and Streamlit"
date: 2024-09-30
author: dataGriff
description: "Distributed Reporting Mesh with Duckdb Delta and Streamlit"
image:
  path: assets/2024-09-30-distributed-reporting-mesh-with-duckdb-delta-and-streamlit/link.png
tags: Duckdb Delta Streamlit Azure
---

Cheese and wine is often a precursor to hungover coding. I decided I wanted to make a reporting suite for both cheese and wine domains without the need for any heavy enterprise machinery. I also wanted to ensure that I could finally source control my business intelligence style applications. Everything we read seems to point us in the direction that this is impossible... Well goodbye heavy clusters, hello [duckdb](https://duckdb.org/){:target="\_blank"} and goodbye GUI interface reporting, hello [streamlit](https://streamlit.io/){:target="\_blank"}! Read on to find a quick start in combining these technologies to create a distributed reporting mesh along with the open source [delta lake](https://delta.io/){:target="\_blank"} file format.

## Pre-Requisites

- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}
- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [Python](https://www.python.org/downloads/){:target="\_blank"}
- [Azure Account](https://azure.microsoft.com/en-us/){:target="\_blank"}
- [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli){:target="\_blank"}

As always I will be using the mighty [gitpod](https://gitpod.io){:target="\_blank"} so I won't need to configure anything other than spinning up a workspace.

## Azure Data Lake Storage

We will want somewhere remote that we can store and access our data. I have gone for Azure data lake as it is storage I am familiar with. You could easily use storage from other cloud providers and upload your data there. The following code:

- Logs in to Azure
- Creates a cheese resource group
- Creates a cheese data lake storage account and container
- Creates a wine resource group
- Creates a wine data lake storage account and container
- **Important** - For ease of demonstration these storage accounts are being created with public access enabled to more easily read the data. Do not do this in production environments!

You can run this from VS code, your terminal or even the cloud shell in Azure.

```bash
#!/bin/bash

az login --tenant $ARM_TENANT_ID # Set your tenant id as an environment variable
az account set --subscription $ARM_SUBSCRIPTION_ID # Set your subscription id as an environment variable

# Variables for resource groups and storage accounts
RG_WINE="lrn-wine-rg" # name of resource group in learning environment
RG_CHEESE="lrn-cheese-rg" # name of resource group in learning environment
STORAGE_WINE="lrndlkwine$(openssl rand -hex 5)" # Generating a unique name for wine data lake account
STORAGE_CHEESE="lrndlkcheese$(openssl rand -hex 5)" # Generating a unique name for cheese data lake account
LOCATION="northeurope" # azure region

# Create resource group for wine
echo "Creating resource group for wine..."
az group create --name $RG_WINE --location $LOCATION

# Create resource group for cheese
echo "Creating resource group for cheese..."
az group create --name $RG_CHEESE --location $LOCATION

# Create Azure Data Lake Storage Gen2 account in wine resource group with AllowBlobPublicAccess enabled
echo "Creating Data Lake Gen2 storage account for wine with public blob access..."
az storage account create \
  --name $STORAGE_WINE \
  --resource-group $RG_WINE \
  --location $LOCATION \
  --sku Standard_LRS \
  --kind StorageV2 \
  --hns true  # Enable hierarchical namespace for Data Lake Gen2

# Enable anonymous blob access for wine storage account
az storage account update \
  --name $STORAGE_WINE \
  --resource-group $RG_WINE \
  --allow-blob-public-access true  # Allow public access to blobs

# Create Azure Data Lake Storage Gen2 account in cheese resource group with AllowBlobPublicAccess enabled
echo "Creating Data Lake Gen2 storage account for cheese with public blob access..."
az storage account create \
  --name $STORAGE_CHEESE \
  --resource-group $RG_CHEESE \
  --location $LOCATION \
  --sku Standard_LRS \
  --kind StorageV2 \
  --hns true  # Enable hierarchical namespace for Data Lake Gen2

# Enable anonymous blob access for cheese storage account
az storage account update \
  --name $STORAGE_CHEESE \
  --resource-group $RG_CHEESE \
  --allow-blob-public-access true  # Allow public access to blobs

# Create container named 'lake' in the wine storage account with public access to blobs
echo "Creating 'lake' container in wine storage account with public access..."
WINE_KEY=$(az storage account keys list --resource-group $RG_WINE --account-name $STORAGE_WINE --query '[0].value' --output tsv)
az storage container create \
  --name lake \
  --account-name $STORAGE_WINE \
  --account-key $WINE_KEY \
  --public-access blob  # Allow public access to blobs

# Create container named 'lake' in the cheese storage account with public access to blobs
echo "Creating 'lake' container in cheese storage account with public access..."
CHEESE_KEY=$(az storage account keys list --resource-group $RG_CHEESE --account-name $STORAGE_CHEESE --query '[0].value' --output tsv)
az storage container create \
  --name lake \
  --account-name $STORAGE_CHEESE \
  --account-key $CHEESE_KEY \
  --public-access blob  # Allow public access to blobs

echo "Data Lake Gen2 storage accounts, containers, and public access have been configured successfully."
```

The reason I am storing the data in separate data lakes and resource groups is to simulate the idea of separated domains in a distributed reporting mesh. This allows for allocation of team responsibility, isolation and ease of cost identification. You would need to practice domain driven design to find the appropriate boundaries in your organisation, but for now cheese and wine as separate domains will demonstrate the concept.

You should see two resource groups in your azure portal.

![Azure Resource Group]({ site.baseurl }/assets/2024-09-30-distributed-reporting-mesh-with-duckdb-delta-and-streamlit/resourcegroups.PNG)

Each resource group containing their respective storage.

![Data Lake Storage]({ site.baseurl }/assets/2024-09-30-distributed-reporting-mesh-with-duckdb-delta-and-streamlit/datalake.PNG)

## Cheese and Wine Data

I recently discovered the website [kaggle](https://www.kaggle.com/) that has loads of open source datasets for data science and experimentation. After a quick search for cheese and wine I found the following datasets to satisfy my cravings:

- [Kaggle Datasets Cheese](https://www.kaggle.com/datasets/joebeachcapital/cheese){:target="\_blank"}
- [Kaggle Datasets Wine Dataset](https://www.kaggle.com/datasets/elvinrustam/wine-dataset){:target="\_blank"}

A quick review of the [license attributed to both](https://creativecommons.org/publicdomain/zero/1.0/){:target="\_blank"} made me realise these were good to go and experiment with!

Upload each csv file to the respective storage account in a "csv" directory using the Azure portal.

![Data Lake Storage Upload]({ site.baseurl }/assets/2024-09-30-distributed-reporting-mesh-with-duckdb-delta-and-streamlit/uploadcsv.PNG)

## Duckdb

```python
import duckdb
import pandas
from IPython.display import display

duckdb.sql(
    """SET azure_transport_option_type = 'curl'"""
)  ## important for when running in linux!

duckdb.sql("""SELECT 'Bring me cheese!'""").show()

df_cheese = duckdb.sql(
    """
SELECT *
FROM 'abfss://lrndlkcheese1e269a0387.dfs.core.windows.net/lake/csv/cheeses.csv'
"""
).df()

display(df_cheese.head(5))

display(list(df_cheese.columns))

df_wine = duckdb.sql(
    """
SELECT coalesce(Region,'(Unknown)') AS Region, count(*) AS Wines
FROM 'abfss://lrndlkcheese1e269a0387.dfs.core.windows.net/lake/csv/cheeses.csv'
GROUP BY ALL
ORDER BY 2 DESC
LIMIT 10
"""
).show()

duckdb.sql("""SELECT 'Bring me wine!'""").show()

df_wine = duckdb.sql(
    """
SELECT *
FROM 'abfss://lrndlkwinee4769a04a5.dfs.core.windows.net/lake/csv/WineDataset.csv'
"""
).df()

display(df_wine.head(5))

display(list(df_wine.columns))

df_wine = duckdb.sql(
    """
SELECT coalesce(Region,'(Unknown)') AS Region, count(*) AS Wines
FROM 'abfss://lrndlkwinee4769a04a5.dfs.core.windows.net/lake/csv/WineDataset.csv'
GROUP BY ALL
ORDER BY 2 DESC
LIMIT 10
"""
).show()
```

## Streamlit

## Delta Lake Mesh

## Distributed Reporting Mesh
