---
title: "Create a Cracker of an Open API Contract with VS Code, Spectral, Prism and Schemathesis"
date: 2024-12-22
author: dataGriff
description: "Create a Cracker of an Open API Contract with VS Code, Spectral, Prism and Schemathesis"
image:
  path: assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/link.png
tags: API
---

I've become super interested in the design, or contract, first approach to APIs, events and data products with [Open API](https://www.openapis.org/){:target="\_blank"}, [Async API](https://www.asyncapi.com/en){:target="\_blank"} and [data contract](https://datacontract.com/){:target="\_blank"} respectively. Contract driven development sounds to me like the way of removing the noise of ambiguous specifications and bridging that gap between requirements and implementation, by making the contract the source of truth, that can be used for your design and subsequent automated testing of the implementation. With Open API contracts having the longest history, and with that more maturity, I decided to explore this space of creating an Open API contract and what that process would be and what tools are available. I hope from this I can learn what I would like and expect from other integration points such as events and data products. The following blog post summarises my initial process and then provides a walkthrough with an intentionally simple whiskey CRUD API.

- [Pre-Requisites](#pre-requisites)
  - [VS Code Extensions](#vs-code-extensions)
- [The Design First Process](#the-design-first-process)
- [Requirements](#requirements)
- [Domain Model](#domain-model)
- [API Contract](#api-contract)
- [Lint API Contract](#lint-api-contract)
- [Mock API Contract](#mock-api-contract)
- [Manually Test Mock API](#manually-test-mock-api)
- [Automate Testing against Mock API](#automate-testing-against-mock-api)
- [What Next?](#what-next)
  - [Mocking and Testing Tools](#mocking-and-testing-tools)
  - [The Role of Artificial Intelligence](#the-role-of-artificial-intelligence)
  - [Hosting Contracts](#hosting-contracts)

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

## Requirements

The requirements are to create a simple CRUD (create, read, update, delete) whiskey API that provides an inventory of glorious whiskies. Both the requirements and domain model for this blog post are intentionally simple as requirement gathering and domain driven design are massive topics of their own. However I wanted to highlight to myself and others that this is an important part of the process that will inform what your API contract should look like and should be given a large proportion of your time. Usually when creating an API you want to stay clear of CRUD language and stay close to business behaviour terminology, again, as this is just a simple inventory of whiskies though a CRUD mentality is ok in this instance (phew). To document the requirements I decided to go down the BDD (behaviour driven development) route and create feature file(s). As I have mentioned earlier this method may change, but the process of needing requirements and formally capturing them somehow will not. In reality you would have a number of feature files documenting the required behaviour for different scenarios.

Here is my feature file for the whiskey inventory which starts to give me an understanding of what the API should do.

```feature
Feature: Manage Whiskey Inventory

  As a whiskey enthusiast
  I want to manage whiskey records in the inventory
  So that I can keep track of what whiskies are available

  Scenario: Create a new whiskey
    Given I am on the "Add Whiskey" page
    When I enter the whiskey name "Glenfiddich"
    And I enter the type "Single Malt"
    And I enter the age "12"
    And I click the "Save" button
    Then I should see a confirmation message "Whiskey added successfully"
    And the whiskey "Glenfiddich" should appear in the whiskey list

  Scenario: View a list of whiskeys
    Given I have the following whiskeys in the system:
      | Name         | Type        | Age |
      | Glenfiddich  | Single Malt | 12  |
      | Macallan     | Single Malt | 15  |
    When I navigate to the "Whiskey List" page
    Then I should see the following whiskeys:
      | Name         | Type        | Age |
      | Glenfiddich  | Single Malt | 12  |
      | Macallan     | Single Malt | 15  |

  Scenario: Update an existing whiskey
    Given the whiskey "Glenfiddich" exists in the system
    When I navigate to the "Edit Whiskey" page for "Glenfiddich"
    And I update the age to "18"
    And I click the "Save" button
    Then I should see a confirmation message "Whiskey updated successfully"
    And the whiskey "Glenfiddich" should have the age "18" in the whiskey list

  Scenario: Delete a whiskey
    Given the whiskey "Macallan" exists in the system
    When I click the "Delete" button for "Macallan"
    Then I should see a confirmation message "Whiskey deleted successfully"
    And the whiskey "Macallan" should not appear in the whiskey list
```

## Domain Model

As we only have one feature and one entity in this application (whiskey), then the domain model becomes ridiculously simple. Again as mentioned above this is intentional as I wanted to focus on the creation of a contract experience over creating a complex API (I am new to this!) - but at the same time documenting this step in the process so you give it a good portion of you time before diving in! Below is an image of the super simple domain model containing one whiskey entity, for further insight into domain model explore [domain driven design](https://martinfowler.com/bliki/DomainDrivenDesign.html){:target="\_blank"} and [domain models](https://www.thoughtworks.com/en-gb/insights/blog/agile-project-management/domain-modeling-what-you-need-to-know-before-coding).

![Domain Model]({ site.baseurl }/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/domain_model.drawio.png)

**Hint:** I used the [draw.io vs code extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio){:target="\_blank"} to create this and if you search for uml in the templates its pretty close to what you need for a domain model.

![Draw IO]({ site.baseurl }/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/drawio.PNG)

## API Contract

## Lint API Contract

## Mock API Contract

## Manually Test Mock API

## Automate Testing against Mock API

## What Next?

### Mocking and Testing Tools

### The Role of Artificial Intelligence

### Hosting Contracts
