---
title: "Creating Schemas and Data from Beer Models"
date: 2022-11-27
author: dataGriff
description: This is how you can used pydantic models to create schemas from your data model such as JSON schemas and fake data generation
image:
  path: /assets/2022-11-27-fastapi-gen/link.png
tags: python fastapi pydantic
---

A quick post today showing how [Pydantic](https://pydantic-docs.helpmanual.io/) offers some great ways to create schemas from your data model. In this post I"ll show you how to create a JSON schema for you beers and generate some fake data!

- [PreRequisites](#prerequisites)
- [Setup your Codebase](#setup-your-codebase)
- [Setup your Python Environment](#setup-your-python-environment)
- [Setup your Model](#setup-your-model)
- [Generate Model Schema](#generate-model-schema)
- [Generate Model Code from Schema](#generate-model-code-from-schema)
- [Generate Data](#generate-data)

## PreRequisites

- You"ll need [python](https://www.python.org/downloads/) installed.
- You"ll need a decent IDE - I use [visual studio code](https://code.visualstudio.com/download).
- Ideally you should have [git](https://git-scm.com/downloads) installed.

## Setup your Codebase

In your favourite IDE setup a folder structure like the following.

```file
beerapi
│   README.md
│   requirements.txt
|   .gitignore
│
└───app
│   │   beer.py
│   │   generate.py
│   │   testdata.py
```

In the requirements.txt file add these three rows which will import the libraries we need to create our FastAPI.

```file
pydantic
datamodel-code-generator
jsf
```

In the .gitignore file ensure your virtual environment is ignored by adding the following line.

```file
venv/*
```

## Setup your Python Environment

When in your project folder root, create a new python virtual environment by running the following in a terminal:

```bash
python -m venv venv
```

Initalise the environment

```bash
venv\scripts\activate
```

Install the required python libraries from the requirements.txt file.

```bash
pip install -r requirements.txt
```

## Setup your Model

We"re going to setup another simple beer model like we did in the last few posts. The only extra piece that has been added is the "Config" class that allows you to add an example of the class in JSON format. This will then be added to your JSON schema that you output.

Copy and paste the below code into your beer.py file.

```py
from enum import Enum
from typing import List, Union
from pydantic import BaseModel, Field

class Flavour(str, Enum):
    """This is a flavour of a beer

    Args:
        str (_type_): This takes in a string for the flavour description
        Enum (_type_): This inherits from Enum data type for the flavour enum
    """
    HOPPY = "Hoppy"
    CHOCOLATE = "Chocolate"
    CARAMEL = "Caramel"
    ORANGE = "Orange"

class Beer(BaseModel):
    """This is a beer

    Args:
        BaseModel (_type_): This inherits from pydantic base model
    """
    name: str = Field(example="Mike Rayer"
                      ,description="This is the name of the beer")
    brewer: str = Field(example="Crafty Devil"
                        ,description="This is the name of the brewer of the beer")
    strength: float = Field(gt=0,lt=20,example=5.2
                            ,description="This is the strength of the alcohol in the beer")
    flavours: Union[List[Flavour], None] = Field(default=None
                                                 ,example=["Caramel"]
                                             ,description="""These are the lists of flavours in the beer""")
    class Config:
        """Pydantic config class to add extra components to schema
        """
        schema_extra = {
            "examples": [
                {
                    "name": "Elvis Juice",
                    "brewer": "Brewdog",
                    "strength": 5.1,
                    "flavours" : ["Orange","Hoppy"]
                }
            ]
        }
```

## Generate Model Schema

Now its time to generate a JSON schema from your wonderful beer model. In the generate.py file copy and paste the below:

```py
from beer import Beer
from pydantic import schema_json_of

schema = schema_json_of(Beer, title="The Beer schema" \
                        , indent=2)

with open("Beer.json", "w", encoding="utf-8") as f:
        f.write(str(schema))
```

Run this generate.py file in your IDE and you should generate a local Beer.json file which shows your beer model in a JSON schema format. It should look something like the below depending on all the metadata you have added.

```json
{
  "title": "The Beer schema",
  "$ref": "#/definitions/Beer",
  "definitions": {
    "Flavour": {
      "title": "Flavour",
      "description": "This is a flavour of a beer\n\n    Args:\n        str (_type_): This takes in a string for the flavour description\n        Enum (_type_): This inherits from Enum data type for the flavour enum\n    ",
      "enum": [
        "Hoppy",
        "Chocolate",
        "Caramel",
        "Orange"
      ],
      "type": "string"
    },
    "Beer": {
      "title": "Beer",
      "description": "This is a beer\n\nArgs:\n    BaseModel (_type_): This inherits from pydantic base model",
      "type": "object",
      "properties": {
        "name": {
          "title": "Name",
          "description": "This is the name of the beer",
          "example": "Mike Rayer",
          "type": "string"
        },
        "brewer": {
          "title": "Brewer",
          "description": "This is the name of the brewer of the beer",
          "example": "Crafty Devil",
          "type": "string"
        },
        "strength": {
          "title": "Strength",
          "description": "This is the strength of the alcohol in the beer",
          "exclusiveMinimum": 0,
          "exclusiveMaximum": 20,
          "example": 5.2,
          "type": "number"
        },
        "flavours": {
          "description": "These are the lists of flavours in the beer",
          "example": [
            "Caramel"
          ],
          "type": "array",
          "items": {
            "$ref": "#/definitions/Flavour"
          }
        }
      },
      "required": [
        "name",
        "brewer",
        "strength"
      ],
      "examples": [
        {
          "name": "Elvis Juice",
          "brewer": "Brewdog",
          "strength": 5.1,
          "flavours": [
            "Orange",
            "Hoppy"
          ]
        }
      ]
    }
  }
}
```

## Generate Model Code from Schema

Now... to show we can do this backwards while drink a can of sweet, sweet ale... We are now going to generate a pydantic model from a JSON schema using [data model code generator](https://pypi.org/project/datamodel-code-generator/0.2.1/). This can be particularly useful to create code if the first thing we are given is a JSON schema.

To do this run the following in the command-line of your IDE:

```bash
datamodel-codegen  --input Beer.json --input-file-type jsonschema --output model.py
```

This will generate the model.py code you need in python as a great quick-start to coding! Just what us hungovercoders need, shortcuts. The float property needs slight tweak so that it looks like the following, but it sure saves a lot of work.

```py
...
    strength: float  = Field(
        ...,
        lt=20.0, gt=0.0,
        description="This is the strength of the alcohol in the beer",
        example=5.2,
        title="Strength",
    )
...
```

## Generate Data

You can also generate data from your model schema using [jsf](https://pypi.org/project/jsf/). This is built on top of [faker](https://pypi.org/project/Faker/), another great tool from python to generate fake data for testing. The below code takes the beer schema and restrictions put in place by the pydantic model to generate fake data for 5 seconds. This could be a great way to load test something quickly and ensure all is working well... Without us having to generate that data ourselves!

```py
from beer import Beer
from jsf import JSF
import time
import json

schema = Beer.schema()
faker = JSF(schema)

start_time = time.time()
seconds = 5

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    fake_json = faker.generate()
    print(json.dumps(fake_json))
    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break
```

The output should be something like...

```json
{"name": "dolor nobis elit. officiis sit esse amet", "brewer": "magnam,", "strength": 2.0, "flavours": []}
{"name": "molestias, Hic", "brewer": "modi Hic elit. reiciendis esse nobis", "strength": 12.0}
{"name": "modi", "brewer": "accusantium quas Lorem culpa! odit exercitationem", "strength": 2.0, "flavours": ["Caramel"]}    
{"name": "architecto sit elit. placeat modi quas reiciendis", "brewer": "repellendus consectetur magnam, possimus ipsum", "strength": 18.0, "flavours": ["Orange", "Caramel", "Orange", "Caramel", "Caramel"]}
{"name": "elit. sit modi reprehenderit illum elit. illum", "brewer": "placeat culpa! nobis esse possimus elit. ipsum", "strength": 14.0, "flavours": ["Chocolate", "Hoppy", "Orange"]}
```

Looks like someone was drunk putting those names in.
