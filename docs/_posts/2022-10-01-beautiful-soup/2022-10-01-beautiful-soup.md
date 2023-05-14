---
title: "Web Scraping for Beer with Python Beautiful Soup"
date: 2022-10-02
author: dataGriff
description: Covering how to use beautifulsoup python library to scrape websites for information and parse it into something useful
image:
  path: /assets/2022-10-01-beautiful-soup/link.png
tags: python beautiful-soup web-scraping
---

So we've previously looked at creating [beer in a flask api](https://www.hungovercoders.com/blog/datagriff/2022/09/25/flask-api.html), now I want to guzzle some beer from the web using the python package [beautiful soup](https://pypi.org/project/beautifulsoup4/) to scrape beer information!

- [PreRequisites](#prerequisites)
- [Setup your Codebase](#setup-your-codebase)
- [Setup your Python Environment](#setup-your-python-environment)
- [Create your Test Web Page](#create-your-test-web-page)
- [Guzzle your First Beers](#guzzle-your-first-beers)
- [Configure your Guzzling](#configure-your-guzzling)
- [Complete Code](#complete-code)

## PreRequisites

- You'll need [python](https://www.python.org/downloads/) installed.
- You'll need a decent IDE - I use [visual studio code](https://code.visualstudio.com/download).
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
│   │   app.py
└───test
    │
    └───pages
        |   test01.html
```

In the requirements.txt file add this row which will import the libraries we need to create our beer guzzler to scrape web information.

```file
bs4
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

Lets start guzzling beer!

## Create your Test Web Page

In the test/pages/html01.html, add the following html code to create a very basic webpage.

```html
<!DOCTYPE html>
<html>
<body>

<div class="beers">
    <div class="beer">
        <p id="name">Mike Rayer</p>
        <p id="brewer">Crafty Devil</p>
        <p id="strength">4.2%</p>
    </div>
    <div class="beer">
        <p id="name">Elvis Juice</p>
        <p id="brewer">Brew Dog</p>
        <p id="strength">5.2%</p>
    </div>
</div>

</body>
</html>
```

This webpage has a div that contains all beers and luckily this div is identifier by a class named "beers". There are then inner div elements that very luckily have each beer identified by a class called "beer". I mean what are the odds...
Finally within each beer there are some nicely setup pieces of text with an id for each of the properties we want to scrape and guzzle into our beer machine.
No the real world won't always be as forgiving as this with regards to web pages, but its a good start for us to practice some beautiful soup.

## Guzzle your First Beers

In the app/app.py file enter the following code:

```py
from bs4 import BeautifulSoup

def guzzle_beer():

    with open("test/pages/test01.html") as page:
        soup = BeautifulSoup(page,"html.parser")
        contents = soup.find("div", class_="beers")
        beers = contents.find_all("div", {"class": "beer"})
        print(beers)

if __name__ == '__main__':
    guzzle_beer()
```

To start with this imports our beautiful soup library that we have already installed from our requirements into our python virtual environments. Then it creates a function that parses our test webpage using beautiful soup and pulls out the contents that match for div with a class of "beers". Every "beer" is then listed in our beers div list. The main program then runs which calls our new beer guzzling function.

Run the above by calling your application in the python environment.

```bash
app\app.py
```

You should end up with something that looks like this, which is an array of the beer div elements.

```html
[<div class="beer">
<p id="name">Mike Rayer</p>
<p id="brewer">Crafty Devil</p>
<p id="strength">4.2%</p>
</div>, <div class="beer">
<p id="name">Elvis Juice</p>
<p id="brewer">Brew Dog</p>
<p id="strength">5.2%</p>
</div>]
```

Now replace your beer function with the following in the app.py file:

```py
def guzzle_beer():

    with open("test/pages/test01.html") as page:
        soup = BeautifulSoup(page,"html.parser")
        contents = soup.find("div", class_="beers")
        beers = contents.find_all("div", {"class": "beer"})
        beer_list = []
        for beer in beers:
            name = beer.find("p", {"id": "name"}).get_text()
            brewer = beer.find("p", {"id": "brewer"}).get_text()
            strength = beer.find("p", {"id": "strength"}).get_text()
            beer_json =    {
            "name": name,
            "brewer": brewer,
            "strength": strength
            }
            beer_list.append(beer_json)
    print(beer_list)
```

This creates a beer_list that we want to create a in a format that is more easy for us to use, such as a JSON object. 
Anyway the beers that we found in the original beautiful soup parsing are looped through and we find the name, brewer and strength in the HTML document. This is found in the beer object in each iteration through beers, then using the find and get_text methods from beautiful soup to find each property. Finally we construct a JSON beer object that we add to our beer_list array and then print it. 

Run the new version of the function by calling your application in the python environment.

```bash
app\app.py
```

You should end up with something that looks like this, which is an JSON of the tasty beers we have parsed. Hmm... this feels like we could POST it to an API or something, one to look at when I feel more sober...

```json
[   
    {
    "name": "Mike Rayer", 
    "brewer": "Crafty Devil", 
    "strength": "4.2%"
    }
, 
    {
    "name": "Elvis Juice",
     "brewer": "Brew Dog",
      "strength": "5.2%"
    }
]
```

Next replace your entire code with the below, this makes the seeking of pages and beers a little more configurable before we move on to the individual beer configuration.

```py
from bs4 import BeautifulSoup

def guzzle_beer(url, beers_class, beer_class):

    with open(url) as page:
        soup = BeautifulSoup(page,"html.parser")
        contents = soup.find("div", class_=beers_class)
        beers = contents.find_all("div", {"class": beer_class})
        beer_list = []
        for beer in beers:
            name = beer.find("p", {"id": "name"}).get_text()
            brewer = beer.find("p", {"id": "brewer"}).get_text()
            strength = beer.find("p", {"id": "strength"}).get_text()
            beer_json =    {
            "name": name,
            "brewer": brewer,
            "strength": strength
            }
            beer_list.append(beer_json)

    return beer_list

if __name__ == '__main__':
    url, beers_class, beer_class = "test/pages/test01.html" \
    , "beers", "beer"

    beer_list = guzzle_beer(url
    , beers_class=beers_class
    , beer_class=beer_class)

    print(beer_list)
```

What this has done now is allowed the guzzle_beer function to take in parameters for the URL, beers div class and beer div class. It now returns a beer_list array object that is then printed in the main function, where the parameters for the configuration are also currently passed. You should get the same beers list of JSON beers that you had before when you run the app again, just now it's a little more configurable.

```bash
app\app.py
```

## Configure your Guzzling

For now we're going to put all of the beer config into a python function that we will put above our guzzle_beer function. Copy and paste the below into your app/app.py file above the guzzle_beer function.

```py
def get_beer_config():
    url = "test/pages/test01.html"
    beers_class = "beers"
    beer_class = "beer"
    beer_config = {
        "name":
        {
            "dom_object": "p",
            "dom_identifier": "id",
            "identifier_value": "name"
        },
          "brewer":
        {
            "dom_object": "p",
            "dom_identifier": "id",
            "identifier_value": "brewer"
        },
          "strength":
        {
            "dom_object": "p",
            "dom_identifier": "id",
            "identifier_value": "strength"
        }
    }

    return url, beers_class, beer_class, beer_config
```

This function returns the configuration of the url, beers class and beer class that we had before in the main function, but also now a new dictionary to help us find the properties we want to find for this specific url. These are the keys of name, brewer and strength along with where to find them in the DOM of the html page. You can imagine this coming from a configurable data store, but for now hard coding it in this application is fine for the demo.

Next replace your guzzle_beer function with the following version of the function:

```py
def guzzle_beer(url:str,beers_class: str, beer_class: str, beer_config: dict):

    beer_list = []
    with open(url) as page:
        soup = BeautifulSoup(page,"html.parser")
        contents = soup.find("div", class_=beers_class)
        beers = contents.find_all("div", {"class": beer_class})
        for beer in beers:
            beer_dict = {}
            for key in beer_config:
                dom_object = beer_config[key]["dom_object"]
                dom_identifier = beer_config[key]["dom_identifier"]
                identifier_value = beer_config[key]["identifier_value"]
                value = beer.find(dom_object, {dom_identifier: f"{identifier_value}"}).get_text()
                beer_dict.update({key:value})
            beer_list.append(beer_dict)

    return beer_list
```

For each beer now in the beers div that we find, it loops over each key in the beer config and pulls our the properties it requires to seek them out, appending them to a dictionary for each beer we find. For each name, brewer and strength for each beer, it gets the dom object, dom identifier and the value that identifies it. These all then get passed  into the original beautiful soup command we had to find and get the actual text for these. This just makes it far more dynamic now from some configuration data! It adds the value found until the full dictionary is constructed of name, brewer and strength. These full constructed beer dictionaries are then added to the beer_list just like before and are equivalent to the JSON objects we already had. Awesome sauce. Such power.

Before calling the application we now need to adjust the running of the main method to pass in the new configuration. Update the main section of your app.py to look like the below.

```py
if __name__ == '__main__':

    url, beers_class, beer_class, beer_config = get_beer_config()

    beer_list = guzzle_beer(url
    , beers_class=beers_class
    , beer_class=beer_class
    , beer_config=beer_config)

    print(beer_list)
  ```

  Running the application again you should end up with the same beer list as before, but now from a far more configurable baseline.

```bash
app\app.py
```

## Complete Code

Just in case the complete code for this beer guzzling solution is shown below.

```py
from bs4 import BeautifulSoup

def get_beer_config():
    url = "test/pages/test01.html"
    beers_class = "beers"
    beer_class = "beer"
    beer_config = {
        "name":
        {
            "dom_object": "p",
            "dom_identifier": "id",
            "identifier_value": "name"
        },
          "brewer":
        {
            "dom_object": "p",
            "dom_identifier": "id",
            "identifier_value": "brewer"
        },
          "strength":
        {
            "dom_object": "p",
            "dom_identifier": "id",
            "identifier_value": "strength"
        }
    }

    return url, beers_class, beer_class, beer_config

def guzzle_beer(url:str,beers_class: str, beer_class: str, beer_config: dict):

    beer_list = []
    with open(url) as page:
        soup = BeautifulSoup(page,"html.parser")
        contents = soup.find("div", class_=beers_class)
        beers = contents.find_all("div", {"class": beer_class})
        for beer in beers:
            beer_dict = {}
            for key in beer_config:
                dom_object = beer_config[key]["dom_object"]
                dom_identifier = beer_config[key]["dom_identifier"]
                identifier_value = beer_config[key]["identifier_value"]
                value = beer.find(dom_object, {dom_identifier: f"{identifier_value}"}).get_text()
                beer_dict.update({key:value})
            beer_list.append(beer_dict)

    return beer_list

if __name__ == '__main__':

    url, beers_class, beer_class, beer_config = get_beer_config()

    beer_list = guzzle_beer(url
    , beers_class=beers_class
    , beer_class=beer_class
    , beer_config=beer_config)

    print(beer_list)
```
