---
title: "Create a Cracker of an Open API Contract with VS Code, Spectral, Prism and Schemathesis"
date: 2024-12-22
author: dataGriff
description: "Create a Cracker of an Open API Contract with VS Code, Spectral, Prism and Schemathesis"
image:
  path: assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/link.png
tags: API
---

I've become super interested in the design, or contract, first approach to APIs, events and data products with [Open API](https://www.openapis.org/){:target="\_blank"}, [Async API](https://www.asyncapi.com/en){:target="\_blank"} and [data contract](https://datacontract.com/){:target="\_blank"} respectively. Contract driven development sounds to me like the way of removing some of the noise of ambiguous specifications and bridging that gap between requirements and implementation, by making the contract the source of truth that can be used for your design and subsequent automated testing of implementation. With Open API contracts having the longest history, and with that more maturity, I decided to explore this space of creating an Open API contract and what that process would be and what tools are available. I hope from this I can learn what I would like and expect from other integration points such as events and data products. The following blog post summarises my initial process and then provides a walkthrough with an intentionally simple whiskey CRUD API.

## Pre-Requisites

- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}

### VS Code Extensions

These extensions will have their own sections in the blog post but its worth being aware of their awesomeness now.

- [Drawio](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio){:target="\_blank"}
- [Open API](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi){:target="\_blank"}
- [YAML](https://open-vsx.org/extension/redhat/vscode-yaml){:target="\_blank"}
- [Spectral](https://marketplace.visualstudio.com/items?itemName=stoplight.spectral){:target="\_blank"}
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens){:target="\_blank"}
- [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client){:target="\_blank"}
- [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

As always I will be using the mighty [gitpod](https://gitpod.io){:target="\_blank"} so I won't need to configure anything other than spinning up the default workspace.

## The Design First Process

It's very important that I stress my goal here is to establish a process of creating, validating and testing an open API contract with the goal of producing a design first workflow. Whilst I have used tools here that helped me, that I want to share with you, I see myself being able to swap them out as and when I need to, for example when I find advantages by using others (its a huge space and I have a number of tools I want to investigate). However in order for me to understand what I need the tools for, I wanted to establish a process that I could follow and also automate as much as possible.

1. **Gather requirements** - Simple ways to document requirements of API behaviour. I decided to go down the BDD route and establish a simple feature file.
2. **Document domain model** - Simple way to document a domain model. I have used [drawio vs code extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio){:target="\_blank"} and embedded this image in the API info section of the contract.
3. **Document API Contract** - Fast feedback IDE for creating an API contract. Using [VS Code](https://code.visualstudio.com/download){:target="\_blank"} with [YAML extension](https://open-vsx.org/extension/redhat/vscode-yaml){:target="\_blank"} and [openapi extension](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi){:target="\_blank"} made this a fairly straight forward experience.
4. **Lint API Contract** - Levelling up your API contract with rules for the Open API specification, above and beyond basic yaml formatting, and any rules you want to apply for your own consistency of API designs. I decided to use [Spectral](https://stoplight.io/open-source/spectral){:target="\_blank"} for this which also comes with a [Spectral VS Code extension](https://marketplace.visualstudio.com/items?itemName=stoplight.spectral){:target="\_blank"}.
5. **Mock API Contract** - Run a mock against the contract so you know its ok for consumers. There is a huge number of API mocking tools out there but at this point I have used [prism](https://stoplight.io/open-source/prism){:target="\_blank"} as its really easy to use though limited in capabilities. For this, and subsequent automated linting and testing, I leveraged docker compose so having the [docker vs code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker){:target="\_blank"} installed is a good idea.
6. **Manually Test Mock API** - Quickly interact with your mock. I used the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client){:target="\_blank"} in VS code as I can keep all the calls local to the contract in source control that are available to all.
7. **Automate Testing against Mock API** - Quickly test all the endpoints of your mock. This might be overkill as the method of testing is based on the contract, which is what the mock is... but I used [schemathesis](https://schemathesis.readthedocs.io/en/stable/){:target="\_blank"} to perform automatically generated tests against the mock very quickly.

Whilst researching this blog post I came across this [excellent video on contract first development](https://www.youtube.com/watch?v=Z-_2vuSfl88){:target="\_blank"} by [Andrey Fadeev](https://www.youtube.com/@andrey.fadeev){:target="\_blank"} that pretty much summarised where my thoughts were at. I highly recommend giving this a watch as he also covers the automation of changelogs which I have not covered here.

![Image Description]({ site.baseurl }/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/image-01.PNG)

## Requirements

## Domain Model

## API Contract

## Lint API Contract

## Mock API Contract

## Manually Test Mock API

## Automate Testing against Mock API

## What Next?
