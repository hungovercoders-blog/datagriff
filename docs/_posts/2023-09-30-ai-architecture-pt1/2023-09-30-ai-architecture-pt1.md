---
title: "AI for Software Architecture Part 1 | Generating boiler plate software architecture with chatgpt and event catalog"
date: 2023-09-30
author: dataGriff
description: Part one of using AI to generate software architecture and documentation with event catalog
image:
  path: /assets/2023-09-30-ai-architecture-pt1/link.png
tags: AI ChatGpt EventCatalog Architecture
---

Unless you've been living under a rock (or some rubble caused by the rise of the machines) you must have heard of [chatgpt](https://chat.openai.com/) by now. This is a large language model that can write poetry, write content (see my post on [SEO](https://blog.hungovercoders.com/datagriff/2023/06/03/seo-optimisation.html)) and even generate excellent boilerplate code for pretty much any language and design pattern. I was keen on seeing how well it could do at generating logical software architecture... My plan therefore is to combine new AI models with this great open source [event catalog](https://www.eventcatalog.dev/) tooling that has templates for markdown I hope to leverage. This first part of the blog series is going to be generating a domain, event and team schema JSON using chatgpt. I will then use this to feed into [event catalog markdown templates](https://www.eventcatalog.dev/docs/events/introduction) in part 2. Hold on to your drinks..!

- [Prerequisites](#prerequisites)
- [Proof of Concept Using ChaptGPT](#proof-of-concept-using-chaptgpt)
- [Generate ChatGPT API Key](#generate-chatgpt-api-key)
- [Configure Environment API Key Variable](#configure-environment-api-key-variable)
- [Calling ChatGPT API Basics](#calling-chatgpt-api-basics)
- [Generating Domain, Event and Team JSON](#generating-domain-event-and-team-json)
- [Next Time](#next-time)

## Prerequisites

- [Github Account](https://www.github.com) - If you haven't already get yourself a github account, this is how you're going to host code and optionally open up gitpod.
- [Chatgpt Account](https://chat.openai.com/) - You'll want to get yourself on this page and ensure its bookmarked, every other developer does! I actually pay for the premium version which is about twenty pounds a month and allows me to use the latest GPT-4 model available which is also a lot faster. I think its totally worth it if you're a mad hungovercoder like me as it generates so much proof of concept code for you to get you going quickly. You won't regret it. 
- A tenner (optional unless you want to do the API part). In order to be fancy and call the ChatGPT API you need to pay. I have done a number of calls now with my ten pounds and you can keep track of it quite easily without the fear of going over any budget. Once you've spent your credit, you simply won't be able to call the API any more.

## Proof of Concept Using ChaptGPT

Before we dive into the programmatic API calling of what we want to achieve lets just demonstrate it using the ChatGPT GUI. Here we can also see the importance of getting the right prompts, of which we will use the best one in our API call, and where the idea of a "[prompt engineer](https://en.wikipedia.org/wiki/Prompt_engineering)" role is coming from.

**We want to generate a JSON schema containing domain, events and team for a given software architecture.**

Tidy. Lets enter into ChatGPT "Please return me the software architecture for a dog rescue in JSON format that includes domain, events and team".

![Chatgpt First Attempt]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-first-attempt.PNG)

The response is actually awesome but I want the schema to be simpler so that I can leverage it with event catalog. I want the schema to be something like the following:

```json
[
    {"domain": "Domain01", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain01", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain02", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"}
]
```

Lets now try "**Please return me the software architecture for a dog rescue in JSON format that includes domain, events and team following this format [
    {"domain": "Domain01", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain01", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain02", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"}
]**".

![Chatgpt Second Attempt]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-second-attempt.PNG)

Nice! We're nearly there. For the API call I am not going to want any English text around the JSON, I will just want the JSON response. Finally then lets try "**Please return me the JSON response only in this format
[
    {"domain": "Domain01", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain01", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain02", "event": "EntityVerb", "team": "Team01"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"},
    {"domain": "Domain03", "event": "EntityVerb", "team": "Team02"}
]
for the software architecture for a dog rescue.**".

![Chatgpt Third Attempt]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-third-attempt.PNG)

Bingo. We've got the JSON format we want and only the JSON schema we want returned. You'll notice that ChatGPT has returned slightly different variations each time in the actual values too, this is why at the moment this whole exercise will be for boilerplate ideas and it will be up to you to refine the architecture. Still its great to get some ideas quickly!

## Generate ChatGPT API Key

As mentioned your first going to need to spend a bit of money in order to use chatgpt api in a programmatic way. You can quite happily stop at the above as you have a schema and we can start to use that in part 2 as well without using the paid for version. In order to use the paid for version you'll need to go to [chatgpt platform billing](https://platform.openai.com/account/billing/overview) and add some credit. I added ten pounds and you can see from the below that this is my absolute budget and I am in complete control of how much I spend as auto-recharge is off.

![Chatgpt Credit]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-credit.PNG)

Once you have added credit to your account head over to [api keys](https://platform.openai.com/account/api-keys) and generate a new one. Copy this ready to paste into your environment variables in the next section.

![Chatgpt API Key]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-api-key.PNG)

## Configure Environment API Key Variable

As you may know from my [previous blog post on gitpod](https://blog.hungovercoders.com/datagriff/2023/09/09/dotnet-api-container-gitpod.html) I am completely immersed in the cloud developer experience it offers. You can add your api key to your local environment variables if you wish, but I thought this would be a good opportunity to show how I can use [environment variables](https://www.gitpod.io/docs/configure/projects/environment-variables) across projects in gitpod.

![Gitpod Environment Variables]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/gitpod-env-vars.PNG)

The scoping seen above basically means what gitpod projects the variables will apply to so you can add specific paths. I'll likely be using this API key in lots of place which is why I have just gone for the wildcard approach. You'll see in the next session how I can call this just like any local environment variable.

## Calling ChatGPT API Basics

Now that we have our API key setup we can open up this [repository](https://github.com/hungovercoders/event.catalog.template) in gitpod and call ChatGPT with the basics. I have already configured the workspace with a [gitpod.yml file](https://github.com/hungovercoders/event.catalog.template/blob/main/.gitpod.yml) so that an appropriate python environment with the correct libraries will be installed via the simple [requirements.txt file](https://github.com/hungovercoders/event.catalog.template/blob/main/catalog-generator/requirements.txt). The libraries are requests for the api call and openai for the chatgpt usage.

To prove the basic call we can enter this into a file called basic.py and execute by running python basic.py in the terminal.

```py
import openai
openai.api_key = os.getenv("CHATGPT_KEY")
topic = "beer"
words = 500
message = f"Tell me as much as you can about {topic} in less than {words} words and you must include at least one pun."
chat_completion = openai.ChatCompletion.create(model="gpt-4"
                                               , messages=[{"role": "user", "content": message}])
out = chat_completion['choices'][0]['message']['content']
print(out)
```

This code gets the API key we setup called "CHATGPT_KEY" to provide the credentials. It then provides a topic with a maximum amount of words and a command to ask of ChatGPT. I can never get enough of beer so I thought I would ask for some more information and also request a pun, because who doesn't like puns?!  The output is then parsed to get the content that is then printed out in this instance to the terminal window.

![Chatgpt Basic API Call]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-basic-api-call.PNG)

## Generating Domain, Event and Team JSON

Right lets get into the meat of this now we know what w're trying to achieve and how to do it.

The proceeding code can be found in the [ongoing repo here](https://github.com/hungovercoders/event.catalog.template/blob/main/catalog-generator/event_lists/app.py) and it does the following:
- Creates a function to get the latest version of the software architecture provided in the path {architecture_required}/{architecture_required}_{version}.json
- Creates a function that gets the directory of where the software architecture event list output will be stored.
- Creates a function that calls ChatGPT with the required architecture and JSON template version from [the template folder](https://github.com/hungovercoders/event.catalog.template/tree/main/catalog-generator/event_lists/template). You therefore have some flexibility in applying a certain template style to your event lists if you find one that really seems to work. You'll notice I actually call ChatGPT three times in the API and then ask ChatGPT to pick the best - code review yourself please! This is becoming a bit of a trick for prompt engineers as these models often output different answers. However, I might be being a bit indulgent here as I am spending money so I'll possibly reduce this down...
- It then creates a function that writes out the final event list to a file so that we can use it later for generating an event catalog (I can't wait for part 2 can you??)
- Finally it calls the main function which combines the above to write out event lists for different architecture to the correct directories.

```py
import os
import openai
import requests
import json

def get_latest_architecture_version(dir_path: str):
    """Gets latest architecture version from directory

    Args:
        dir_path (str): The directory path to search

    Returns:
        str: The architecture version
    """
    int_version = 1
    if(os.path.exists(dir_path)):
        files = os.listdir(dir_path)
        for file in files:
            version = file.split('_')[-1].replace(".json","")
            int_version = int(version) + 1
        version_str = str(int_version)
    version_str = version_str.rjust(3, '0') 
    return version_str

def get_filepath(architecture_required : str):
    """Returns filepath for events architecture

    Args:
        architecture_required (str): The system of he software architecture required

    Returns:
        _type_: The filepath for the event architecture
    """
    architecture_path = architecture_required.replace(" ","_")
    isExist = os.path.exists(architecture_path)
    if not isExist:
        os.makedirs(architecture_path)
        print("The new directory is created!")
    version = get_latest_architecture_version(architecture_path)
    file_path = f"{architecture_path}/{architecture_path}_{version}.json"
    return file_path

def get_event_list(architecture_required : str, template_version: int):
    """
    Calls chatgpt to get domain, event and team list
    """
    
    openai.api_key = os.getenv("CHATGPT_KEY")
    template_version_str = str(template_version).rjust(3, '0') 
    
    with open(f'template/template_{template_version_str}.json') as template_file:
        json_template = json.load(template_file)
    
    answers = []
    
    for i in range(1,4):

        print(f"Calling API {i} time to get the json architecture for {architecture_required}...")
        chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user"
        , "content": f"""Return the JSON only in your response for an event catalog that supports a software
        architecture for an {architecture_required} system using this JSON as the example template {json_template} to inform your choices
        for the software architecture."""}])
        out = chat_completion['choices'][0]['message']['content']
        print(f"Called API {i} times to get the json architecture for {architecture_required}.")
        answers.append(out)
        
    print(f"Calling API to ask which is the best json architecture for {architecture_required}...")
    chat_completion = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "user"
    , "content": f"""Return the JSON only in your response of the best json representation of the software architecture for {architecture_required} that is found in {answers} given the template {json_template}."""}])
    final_answer = chat_completion['choices'][0]['message']['content']
    print(f"Called API to ask which is the best json architecture for {architecture_required}...")
    
    return final_answer
    
def write_event_list(architecture_required  : str, event_list : str):
    """
    Writes domain, event and team schema to file
    """
    
    file_path = get_filepath(architecture_required)
    print(f"The event list json will write out to {file_path}.")

    print(f"Writing out file to {file_path}...")
    with open(file_path, "w") \
    as outfile:
        outfile.write(event_list)
    print(f"Written out file to {file_path}.")
    
def main():
    """
    Runs the main program to get architecture event list schema for desired software system
    """
    print('Enter the software architecture you require:')
    architecture_required = input()
    print('JSON template version required:')
    template_version = input()
    event_list = get_event_list(architecture_required, template_version)
    write_event_list(architecture_required, event_list)

if __name__ == '__main__':
    main()
```

You can run the code in the terminal by running the below:

```bash
cd catalog-generator
cd event_lists
python app.py
```

Then entering the software architecture you want to generate a schema for and give the JSON template version you want to try.

![Chatgpt Event List API Call]({{ site.baseurl }}/assets/2023-09-30-ai-architecture-pt1/chatgpt-eventlist-api-call.PNG)

You can see the results I have made so far for different software systems in [event lists](https://github.com/hungovercoders/event.catalog.template/tree/main/catalog-generator/event_lists).

A simple example of an output can be seen below:

```json
[
    {"domain": "Inventory","event": "BookAdded","team": "InventoryManagement"}, 
    {"domain": "Inventory","event": "BookRemoved","team": "InventoryManagement"}, 
    {"domain": "ShoppingCart","event": "ItemAdded","team": "CustomersService"}, 
    {"domain": "ShoppingCart","event": "ItemRemoved","team": "CustomersService"}, 
    {"domain": "Orders","event": "OrderPlaced","team": "OrdersProcessing"}, 
    {"domain": "Orders","event": "OrderDelivered","team": "DeliveryService"}, 
    {"domain": "Payments","event": "PaymentReceived","team": "Finance"}, 
    {"domain": "Payments","event": "RefundIssued","team": "Finance"}
]
```

## Next Time

In the next part of this blog series we're going to loop over the domains, events and teams above, automatically creating pages for some [event catalog documentation](https://www.eventcatalog.dev/docs/events/introduction). This will prove we can automate some basic boilerplate software architecture documentation and schemas too! You can keep track of the repo [here](https://github.com/hungovercoders/event.catalog.template/tree/main) in the [hungovercoders organisation](https://github.com/hungovercoders).
