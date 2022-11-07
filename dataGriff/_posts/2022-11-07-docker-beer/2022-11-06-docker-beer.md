---
title: "Sitting on the docker the beer"
date: 2022-11-06

author: dataGriff
---

In the previous post we created a [Beer API using Fast API in python](https://www.hungovercoders.com/blog/datagriff/2022/11/06/fast-api.html). Now fellow hungovercoders we want to pour this into a docker container and publish in an azure container app, sharing our beer-fuelled goodness with the world!!!

- [PreRequisites](#prerequisites)
- [Setup your Codebase](#setup-your-codebase)
- [Setup the FastAPI Code](#setup-the-fastapi-code)
- [Setup the Docker File](#setup-the-docker-file)
- [Create an Azure Container Registry](#create-an-azure-container-registry)
- [Deploy your Container to an Azure Webapp for Containers](#deploy-your-container-to-an-azure-webapp-for-containers)

## PreRequisites

- You'll need [python](https://www.python.org/downloads/) installed.
- You'll need a decent IDE - I use [visual studio code](https://code.visualstudio.com/download).
- Ideally you should have [git](https://git-scm.com/downloads) installed.
- You'll need to install [docker](https://docs.docker.com/get-docker/). I highly recommend going through the docker tutorial once you have it installed, its very cool.

## Setup your Codebase

In your favourite IDE setup a folder structure like the following.

```file
beerapi
│   README.md
│   requirements.txt
|   .gitignore
|   Dockerfile    
│
└───app
│   │   main.py
│   │   __init__.py
```

In the requirements.txt file add these three rows which will import the libraries we need to create our FastAPI.

```file
fastapi
pydantic
uvicorn
```

## Setup the FastAPI Code

We're going to use exactly the same beer API shown in the previous blog for our new docker hosted API. It gives just enough functionality to test with and is full of beer! Copy and paste the following code into your main.py file. For this exercise, we're going to leave the __init__.py file empty.

```py
from fastapi import FastAPI, status, Response, Body
from pydantic import BaseModel, Field
from typing import Union, List
from enum import Enum

class Flavour(str, Enum):
    """This is a flavour of a beer

    Args:
        str (_type_): _description_
        Enum (_type_): _description_
    """
    HOPPY = "Hoppy"
    CHOCOLATE = "Chocolate"
    CARAMEL = "Caramel"
    ORANGE = "Orange"

class Beer(BaseModel):
    """This is a beer

    Args:
        BaseModel (_type_): _description_
    """
    name: str = Field(example="Mike Rayer"
                      ,description="This is the name of the beer")
    brewer: str = Field(example="Crafty Devil"
                        ,description="This is the name of the brewer of the beer")
    strength: float = Field(gt=0,lt=100,example=5.2
                            ,description="This is the strength of the alcohol in the beer")
    flavours: Union[List[Flavour], None] = Field(default=None
                                                 ,example=["Caramel"]
                                                 ,description="These are the lists \
                                                 of flavours in the beer")

beer_list = []
beer = Beer(name="Mike Rayer",brewer="Crafty Devil",strength=4.6)
beer_list.append(beer)
beer = Beer(name="Stay Puft",brewer="Tiny Rebel",strength=4.8)
beer_list.append(beer)

app = FastAPI()

@app.get("/")
async def root():
    """Welcomes you to the beer API

    Returns:
        string: Welcome message
    """
    return "Welcome to the beer API!"

@app.get("/beers/")
async def get_beers(response: Response):
    """Returns all available beers

    Returns:
        list[Beer]: Returns a list of beer objects
    """
    response.status_code=status.HTTP_200_OK
    return beer_list
@app.post("/beers/")
async def create_beer(response: Response, beer: Beer= Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Elvis Juice",
                    "brewer": "Brewdog",
                    "strength": 4.6
                },
            },
             "beerTooStrong": {
                "summary": "Too strong beer fails",
                "description": "This is a beer with a strength above 100%.",
                "value": {
                    "name": "Elvis Juice",
                    "brewer": "Brewdog",
                    "strength": 101.0
                },
            },
            "beerTooWeak": {
                "summary": "Too weak beer fails",
                "description": "This is a beer with a strength below 0%.",
                "value": {
                    "name": "Elvis Juice",
                    "brewer": "Brewdog",
                    "strength": -1.0
                },
            },
            "invalidMissingStrength": {
                "summary": "Beers without a strength are rejected",
                "description": "Beers without a strength are rejected",
                "value": {
                    "name": "Mike Rayer",
                    "brewer": "Crafty Devil"
                },
            },
            "beerGoodFlavour": {
                "summary": "Good flavour addition",
                "description": "This is a beer with an allowable list of flavours",
                "value": {
                    "name": "Old Abbot",
                    "brewer": "Hogwarts",
                    "strength": 5.0,
                    "flavours": ["Orange","Caramel"],
                },
            },
            "beerBadFlavour": {
                "summary": "Good flavour addition",
                "description": "This is a beer with an allowable list of flavours",
                "value": {
                    "name": "Hobgoblin",
                    "brewer": "Wychwood",
                    "strength": 4.3,
                    "flavours": ["Orange","Toothpaste"],
                },
            }
        },
    )):
    """Creates a new beer

    Args:
        beer (Beer): A beer object with the properties specified in the schemas.

    Returns:
        string: Description of whether beer is added.
    """
    if beer not in beer_list:
        beer_list.append(beer) 
        content = f'Beer "{beer.name}" Added.'
        response.status_code=status.HTTP_201_CREATED
        return content

```

## Setup the Docker File

The FastAPI documentation strikes again and teaches you quite easily how to utilise it with [docker](https://fastapi.tiangolo.com/deployment/docker/).

In the Dockerfile in your directory add the following code:

```bash
FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
```

This starts from a base python image, sets a working directory, copies over the required libraries in the requirements.txt file, installs the libraries, copies the app code and then finally runs the app on port 80. The order of the docker file is important and the pip install step will be cached if nothing has changed in the requirements file. This will make your build of the image much faster than if you did the copy app code across first, as the app code is likely to change more and so break what you could potentially cache in a layered order.

Open your terminal in Visual Studio code in the directory that contains the Dockerfile and the app folder, then run the following:

```bash
docker build -t imagebeerapi .
```

To run the image run the following in the terminal in the same directory:

```bash
docker run -d --name containerbeerapi -p 80:80 imagebeerapi
```

In docker desktop you should now see a new container running called "beerapi". If you now go to [http://localhost/beers](http://localhost/beers) you will get the beers in your beerapi. If you go to [http://localhost/docs](http://localhost/docs) you get to see all the lovely swagger we have come to know and love from FastAPI, just all running in a container! You'll also note you didn't have to create a virtual environment for your python code when using the docker container, as all the dependencies and environment is handled within your container!

## Create an Azure Container Registry

## Deploy your Container to an Azure Webapp for Containers