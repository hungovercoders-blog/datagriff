---
title: "Create a Cracker of an Open API Contract with VS Code, Spectral, Prism and Schemathesis"
date: 2024-12-22
author: dataGriff
description: "Create a Cracker of an Open API Contract with VS Code, Spectral, Prism and Schemathesis"
image:
  path: assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/link.PNG
tags: API
---

I've become super interested in the design, or contract, first approach to APIs, events and data products with [Open API](https://www.openapis.org/){:target="\_blank"}, [Async API](https://www.asyncapi.com/en){:target="\_blank"} and [data contract](https://datacontract.com/){:target="\_blank"} respectively. Contract driven development sounds to me like the way of removing the noise of ambiguous specifications and bridging that gap between requirements and implementation, by making the contract the source of truth, that can be used for your design and subsequent automated testing of the implementation. With Open API contracts having the longest history, and with that more maturity, I decided to explore this space of creating an Open API contract and what that process would be and what tools are available. I hope from this I can learn what I would like and expect from other integration points such as events and data products. The following blog post summarises my initial process and then provides a walkthrough with an intentionally simple whiskey CRUD API.

- [Pre-Requisites](#pre-requisites)
  - [VS Code Extensions](#vs-code-extensions)
- [The Design First Process](#the-design-first-process)
- [Requirements](#requirements)
- [Domain Model](#domain-model)
- [API Contract](#api-contract)
  - [Post Endpoint](#post-endpoint)
  - [Get Endpoint](#get-endpoint)
  - [Open API Extension](#open-api-extension)
  - [Formatting Errors](#formatting-errors)
- [Lint API Contract](#lint-api-contract)
  - [Out of the Box](#out-of-the-box)
  - [Custom Rules](#custom-rules)
  - [Spectral CLI with Docker Compose](#spectral-cli-with-docker-compose)
- [Mock API Contract](#mock-api-contract)
  - [Manually Test Mock API](#manually-test-mock-api)
- [Automate Testing against Mock API](#automate-testing-against-mock-api)
- [What Next?](#what-next)
  - [Intgerating with Pre-Commit and CI](#intgerating-with-pre-commit-and-ci)
  - [Changelogs](#changelogs)
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
- [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens){:target="\_blank"}
- [Spectral](https://marketplace.visualstudio.com/items?itemName=stoplight.spectral){:target="\_blank"}
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

so really I should have an 8th step...

- **Automation of Change Logs** - Automate the generation of change logs from the contract. I've not covered in this blog but I imagine I need to look into tools like [oasdiff](https://www.oasdiff.com/) that can fit this need.

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
    When I enter the whiskey name "Myth"
    And I enter the brand "Penderyn"
    And I enter the age "8"
    And I enter the type "Single Malt"
    And I click the "Save" button
    Then I should see a confirmation message "Whiskey added successfully"
    And the whiskey "Glenfiddich" should appear in the whiskey list

  Scenario: View a list of whiskeys
    Given I have the following whiskeys in the system:
      | Name      | Brand        | Age | Type         |
      | Myth      | Penderyn     | 8   | Single Malt  |
      | Lasanta   | Glenmorangie | 12  | Single Malt  |
    When I navigate to the "Whiskey List" page
    Then I should see the following whiskeys:
      | Name      | Brand        | Age | Type         |
      | Myth      | Penderyn     | 8   | Single Malt  |
      | Lasanta   | Glenmorangie | 12  | Single Malt  |

  Scenario: Update an existing whiskey
    Given the whiskey "Myth" exists in the system
    When I navigate to the "Edit Whiskey" page for "Myth"
    And I update the age to "18"
    And I click the "Save" button
    Then I should see a confirmation message "Whiskey updated successfully"
    And the whiskey "Myth" should have the age "18" in the whiskey list

  Scenario: Delete a whiskey
    Given the whiskey "Lasanta" exists in the system
    When I click the "Delete" button for "Lasanta"
    Then I should see a confirmation message "Whiskey deleted successfully"
    And the whiskey "Lasanta" should not appear in the whiskey list
```

## Domain Model

As we only have one feature and one entity in this application (whiskey), then the domain model becomes ridiculously simple. Again as mentioned above this is intentional as I wanted to focus on the creation of a contract experience over creating a complex API (I am new to this!) - but at the same time documenting this step in the process so you give it a good portion of you time before diving in! Below is an image of the super simple domain model containing one whiskey entity, for further insight into domain model explore [domain driven design](https://martinfowler.com/bliki/DomainDrivenDesign.html){:target="\_blank"} and [domain models](https://www.thoughtworks.com/en-gb/insights/blog/agile-project-management/domain-modeling-what-you-need-to-know-before-coding).

![Domain Model]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/domain_model.drawio.png)

**Hint:** I used the [draw.io vs code extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio){:target="\_blank"} to create this and if you search for uml in the templates its pretty close to what you need for a domain model.

![Draw IO]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/drawio.PNG)

## API Contract

The API contract will be developed in VS code initially leveraging the [Open API](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi){:target="\_blank"}, [YAML](https://open-vsx.org/extension/redhat/vscode-yaml){:target="\_blank"} and [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens){:target="\_blank"} extension. We'll be using more later but I want to highlight what they bring to the table as we walk through.

To see the final API contract at any point just go [here]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/whiskey_inventory.1.oas.yml), but the rest of the blog will give you insights into the how and why it ended up looking like it did...

Based on the feature requirements and domain model, I know roughly my endpoints will look something like the following before I start my API contract:

```bash
POST whiskies/ ## to create a whiskey
GET whiskies/ ## to get a list of whiskies
GET whiskies/{id} ## get a single whiskey
PUT whiskies/{id} ## udpate a single whiskey
DELETE whiskies/{id} ## delete a single whiskey
```

### Post Endpoint

The first areas of the open api contract we'll create will be:

- **OpenAPI Version**
- **Info** - including title, details and description
- **Servers** - just a mock endpoint at this point in preparation
- **Tags** - even though we have a simple API, its worth adding tags now and keeping your contract organised.
- **Paths** - We'll add one POST endpoint first so that we have a valid Open API contract. I have utilised the term "whiskies" to acknowledge we are interacting with a collection of items. One example has been added but you can add more if you need a richer document for testing and you consumers.
- **Components** - For the schemas we'll reuse in the contract, in this case the whiskey. Note the use of **allOf** in whiskeyWithID schema so that we can leverage the original whiskey schema that wouldn't have an ID generated for it yet, but return it in a response. I have restricted the whiskey brands to be a shortlist of enums so the API contract remains small for this demo, but I will eventually add all known brands!

```yaml
openapi: 3.0.4
info:
  title: Whiskey Inventory
  description: |
    Whiskey Inventory.<br>
    ## Domain Model
    ![Domain Model](https://github.com/hungovercoders-blog/datagriff/blob/main/docs/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/domain_model.drawio.png?raw=true)
  version: 1.0.0
servers:
  - url: http://localhost:8080
    description: Mock server for development purposes.
tags:
  - name: Whiskey
    description: Operations related to whiskey
paths:
  /whiskies:
    post:
      description: Add a new whiskey.
      tags:
        - Whiskey
      summary: Add a whiskey
      operationId: addWhiskey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Whiskey"
            examples:
              mythRequest:
                summary: Myth Request
                value:
                  name: Myth
                  brand: Penderyn
                  age: 8
                  type: Single Malt
      responses:
        "201":
          description: Whiskey added successfully.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/WhiskeyWithId"
              examples:
                mythResponse:
                  summary: Response for successfully adding Myth
                  value:
                    id: penderyn-myth
                    name: Myth
                    brand: Penderyn
                    age: 8
                    type: Single Malt
    get:
      description: Get a list of all whiskies.
      tags:
        - Whiskey
      summary: List whiskies
      operationId: listWhiskies
      responses:
        "200":
          description: List of all whiskies.
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                  - pagination
                properties:
                  data:
                    type: object
                    properties:
                      whiskies:
                        type: array
                        maxItems: 10
                        items:
                          $ref: "#/components/schemas/WhiskeyWithId"
                  pagination:
                    $ref: "#/components/schemas/pagination"
              examples:
                allWhiskies:
                  summary: List of all whiskies
                  value:
                    data:
                      whiskeys:
                        - id: penderyn-myth
                          name: Myth
                          brand: Penderyn
                          age: 8
                          type: Single Malt
                        - id: glenmorangie-lasanta
                          name: Lasanta
                          brand: Glenmorangie
                          age: 12
                          type: Single Malt
                        - id: penderyn-legend
                          name: Myth
                          brand: Legend
                          age: 12
                          type: Single Malt
                    pagination:
                      total: 3
                      currentPage: 1
                      perPage: 10

components:
  schemas:
    Whiskey:
      type: object
      required:
        - name
        - brand
        - age
        - type
      properties:
        name:
          type: string
          description: Name of the whiskey.
          example: Myth
          minLength: 2
          maxLength: 30
        brand:
          type: string
          description: Brand of the whiskey.
          example: Penderyn
          enum:
            - Penderyn
            - Glenmorangie
            - Glenfidditch
        age:
          type: integer
          description: How long the whiskey was aged.
          example: 12
          minimum: 3
          maximum: 85
        type:
          type: string
          description: What is the type of whiskey.
          example: Single Malt
          maxItems: 3
          enum:
            - Single Malt
            - Blended

    WhiskeyWithId:
      type: object
      allOf:
        - $ref: "#/components/schemas/Whiskey"
        - type: object
          properties:
            id:
              type: string
              description: Unique identifier for the whiskey.
              example: penderyn-myth
```

### Get Endpoint

No we'll add a GET endpoint to retrieve all of our whiskies from the whiskies path. When we do this we're going to move the whiskey array into a "data" object and add a "pagination" object in there too. This means the client can manage pages correctly and also using an object for data will be more extensible in the future than returning a straight up array. See the updated contract below.

```yaml
openapi: 3.0.4
info:
  title: Whiskey Inventory
  description: |
    Whiskey Inventory.<br>
    ## Domain Model
    ![Domain Model](https://github.com/hungovercoders-blog/datagriff/blob/main/docs/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/domain_model.drawio.png?raw=true)
  version: 1.0.0
servers:
  - url: http://localhost:8080
    description: Mock server for development purposes.
tags:
  - name: Whiskey
    description: Operations related to whiskey
paths:
  /whiskies:
    post:
      description: Add a new whiskey.
      tags:
        - Whiskey
      summary: Add a whiskey
      operationId: addWhiskey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Whiskey"
            examples:
              mythRequest:
                summary: Myth Request
                value:
                  name: Myth
                  brand: Penderyn
                  age: 8
                  type: Single Malt
      responses:
        "201":
          description: Whiskey added successfully.
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/WhiskeyWithId"
              examples:
                mythResponse:
                  summary: Response for successfully adding Myth
                  value:
                    id: penderyn-myth
                    name: Myth
                    brand: Penderyn
                    age: 8
                    type: Single Malt
    get:
      description: Get a list of all whiskies.
      tags:
        - Whiskey
      summary: List whiskies
      operationId: listWhiskies
      responses:
        "200":
          description: List of all whiskies.
          content:
            application/json:
              schema:
                type: object
                required:
                  - data
                  - pagination
                properties:
                  data:
                    type: object
                    properties:
                      whiskies:
                        type: array
                        maxItems: 10
                        items:
                          $ref: "#/components/schemas/WhiskeyWithId"
                  pagination:
                    $ref: "#/components/schemas/pagination"
              examples:
                allWhiskies:
                  summary: List of all whiskies
                  value:
                    data:
                      whiskeys:
                        - id: penderyn-myth
                          name: Myth
                          brand: Penderyn
                          age: 8
                          type: Single Malt
                        - id: glenmorangie-lasanta
                          name: Lasanta
                          brand: Glenmorangie
                          age: 12
                          type: Single Malt
                        - id: penderyn-legend
                          name: Myth
                          brand: Legend
                          age: 12
                          type: Single Malt
                    pagination:
                      total: 3
                      currentPage: 1
                      perPage: 10

components:
  schemas:
    Whiskey:
      type: object
      required:
        - name
        - brand
        - age
        - type
      properties:
        name:
          type: string
          description: Name of the whiskey.
          example: Myth
          minLength: 2
          maxLength: 30
        brand:
          type: string
          description: Brand of the whiskey.
          example: Penderyn
          enum:
            - Penderyn
            - Glenmorangie
            - Glenfidditch
        age:
          type: integer
          description: How long the whiskey was aged.
          example: 12
          minimum: 3
          maximum: 85
        type:
          type: string
          description: What is the type of whiskey.
          example: Single Malt
          maxItems: 3
          enum:
            - Single Malt
            - Blended

    WhiskeyWithId:
      type: object
      allOf:
        - $ref: "#/components/schemas/Whiskey"
        - type: object
          properties:
            id:
              type: string
              description: Unique identifier for the whiskey.
              example: penderyn-myth

    pagination:
      type: object
      required:
        - total
        - currentPage
        - perPage
      additionalProperties: false
      properties:
        total:
          type: integer
          description: Total number of whiskeys available.
          example: 3
          maximum: 100000
          minimum: 1
        currentPage:
          type: integer
          description: The current page being viewed.
          example: 1
          maximum: 10000
          minimum: 1
        perPage:
          type: integer
          description: Number of whiskeys per page.
          example: 10
          maximum: 10
          minimum: 1
```

### Open API Extension

The open API extension will allow you to see the API document format in the left navigation bar as well as preview the swagger as it currently is.

Here is the outline:

![Open API Extension]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/openapi_outline.PNG)

Here is the swagger preview:

![Open API Swagger]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/openapi_swagger.PNG)

Annoyingly at the moment it does not support Open API version 3.1 (see [here](https://github.com/42Crunch/vscode-openapi/issues/110){:target="\_blank"}), so I will already potentially be keeping an eye out on other tooling here.

### Formatting Errors

[Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens){:target="\_blank"} at this point will highlight basic yaml and open API document errors, such as if certain sections are missing (see below).

![Basic Errors]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/openapi_error_missinginfo.PNG)

It won't, however, highlight any more detailed errors that you might want to enforce in your API contract. This is where Spectral comes in.

## Lint API Contract

I wanted a way to apply my own validation and more indepth rules to the API contract. [Spectral](https://stoplight.io/open-source/spectral){:target="\_blank"} is a tool that allows you to do this and is available as a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=stoplight.spectral){:target="\_blank"}. To take advantage of spectral for open API specifications you need to add a configuration file called ".spectral.yaml" and add the following to the contents:

```yaml
extends: ["spectral:oas"]
```

If you wanted to look at AsyncAPI, another contract I want to explore, you would add:

```yaml
extends: ["spectral:asyncapi"]
```

### Out of the Box

Out of the box Spectral open API ruleset combined with [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens){:target="\_blank"} will highlight any errors in the API contract that do not conform to the schemas specified, which is over and abobe what we originally got. For example, if you have a required field that is not present in the contract, it will highlight this for you.

![Missing Property]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/spectral_missing_property.PNG)

Or if you have a value that is not in the allowed enums, it will highlight this for you.

![Invalid Value]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/spectral_invalid_value.PNG)

For me this was absolutely great as I could see where I had made mistakes in the contract and correct them. I already had one with a missing contact section under info:

![Missing Contact]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/spectral_missing_contact.PNG)

So I added this at the top to remove the error:

```yaml
info:
  title: Whiskey Inventory
  description: |
    Whiskey Inventory.<br>
    ## Domain Model
    ![Domain Model](https://github.com/hungovercoders-blog/datagriff/blob/main/docs/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/domain_model.drawio.PNG?raw=true)
  version: 1.0.0
  contact:
    name: datagriff
    url: https://hungovercoders.com
    email: info@hungovercoders.com
```

I now wanted to go further with this and see if I could apply my own rules to the API contract. Enter [spectral rulesets](https://docs.stoplight.io/docs/spectral/e5b9616d6d50c-rulesets){:target="\_blank"}...

### Custom Rules

You can apply your own API design rules using [spectral rulesets](https://docs.stoplight.io/docs/spectral/e5b9616d6d50c-rulesets){:target="\_blank"}. I wasn't sure what rules I wanted to apply, only that I wanted to apply them. Luckily I found this [page of examples](https://github.com/stoplightio/spectral-rulesets){:target="\_blank"} which included [adidas spectral rules](https://github.com/adidas/api-guidelines/blob/master/.spectral.yml){:target="\_blank"} and also some good security ones from [owasp](https://github.com/stoplightio/spectral-owasp-ruleset){:target="\_blank"}. In this blog post I am not currently concerned with security, as its a big subject in its own right, but I will return to it I promise! I decided to pilfer some of the adidas ones who have published all of their API rules [here](https://github.com/adidas/api-guidelines/blob/master/.spectral.yml).

My simple .spectral.yaml file looks like this:

```yaml
extends: ["spectral:oas"]

rules:
  # ---------------------------------------------------------------------------
  # General OAS rules
  # ---------------------------------------------------------------------------

  paths-kebab-case:
    description: All YAML/JSON paths MUST follow kebab-case
    severity: warn
    recommended: true
    message: "{{property}} is not kebab-case: {{error}}"
    given: $.paths[*]~
    then:
      function: pattern
      functionOptions:
        match: "^\/([a-z0-9]+(-[a-z0-9]+)*)?(\/[a-z0-9]+(-[a-z0-9]+)*|\/{.+})*$"

  path-parameters-camelCase-alphanumeric:
    description: Path parameters MUST follow camelCase
    severity: warn
    recommended: true
    message: "{{property}} path parameter is not camelCase: {{error}}"
    given: $..parameters[?(@.in == 'path')].name
    then:
      function: pattern
      functionOptions:
        match: "^[a-z][a-zA-Z0-9]+$"

  definitions-camelCase-alphanumeric:
    description: All YAML/JSON definitions MUST follow fields-camelCase and be ASCII alphanumeric characters or `_` or `$`.
    severity: error
    recommended: true
    message: "{{property}} MUST follow camelCase and be ASCII alphanumeric characters or `_` or `$`."
    given: $.definitions[*]~
    then:
      function: pattern
      functionOptions:
        match: "/^[a-z$_]{1}[A-Z09$_]*/"

  properties-camelCase-alphanumeric:
    description: All JSON Schema properties MUST follow fields-camelCase and be ASCII alphanumeric characters or `_` or `$`.
    severity: error
    recommended: true
    message: "{{property}} MUST follow camelCase and be ASCII alphanumeric characters or `_` or `$`."
    given: $.definitions..properties[*]~
    then:
      function: pattern
      functionOptions:
        match: "/^[a-z$_]{1}[A-Z09$_]*/"
```

However if I change a property to be camel case now, this is not highlighted in vs code. I tried ensuring that spectral was using the correct .spectral configuration file for the extension, but it still didn't work. I will need to investigate this further, but luckily the spectral CLI can be used to lint the contract and apply the ruleset...

![No Error]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/spectral_vs_code_no_error.PNG)

### Spectral CLI with Docker Compose

I knew I'd want to integrate the spectral linting with a CI pipeline at some point so I decided to use the [spectral CLI with docker compose](https://docs.stoplight.io/docs/spectral/b8391e051b7d8-installation){:target="\_blank"} to lint the API contract. I created a docker-compose.yml file with the following contents:

```yaml
version: "3.9"
services:
  spectral:
    image: stoplight/spectral:5
    command: "lint /tmp/whiskey_inventory.1.oas --ruleset /tmp/.spectral.yml"
    volumes:
      - ./whiskey_inventory.1.oas.yml:/tmp/whiskey_inventory.1.oas:ro
      - ./.spectral.yml:/tmp/.spectral.yml:ro
```

I then ran the following command to lint the API contract:

```bash
docker compose up
```

This will output any errors in the API contract that do not conform to the ruleset. I will need to investigate why the VS Code extension is not picking up the ruleset, but at least I have a way to lint the contract in a CI pipeline.

![Spectral Lint Docker]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/spectral_lint_docker.PNG)

Once all errors are removed then the CLI will report that the contract is valid.

![Spectral Lint Docker Correct]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/spectral_lint_docker_correct.PNG)

This linting can easily be added as a githook to shift left the validation of the API contract.

## Mock API Contract

I wanted to run a mock API against the contract so that I could test it manually and also automate tests against it. I decided to use [prism](https://stoplight.io/open-source/prism){:target="\_blank"} as it was easy to use and I could run it in a [docker compose solution](https://docs.stoplight.io/docs/prism/f51bcc80a02db-installation#docker-compose){:target="\_blank"} alongside my linting. I added the prism execution to my docker-compose.yml file which ended up looking like this:

```yaml
version: "3.9"
services:
  spectral:
    image: stoplight/spectral:5
    command: lint /tmp/whiskey_inventory.1.oas --ruleset /tmp/.spectral.yml
    volumes:
      - ./whiskey_inventory.1.oas.yml:/tmp/whiskey_inventory.1.oas:ro
      - ./.spectral.yml:/tmp/.spectral.yml:ro
  prism:
    image: stoplight/prism:4
    command: "mock -h 0.0.0.0 /tmp/whiskey_inventory.1.oas.yml"
    volumes:
      - ./whiskey_inventory.1.oas.yml:/tmp/whiskey_inventory.1.oas.yml:ro
    ports:
      - "8080:4010" # Serve the mocked API locally as available on port 8080
```

Now when I run the following command:

```bash
docker compose up
```

I now first have my linting checks run and then the prism mock API is started with the endpoints available.

![Prism Running]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/prism_running.PNG)

Next I wanted to easily manually test and save those tests in source...

### Manually Test Mock API

I decided to use the [REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client){:target="\_blank"} extension in VS code to manually test the mock API. I created a new file called "whiskey_inventory.http" and added the following content:

```http
### Add a new whiskey
POST http://localhost:8080/whiskies
Content-Type: application/json

{
  "name": "Myth",
  "brand": "Penderyn",
  "age": 8,
  "type": "Single Malt"
}

### Get a list of all whiskies
GET http://localhost:8080/whiskies
```

Executing the first POST request should return a 201 response for "created" and will mirror what we placed in the response of our contract example for this endpoint.

![Mock POST]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/mock_post.PNG)

Executing the second GET request should return a 200 response for "ok" and will mirror the list that we placed as the response in our contract example for this endpoint.

![Mock GET]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/mock_get.PNG)

If we want to ignore the examples and create dynamic content based on the schemas in the contract, we can use the following syntax in the rest client file to [leverage prism dynamic content](https://docs.stoplight.io/docs/prism/9528b5a8272c0-dynamic-response-generation-with-faker){:target="\_blank"}:

```http
### Add a new whiskey - Dynamic
POST http://localhost:8080/whiskies
Content-Type: application/json
Prefer: dynamic=true

{
  "name": "Myth",
  "brand": "Penderyn",
  "age": 8,
  "type": "Single Malt"
}

### Get a list of all whiskies
GET http://localhost:8080/whiskies
Prefer: dynamic=true
```

This will now return dynamic content based on the schemas in the contract as per the below.

![Dynamic GET]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/dynamic_get.PNG)

I noticed that additional properties would appear in the whiskey schema despite me using additionalProperties:false or unevaluatedProperties: false, this is something I need to investigate further.

Other extensions that could be used to test the APIs are [postman](https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode){:target="\_blank"}, [httpie](https://marketplace.visualstudio.com/items?itemName=wk-j.vscode-httpie){:target="\_blank"} and [thunderclient](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client){:target="\_blank"}, which may be more powerful than the REST Client extension when it comes to more complex flows. For now though I have the need for manual exploratory testing as part of my process and [Rest client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client){:target="\_blank"} covers that need, particularly as I can store the requests in source control alongside the contract.

## Automate Testing against Mock API

I wanted to test the mock API as much as possible without having to write a full suite of manual tests. I came across the tool [schemathesis](https://schemathesis.readthedocs.io/en/stable/index.html){:target="\_blank"} which dynmically generates tests based on the contract. It seemed a bit odd for me to test a mock of the contract on the contract as it was likely guranteed to pass, but I wanted to see how it worked and it couldn't hurt. I also thought this looked like a good tool to test the real API.

I first needed to add CURL to the prism docker image so that I could perform a healthcheck before schemathesis ran, as it needed the API to be available first. I created a dockerfile and added the following to install curl on the prism image:

```Dockerfile
# Extend the base image
FROM stoplight/prism:4

# Install curl
RUN apk add --no-cache curl
```

I then amended the docker compose file to look like the following. I added a healthcheck to the prism service to ensure the API was available before schemathesis ran. I also added the schemathesis service to the docker compose file which would run the tests against the mock API.

```yaml
version: "3.9"
services:
  spectral:
    image: stoplight/spectral:5
    command: lint /tmp/whiskey_inventory.1.oas --ruleset /tmp/.spectral.yml
    volumes:
      - ./whiskey_inventory.1.oas.yml:/tmp/whiskey_inventory.1.oas:ro
      - ./.spectral.yml:/tmp/.spectral.yml:ro

  prism:
    build:
      context: .
      dockerfile: Dockerfile
    command: mock -h 0.0.0.0 /tmp/whiskey_inventory.1.oas.yml
    volumes:
      - ./whiskey_inventory.1.oas.yml:/tmp/whiskey_inventory.1.oas.yml:ro
    ports:
      - 8080:4010 # Serve the mocked API locally as available on port 8080
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:4010/whiskies"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 5s

  schemathesis:
    image: schemathesis/schemathesis:stable
    depends_on:
      prism:
        condition: service_healthy
    volumes:
      - ./whiskey_inventory.1.oas.yml:/tmp/whiskey_inventory.1.oas.yml:ro
    command: >
      run
      --base-url=http://prism:4010
      /tmp/whiskey_inventory.1.oas.yml
```

In the output you will see a number of requests against prism and finally, if all is well, you will get a schemathesis report stating all is well.

![Schemathesis Summary]({{ site.baseurl }}/assets/2024-12-22-create-a-cracker-of-an-open-api-contract-with-vs-code-spectral-prism-and-schemathesis/schemathesis_summary.PNG)

All of this linting and dynamic mock testing I thought would be a good basis for approving an API contract as part of a pre-commit and likely CI stage. Its all in docker compose so can be easily integrated into a pipeline. Hopefully will all these checks in place you'll end up with a **cracking API contract**!

## What Next?

### Intgerating with Pre-Commit and CI

Seen as the method used here to carry out all the checks is using a `docker compose up` command, it should be relatively trivial now to add this to a pre-commit githook or CI pipeline. I hope to extract some of the variables into environment variables so I can reuse the solution and customise it for different contracts.

### Changelogs

I'll want to investigate tools like [oasdiff](https://www.oasdiff.com/){:target="\_blank"} to generate changelogs based on the contract. It looks like this also identifies breaking changes which will be really useful.

### Mocking and Testing Tools

I have already started down this rabbit hole which is why I reeled myself in and focused on the process so I could get something working. Any of the tools can be swapped in and out as benefits or drawbacks are found. I am particularly interested in stateful mocks to provide a more realistic experience for consumers. I'll likely look at tools that have asyncpi support too. The following are a good starting point for investigation:

- [Specmatic](https://specmatic.io/){:target="\_blank"}
- [Microcks](https://microcks.io/){:target="\_blank"}
- [Mockoon](https://mockoon.com/){:target="\_blank"}

But there are many more (e.g. [Top API Mocking tools](https://speedscale.com/blog/api-mocking-tools/){:target="\_blank"}).

### The Role of Artificial Intelligence

Initially this was going to be a post about using AI to generate API contracts. For example there already is an [open api GPT](https://chatgpt.com/g/g-gQ0FMGHmb-openapi-gpt){:target="\_blank"} that can be used, as well as obviously [copilot](https://code.visualstudio.com/docs/copilot/overview){:target="\_blank"} within vs code. I started this approach by bringing the context from the feature file we created in requirements, but found I had to rework a lot of the contract anyway. The specific linting provided to me by spectral and error lens was far better than iterating against AI at this point. Also I found it important that I understood the contract specitication deeply as it helped my understand the behaviour I was building. I think AI is useful in this process but is no substitiute for understanding the OpenAPI contract and the behaviour you need to create. Once the contract is in place however based on good requirements, code generation from AI will likely be a very useful tool (althought codegen is another area I need to explore as there might be more specific tooling).

### Hosting Contracts

I need to make a decision on hosting contracts somewhere and being able to apply this process to them from a central source of truth for the API. This will be for both publishers to implement and test, and consumers to be able to accurately mock from. Options so far are:

- [Docusaurus](https://docusaurus.io/){:target="\_blank"} - leveraging the [open api plugin](https://github.com/PaloAltoNetworks/docusaurus-openapi-docs)
- [Event catalog](https://www.eventcatalog.dev/){:target="\_blank"}
- [Swaggerhub](https://swagger.io/tools/swaggerhub/){:target="\_blank"}

So many choices and many rabbit holes will be explored!

Have a merry christmas all!
