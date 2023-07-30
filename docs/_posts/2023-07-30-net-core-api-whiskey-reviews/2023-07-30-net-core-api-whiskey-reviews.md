---
title: ".Net Core 7 API backed with Cosmos or Mongo | Create a Whiskey Review API with .Net Core 7"
date: 2023-07-30
author: dataGriff
description: Create a simple API with .Net Core 7 backed with a NoSQL database
image:
  path: /assets/2023-07-03-net-core-api-whiskey-reviews/link.png
tags: Azure API Cosmos Mongo .Net
---

- [Pre-Requisites](#pre-requisites)
- [Plan the API](#plan-the-api)
- [Codebase Overview](#codebase-overview)
- [Deploy Resources](#deploy-resources)
- [Create the API Starter Template](#create-the-api-starter-template)
- [Install Packages](#install-packages)
- [Create the Model](#create-the-model)
- [Create the Data Interface](#create-the-data-interface)
- [Create the Controller](#create-the-controller)
- [Test the API with Swagger](#test-the-api-with-swagger)
- [Basic Front End](#basic-front-end)

## Pre-Requisites

## Plan the API

The API is going to allow us to create, view and amend whiskey reviews as a user. We therefore need to think about our endpoints in relation to this behaviour and expected user interaction. We also don't want to create any verbs in our URI paths as we will leave that to the HTTP verbs to handle for us. We also want to show that the API is interacting with the whiskeyreviews and so we'll represent this entity as plural in the rest calls.

| Behaviour  | HTTP Verb  | URI |
|---|---|---|
|  User creates a whiskey review |  POST |  https://api.myurl/users/{userid}/whiskeyreviews |
|  User gets whiskey reviews |  GET |  https://api.myurl/users/{userid}/whiskeyreviews |
|  User gets specific whiskey review |  GET |  https://api.myurl/users/{userid}/whiskeyreviews/{whiskey} |
|  User deletes a whiskey review |  DELETE |  https://api.myurl/users/{userid}/whiskeyreviews/{whiskey} |

## Codebase Overview

The codebase we end up with is going to look something like the following. We will autogenerate this with some quick start terminal commands but I always think its good to have the destination in mind to understand what we're building.

```file
whiskey.reviews
│   README.md
|   .gitignore    
└───api
│   │   Program.cs
│   │   api.csproj
│   │   appsettings.json
│   │   appsettings.Development.json
│   └───Models
|   |   |   WhiskeyReview.cs
│   └───Data
|   |   |   CosmosSQLDatabase.cs
|   |   |   IDatabaseAdapter.cs
|   |   |   MongoDBDatabase.cs
│   └───Controllers
|   |   |   WhiskeyReviewController.cs
└───web
│   │   WhiskeyReviews.html
```

The api folder will contain the resources for the api. The Models folder will contain our object that represents the whiskey reviews we'll be creating. The Data folder will have the IDatabaseAdapter interface that both the Cosmos and Mongo files need to inherit from. This interface is what is going to allow us to swap out the database back end without impacting the functionality of the application. The Controller folder will then contain all the endpoints that the api will expose and how each API verb behaves when it is interacted with. This will interact with the current database via the IDatabaseAdapter which is declared in the Program.cs file. It is the Program.cs file that launches the program and contains the configuration and settings of the API we're main. 

## Deploy Resources

Setup your environment variables so that the code in the following post will work for you correctly.

## Create the API Starter Template

In your IDE run the following commands in a terminal to setup your new API and then change directory to start working within it.

```bash
dotnet new webapi -n api
cd api
```

Once you have run the above you should see the basic skeleton of the API setup in your directory as per below.

![API Skeleton]({{ site.baseurl }}/assets/2023-07-30-net-core-api-whiskey-reviews/api-skeleton.png)

To make sure that this all runs correctly on your local machine, copy and paste the following into the Properties/launchSettings.json file. This will ensure the ports 3000 and 3001 are used for http and https respectively.

```json
{
  "$schema": "https://json.schemastore.org/launchsettings.json",
  "iisSettings": {
    "windowsAuthentication": false,
    "anonymousAuthentication": true,
    "iisExpress": {
      "applicationUrl": "https://localhost:3001",
      "sslPort": 3001
    }
  },
  "profiles": {
    "http": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
      "applicationUrl": "http://localhost:3000",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "https": {
      "commandName": "Project",
      "dotnetRunMessages": true,
      "launchBrowser": true,
      "launchUrl": "swagger",
      "applicationUrl": "https://localhost:3001;http://localhost:3000",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    },
    "IIS Express": {
      "commandName": "IISExpress",
      "launchBrowser": true,
      "launchUrl": "swagger",
      "environmentVariables": {
        "ASPNETCORE_ENVIRONMENT": "Development"
      }
    }
  }
}
```

Then in the Program.cs file add this line before the app is built to ensure the URLs in the launch settings are reflected.

```csharp
builder.WebHost.UseUrls("http://localhost:3000", "https://localhost:3001");

var app = builder.Build();
```

Run the following to make sure that it builds correctly:

```bash
dotnet build
```

Then run the following to run the API

```bash
dotnet run
```

You can test it is then working by going to the following address [https://localhost:3001/swagger/index.html](https://localhost:3001/swagger/index.html) and you should see the swagger for the example weather API as per below.

![Weather Swagger]({{ site.baseurl }}/assets/2023-07-30-net-core-api-whiskey-reviews/weather-swagger.png)

Once you have completed this test (and had a play around if you want), remove the WeatherForecast.cs file and the Controllers/WeatherForecastController.cs file. We will be replacing all this with our whiskey review models!

## Install Packages

We're going to need some packages for our API to work so lets install them all now. Run the following in a terminal in your api directory.

```bash
dotnet add package Microsoft.Azure.Cosmos
dotnet add package Microsoft.OpenAPI
dotnet add package Swashbuckle.AspNetCore.Annotations
dotnet add package Newtonsoft.Json
dotnet add package Microsoft.AspNetCore.Mvc.NewtonsoftJson
```

The cosmos package will allow us to interact with Azure Cosmos DB as our NoSQL database store. The OpenAPI and Swashbuckle packages will allow us to document our API with swagger.The Newtonsoft.Json package will allow us to use JsonProperty in our Model class so that when we serialize and deserialize our whiskey reviews from JSON it all works successfully.

## Create the Model

In your api directory create a Models folder and a WhiskeyReview.cs file. This will contain the properties that will model our whiskey review entity in the real world.

In the WhiskeyReview file paste the following code:

```csharp
using System.Text.Json.Serialization;
using Newtonsoft.Json;

namespace api.Models
{

    public enum Note
    {
        Vanilla,
        Honey,
        Caramel,
        Nutmeg
    }

    public class WhiskeyReview
    {
        public WhiskeyReview()
        {
            id = Whiskey;
            date = DateTime.Now;
        }

        [JsonProperty("id")]
        public string Id { get; }

        [JsonProperty("date")]
        public string Date { get; }

        [JsonProperty("userId")]
        public string UserID { get; set; }

        [JsonProperty("whiskey")]
        public string Whiskey { get; set; }

        [JsonProperty("rating")]
        public int Rating
        {
            get { return rating; }
            set 
            { 
                if(value < 1 || value > 5)
                    throw new ArgumentException("Rating must be between 1 and 5.");
                else
                    rating = value;
            }
        }

        [JsonProperty("notes")]
        public Note[] Notes { get; set; }

        public string Review
        {
            get { return review; }
            set
            {
                if (value != null && value.Length > 500)
                    throw new ArgumentException("Review must be less than 500 characters.");
                else
                    review = value;
            }
        }
    }
}
```

The code creates a list of enums that are allowed for the notes property. This is an array where users can add multiple notes they taste in the whiskey. There is then validation on the rating to ensure this is only between 1 and 5. There is also validation on the review to ensure this is no more than 500 words.

## Create the Data Interface

First we are going to create an IDatabaseAdapter.cs file. This interface will allow us to make a database agnostic interface to interact with whatever database technology we are currently using. It should mean we can easily swap out the database technology we use in the next file without disrupting the model and controllers.

Create a Data folder and in here create an IDatabaseAdapter.cs file. Paste the following code into this file.

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;
using api.Models;

namespace api.Data
{
    public interface IDatabaseAdapter
    {

        Task<bool> CreateWhiskeyReview(string userId);

        Task<List<WhiskeyReview>> GetUserReviews(string userId);

        Task<WhiskeyReview> GetUserReview(string userId, string whiskey);

        Task<bool> DeleteReview(string userId, string whiskey) ;
    }
}
```

This allows us to interface with a database and meets the behavioural requirements we set out in our API design at the start.

Now create another file in the data folder called CosmosSQLDatabase.cs. This class will now need to implement the above methods as it will inherit from this to ensure consistency for the future. In this file copy and paste the code below:

```csharp
using api.Models;
using Microsoft.Azure.Cosmos;

namespace api.Data
{
    public class CosmosSQLDatabase : IDatabaseAdapter
    {
        public CosmosClient _cosmosClient;
        private Database _database;
        private Container _container;

        public CosmosSQLDatabase()
        {
            string endpoint = Environment.GetEnvironmentVariable("COSMOS_ENDPOINT");
            string key = Environment.GetEnvironmentVariable("COSMOS_KEY");

            // Initialize CosmosClient
            _cosmosClient = new CosmosClient(endpoint, key);

            // Call the async initialization method.
            InitializeAsync().GetAwaiter().GetResult();
        }

        private async Task InitializeAsync()
        {
            _database = await _cosmosClient.CreateDatabaseIfNotExistsAsync("whiskey");
            _container = await _database.CreateContainerIfNotExistsAsync("reviews", "/userId");
        }

        public async Task<List<WhiskeyReview>> GetUserReviews(string userId)
        {
            var query = new QueryDefinition("SELECT * FROM c WHERE c.userId = @userId")
                .WithParameter("@userId", userId);
            FeedIterator<WhiskeyReview> resultSet = _container.GetItemQueryIterator<WhiskeyReview>(query);

            List<WhiskeyReview> results = new List<WhiskeyReview>();
            
            while (resultSet.HasMoreResults)
            {
                FeedResponse<FlightPlan> response = await resultSet.ReadNextAsync();
                results.AddRange(response.ToList());
            }

            return results;
        }

        public async Task<WhiskeyReview> GetUserReview(string userId, string whiskey)
        {
            try
            {

                ItemResponse<WhiskeyReview> response = await _container.ReadItemAsync<WhiskeyReview>(whiskey, new PartitionKey(userId));
                return response.Resource;
            }
            catch (CosmosException ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
            {
                return null;
            }
        }

        public async Task<bool> CreateWhiskeyReview(WhiskeyReview whiskeyReview)
        {
            try
            {
                ItemResponse<WhiskeyReview> response = await _container.CreateItemAsync<WhiskeyReview>(whiskeyReview);

                return TransactionResult.Success;
            }
            catch (Exception)
            {
                return false;
            }
        }

        public async Task<bool> DeleteReview(string userId, string whiskey)
        {
            try
            {
                ItemResponse<WhiskeyReview> response = await _container.DeleteItemAsync<WhiskeyReview>(whiskey, new PartitionKey(userId));
                return true;
            }
            catch (CosmosException ex) when (ex.StatusCode == System.Net.HttpStatusCode.NotFound)
            {
                return false;
            }
        }

    }
}

```

## Create the Controller

## Test the API with Swagger

## Basic Front End




