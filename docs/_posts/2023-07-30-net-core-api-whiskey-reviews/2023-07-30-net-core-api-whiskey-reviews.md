---
title: ".Net Core 7 API backed with Cosmos SQL | Create a Whiskey Review API with .Net Core 7"
date: 2023-07-30
author: dataGriff
description: Create a simple API with .Net Core 7 backed with a NoSQL database
image:
  path: /assets/2023-07-03-net-core-api-whiskey-reviews/link.png
tags: Azure API Cosmos .Net
---

Well I'm definitely a hungovercoder today and its been quite difficult to stare at lists of distilleries without wanting a bit of hair of the dog... Anyway this POST (see what I did there?) will walkthrough how to create a simple API using .Net Core backed with an Azure Cosmos SQL database. I am not a .Net ninja, nor am I an API aficionado (yet!), but the following will create you a basic and currently very insecure API. I hope to investigate APIs further in .Net and follow-up with better practice approaches in the future.

- [Pre-Requisites](#pre-requisites)
- [Plan the API](#plan-the-api)
- [Codebase Overview](#codebase-overview)
- [Create the API Starter Template](#create-the-api-starter-template)
- [Install Packages](#install-packages)
- [Create the Distillery Model](#create-the-distillery-model)
- [Add Distillery Data](#add-distillery-data)
- [Create the Whiskey Controller](#create-the-whiskey-controller)
- [Test our API](#test-our-api)
- [Get our Swagger On](#get-our-swagger-on)
- [Create the Whiskey Review Model](#create-the-whiskey-review-model)
- [Deploy Cosmos SQL API](#deploy-cosmos-sql-api)
- [Create the Data Interface](#create-the-data-interface)
- [Add Whiskey Review Endpoints to our Controller](#add-whiskey-review-endpoints-to-our-controller)
- [Test the API](#test-the-api)

## Pre-Requisites

* [Visual Studio Code](https://code.visualstudio.com/)
* [.Net Framework](https://dotnet.microsoft.com/en-us/download/dotnet-framework)
* [Azure Subscription](https:://portal.azure.com)
* [Cosmos DB Emulator](https://learn.microsoft.com/en-us/azure/cosmos-db/local-emulator) (optional - but handy for local dev)

## Plan the API

The API is going to allow us to create, view and amend whiskey reviews as a user. We therefore need to think about our endpoints in relation to this behaviour and expected user interaction. We also don't want to create any verbs in our URI paths as we will leave that to the HTTP verbs to handle for us. The first endpoint is going to be simple GET of a list of distilleries that we can use to validate some inputs. The second is then how we can POST a new whiskey review. The rest of the calls are how a user can then interact with their own whiskeys and reviews.

| Behaviour  | HTTP Verb  | URI |
|---|---|---|
|  Get distilleries |  GET |  https://api.myurl/distilleries |
|  Whiskey review created |  POST |  https://api.myurl/whiskeys/reviews |
|  User gets whiskey reviews |  GET |  https://api.myurl/users/{userId}/whiskeys |
|  User gets a whiskey review |  GET |  https://api.myurl/users/{userId}/whiskeys/{whiskeyId} |
|  User deletes a whiskey review |  DELETE |  https://api.myurl/users/{userId}/whiskeys/{whiskeyId} |
|  User updates whiskey review |  PUT | https://api.myurl/users/{userId}/whiskeys/{whiskeyId} |

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
|   |   |   Distillery.cs
|   |   |   TransactionResult.cs
│   └───Data
|   |   |   CosmosSQLDatabase.cs
|   |   |   IDatabaseAdapter.cs
│   └───DataSource
|   |   |   CosmosSQLDatabase.c
|   |   |   IDatabaseAdapter.cs
│   └───Controllers
|   |   |   WhiskeyReviewController.cs
```

The api folder will contain the resources for the api. The Models folder will contain our object that represents the whiskey reviews we'll be creating. The Data folder will have the IDatabaseAdapter interface that both the Cosmos and Mongo files need to inherit from. This interface is what is going to allow us to swap out the database back end without impacting the functionality of the application. The Controller folder will then contain all the endpoints that the api will expose and how each API verb behaves when it is interacted with. This will interact with the current database via the IDatabaseAdapter which is declared in the Program.cs file. It is the Program.cs file that launches the program and contains the configuration and settings of the API.

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
dotnet add package Microsoft.Extensions.Caching.Memory
```

The cosmos package will allow us to interact with Azure Cosmos DB as our NoSQL database store. The OpenAPI and Swashbuckle packages will allow us to document our API with swagger.The Newtonsoft.Json package will allow us to use JsonProperty in our Model class so that when we serialize and deserialize our whiskey reviews from JSON it all works successfully. The caching memory package will allow us to cache some reusable lists for our distilleries.

## Create the Distillery Model

The first model we are going to create is for our distillery lookup. Under the api/Models folder, create a file called Distillery.cs. Add the following code which will represent our distilleries.

```csharp
using System.Text.Json.Serialization;
using System.ComponentModel.DataAnnotations;

namespace api.Models
{
    public class Distillery
    {
        [JsonPropertyName("id")]
        public string Id { get; set; }

        [JsonPropertyName("name")]
        public string Name { get; set; } 

        [JsonPropertyName("wikiLink")]
        public string? WikiLink { get; set; }

        [JsonPropertyName("country")]
        public string? Country { get; set; }

        [JsonPropertyName("type")]
        public string? Type { get; set; }
    }
}
```

This class setups up a distillery object to have five properties. The JsonPropertyName is leveraging the System.Text.Json.Serialization and not Newtonsoft (more on that later) which states what the name of the properties will be when serializing and deserializing. You'll notice this in the next section where our distillery JSON data matches the casing in the JsonPropertyName. 

## Add Distillery Data

Create a distilleries.json file under a api/DataSource directory. This is going to contain lookup data for our distilleries and it is going to be read only. In the file add the following data:

```json
[
    {
        "id": "glenmorangie",
        "name": "Glenmorangie",
        "wikiLink": "/wiki/Glenmorangie_distillery",
        "country": "Scotland",
        "type": "Single Malt"
    },
        {
        "id": "clontarf1014",
        "name": "Clontarf 1014",
        "wikiLink": "/wiki/Clontarf_(whiskey)",
        "country": "Ireland",
        "type": "Blended"
    },
    {
        "id": "hakushu",
        "name": "Hakushu",
        "wikiLink": "/wiki/Hakushu_distillery",
        "country": "Japan",
        "type": "Single grain Irishs"
    }
]
```

If you want to get a big list of distilleries you can use [this]() in the original repo which I have taken by scraping the [wikipedia list of whiskey brands](https://en.wikipedia.org/wiki/List_of_whisky_brands) page.

## Create the Whiskey Controller

Create a file called WhiskeyReviewController.cs under the Controllers directory. This is going to hold our endpoints for interacting with the API. Add the following code to the file which will add a single GET endpoint to retrieve our distilleries. The method utilises local caching so once the distilleries have been looked up from storage subsequent calls get the data from the cache. The comments above the GetDistilleries method form part of our Swagger documentation which we will see in the next section where we test the API. The URL of the API will be the base domain plus api/v1, which is declared at the APIController route. The v1 style path is to allow versioning. The route for the distilleries GET request will be at "distilleries" as declared by the route property above the method, so the path for this request will be api/v1/distilleries.

```csharp
using System.Net;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using api.Models;
using Swashbuckle.AspNetCore.Annotations;
using System;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using Microsoft.Extensions.Caching.Memory;

namespace api.Controllers
{
    [Route("api/v1")] //this is the base route
    [ApiController]
    public class WhiskeyReviewController : ControllerBase
    {
        private readonly IMemoryCache _cache;

        public WhiskeyReviewController(IMemoryCache cache)
        {
            _cache = cache;
        }

        /// <summary>
        /// Gets list of distilleries
        /// </summary>
        /// <remarks>
        /// Sample request:
        /// 
        ///     GET api/v1/distilleries
        /// </remarks>
        /// <response code="200">Successfully returned distillers</response>
        /// <returns>Distilleries</returns>
        [Route("distilleries")]
        [HttpGet]
        public async Task<List<Distillery>> GetDistilleries()
        {
            const string cacheKey = "distilleries";
            if (!_cache.TryGetValue(cacheKey, out List<Distillery> _distilleries))
            {
                Console.WriteLine("Retrieving data from storage...");
                string jsonString = await System.IO.File.ReadAllTextAsync("Datasource\\distilleries.json");
                _distilleries = JsonSerializer.Deserialize<List<Distillery>>(jsonString);

                _cache.Set(cacheKey, _distilleries, new MemoryCacheEntryOptions
                {
                    AbsoluteExpirationRelativeToNow = TimeSpan.FromDays(365)
                });
            }
            else
            {
                Console.WriteLine("Retrieving data from cache...");
            }
            return _distilleries;
        }
    }
}
```

In order to leverage the caching you will need to add this to the services when the app is built in the Program.cs file. Add the following line above the AddControllers() method call in the Program.cs file to ensure the memory cache service is available.

```csharp
//Ensuring cache is available for lookup
builder.Services.AddMemoryCache();
// Add services to the container.
builder.Services.AddControllers();
```

## Test our API

In the terminal open up your api directory and run dotnet build to make sure everything is building correctly. Then run dotnet run which should start up your API. Navigate to the URL we have stated and go to the swagger docs at [https://localhost:3001/swagger/index.html)](https://localhost:3001/swagger/index.html).

You should see the swagger as below.

If you execute the GET the request you will see the list of distilleries returned.

You'll also notice if you perform repeat GET requests against the API, only the first will write "retrieving from storage" and the rest will write "retrieving from cache" as we are caching this lookup data in the app.

## Get our Swagger On

You'll notice that none of the documentation we added to our API is currently present in the Swagger. To add this, add thw following using statement in the Program.cs file.

```csharp
using System.Reflection;
```

Then replace the AddSwagger code with this so that when the services are being built they will leverage the documentation we have provided for the API.

```csharp
builder.Services.AddSwaggerGen(options =>
{
    options.EnableAnnotations();

    var xmlFilename = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    options.IncludeXmlComments(Path.Combine(AppContext.BaseDirectory, xmlFilename));
});
```

You'll also need to edit the project file XML by adding the GenerateDocumentationFile property group and setting it to true.

```xml
  <PropertyGroup>
    <TargetFramework>net7.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
    <GenerateDocumentationFile>true</GenerateDocumentationFile>
  </PropertyGroup>
```

Now when we go back to the API we should see some basic documentation based on the comments above our code in the controller class.



## Create the Whiskey Review Model

In your api directory create a Models folder and a Distillery.cs file. This will contain the properties that will model our whiskey review entity in the real world.

In the WhiskeyReview file paste the following code:

```csharp
using Newtonsoft.Json;
using System.ComponentModel.DataAnnotations;

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
            Date = DateTime.Now;
        }

        [JsonProperty("id")]
        public string Id { get { return WhiskeyID   + "-" + UserId.ToLower(); } }

        [JsonProperty("userId")]
        public string UserId { get; set; }

        [JsonProperty("date")]
        private DateTime Date { get; set; }

        [JsonProperty("whiskeyId")]
        public string WhiskeyID
        {
            get
            {
                return new string(WhiskeyName.Where(c => Char.IsLetterOrDigit(c)).ToArray()).ToLower();
            }
        }

        [Required]
        [JsonProperty("whiskeyName")]
        public string WhiskeyName { get; set; }

        [Required]
        [JsonProperty("distilleryName")]
        public string? DistilleryName { get; set; }

        [Required]
        [Range(1, 5)]
        [JsonProperty("rating")]
        public int? Rating { get; set; }

        [JsonProperty("notes")]
        public Note[]? Notes { get; set; }

        [StringLength(100, MinimumLength = 1, ErrorMessage = "Must be at least 1 characters long and less than 100 characters.")]
        [JsonProperty("review")]
        public string? Review { get; set; }

        [JsonProperty("location")]
        public string? Location { get; set; }
    }
}
```

The code creates a list of enums that are allowed for the notes property. This is an array where users can add multiple notes they taste in the whiskey. There is then validation on the rating to ensure this is only between 1 and 5. There is also validation on the review to ensure this is no more than 500 words. The Date property is private and will just set the Date to be now whenever an instance of a whiskey review is created. The Whiskey ID is generated by removing spaces and special characters from the Whiskey Name. This is then concatenated with the user to make a unique id for each review.

## Deploy Cosmos SQL API

We need to create a serverless Cosmos SQL API instance in Azure to back our API. You can use the cosmos local emulator if you wish but for this demo I have used an Azure instance. To deploy a serverless instance of Cosmos you can use the use the following CLI command and either run it from a local terminal or in the cloud shell.

```bash

```

Once you the instance has created, copy the key and endpoint:

And set them as environment variables on your machine:

This means we can now easily reference these in our code without worrying about checking in connection strings.

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

## Add Whiskey Review Endpoints to our Controller

## Test the API




