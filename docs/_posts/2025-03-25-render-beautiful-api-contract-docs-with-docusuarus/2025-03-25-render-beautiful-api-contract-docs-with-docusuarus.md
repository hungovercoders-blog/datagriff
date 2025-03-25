---
title: "Render Beautiful API Contract Docs with Docusuarus"
date: 2025-03-25
author: dataGriff
description: "Render Beautiful API Contract Docs with Docusuarus"
image:
  path: assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/link.png
tags: API Docusaurus
---

Its been far too long again and I need to share with you more about my contracts obsession. Starting with how to make API contracts aesthetically pleasing with code examples using [Docusaurus](https://docusaurus.io/){:target="\_blank"} and the [openapi plugin](https://github.com/PaloAltoNetworks/docusaurus-openapi-docs){:target="\_blank"}. If you simply can't wait to see how pretty these are before you invest anytime, skip to the [Final Docs in Live Site](#final-docs-in-live-site) section.

- [Pre-Requisites](#pre-requisites)
- [Directory Layout](#directory-layout)
- [Add API Contract](#add-api-contract)
- [Configure Docusuarus for API Doc Generation](#configure-docusuarus-for-api-doc-generation)
  - [Configure Docusaurus Config File](#configure-docusaurus-config-file)
  - [Configure Sidebar](#configure-sidebar)
- [Generate API Docs](#generate-api-docs)
- [Resolving Issues](#resolving-issues)
- [Code Examples](#code-examples)
- [Final Docs in Live Site](#final-docs-in-live-site)
- [Next Steps](#next-steps)

## Pre-Requisites

- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}
- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [See my previous post on setting up a docusaurus website](https://blog.hungovercoders.com/datagriff/2024/12/02/deploy-docusaurus-on-azure-static-web-apps.html){:target="\_blank"}

As always I will be using the mighty [gitpod](https://gitpod.io){:target="\_blank"} so I won't need to configure anything other than spinning up the default workspace.

## Directory Layout

If you've setup [Docusaurus](https://docusaurus.io/){:target="\_blank"} like in my [previous post](https://blog.hungovercoders.com/datagriff/2024/12/02/deploy-docusaurus-on-azure-static-web-apps.html){:target="\_blank"}, you should have a root directory layout that looks something like this:

```txt
.github/
.vscode/
www/
  .docusaurus/
  blog/
  build/
  docs/
  node_modules/
  src/
  static/
gitpod.yml
package-lock.json
README.md
```

We're going to leverage the static folder with a new directory called "contracts" to store our API contracts. This will also be where we store our other contracts in the future such as data contracts or asyncapi contracts. I decided to take the domain approach as the parent directory so domains are clustered together with their contracts rather than separating them out by function first. Our future static directory structure will therefore look something like the following:

```txt
static/
  contracts/
    whiskey/
      api/
        v1/
          whiskey.oas.1.0.yml
      events/
        v1/
          whiskey.async.1.0.yaml
      data/
        v1/
          whiskey.datacontract.1.0.yml
```

For now we will be focusing purely on the API contracts but I will be adding the other contract types in future posts.

## Add API Contract

In the static/contracts/whiskey/api/v1/ directory add a file called whiskey.oas.1.0.yml with the following content:

```yaml
openapi: 3.0.1
security:
  - basicAuth: []
info:
  title: Whiskey API
  description: |
    ## Whiskey API

    This is the whiskey API provided by Hungovercoders.

    ![Hungovercoders](https://www.hungovercoders.com/assets/logo3.ico)

  version: "1.0"
tags:
  - name: whiskey
    description: Whiskey operations
servers:
  - url: https://api.example.com/v1
    description: Production server (uses live data)
  - url: https://sandbox-api.example.com:8443/v1
    description: Sandbox server (uses test data)
paths:
  /whiskeys:
    get:
      summary: Get all whiskeys
      operationId: getAllWhiskeys
      tags:
        - whiskey
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                type: array
                maxItems: 100
                items:
                  $ref: "#/components/schemas/Whiskey"
        "500":
          description: Server Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Server Error
    post:
      summary: Add a new whiskey
      operationId: addWhiskey
      tags:
        - whiskey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: "#/components/schemas/Whiskey"
      responses:
        "201":
          description: Created
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Whiskey"
          links:
            GetWhiskey:
              operationId: getAWhiskey
              parameters:
                id: $response.body#/id
        "400":
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid input
        "500":
          description: Server Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Server Error
  /whiskeys/{id}:
    get:
      summary: Get a specific whiskey
      operationId: getAWhiskey
      tags:
        - whiskey
      parameters:
        - name: id
          in: path
          description: The ID of the whiskey to retrieve
          required: true
          schema:
            type: string
      responses:
        "200":
          description: OK
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Whiskey"
        "400":
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid ID supplied
        "404":
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Whiskey not found
        "500":
          description: Server Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Server Error
        default:
          description: Non-specific HTTP response code
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
    delete:
      summary: Delete a specific whiskey
      operationId: deleteAWhiskey
      tags:
        - whiskey
      parameters:
        - name: id
          in: path
          description: The ID of the whiskey to delete
          required: true
          schema:
            type: string
      responses:
        "204":
          description: No Content
        "400":
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Invalid ID supplied
        "404":
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Whiskey not found
        "500":
          description: Server Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    example: Server Error
        default:
          description: Non-specific HTTP response code
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"

components:
  schemas:
    Whiskey:
      x-tags:
        - whiskey
      title: Whiskey
      description: A whiskey object
      type: object
      properties:
        id:
          type: string
        name:
          type: string
          minLength: 1
          maxLength: 50
        age:
          type: integer
          format: int32
          minimum: 3
          maximum: 200
        abv:
          type: number
          format: percent
          minimum: 0
          maximum: 92
        distillery:
          type: string
          minLength: 1
          maxLength: 50
        type:
          type: string
          enum:
            - Single Malt
            - Blended
            - Bourbon
            - Rye
            - Corn
            - Wheat
            - Other
        country:
          type: string
          enum:
            - Scotland
            - Ireland
            - USA
            - Canada
            - Japan
            - Wales
            - England
            - India
            - Australia
            - Other
      additionalProperties: false
    Error:
      type: object
      required:
        - code
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    apiKey:
      description: API Key
      type: apiKey
      name: api-key
      in: header
    basicAuth:
      description: Basic Authentication
      type: http
      scheme: basic
```

## Configure Docusuarus for API Doc Generation

Next the fun bit to render these documents beautifully in docusaurus using this awesome [openapi plugin](https://github.com/PaloAltoNetworks/docusaurus-openapi-docs){:target="\_blank"}. You can follow the documentation on the plugin page but I'll give you a quick start guide here.

First install the plugin:

```bash
yarn add docusaurus-plugin-openapi-docs
```

Then install the theme:

```bash
yarn add docusaurus-theme-openapi-docs
```

You should then see the following in your package.json:

```json
    "docusaurus-plugin-openapi-docs": "^4.3.7",
    "docusaurus-theme-openapi-docs": "^4.3.7",
```

To see the latest dependency matrix for the open api docs go [here](https://github.com/PaloAltoNetworks/docusaurus-openapi-docs#compatibility-matrix){:target="\_blank"}. As long as your docusaurus version and open api docs version are compatible you should be good to go.

### Configure Docusaurus Config File

This bit tripped me up a few times and luckily I realised I could use the [docusaurus-openapi-template](https://github.com/PaloAltoNetworks/docusaurus-template-openapi-docs/blob/main/docusaurus.config.ts){:target="\_blank"} as a good reference point.

Add the plugin to your docusaurus.config.ts or docusaurus.config.js file:

```js
plugins: [
  [ require.resolve('docusaurus-lunr-search'), {
    languages: ['en', 'de'] // language codes
  }],
  [
    "docusaurus-plugin-openapi-docs",
    {
      id: "openapi",
      docsPluginId: "classic",
      config: {
          whiskey: {
            specPath: "static/contracts/whiskey/api/v1/whiskey.oas.1.0.yml",
            outputDir: "docs/whiskey/api/v1",
            downloadUrl:
              "../../contracts/whiskey/api/v1/whiskey.oas.1.0.yml",
            sidebarOptions: {
              groupPathsBy: "tag",
              categoryLinkSource: "tag",
            },
        } satisfies OpenApiPlugin.Options,
      } satisfies Plugin.PluginOptions,
    },
  ],
],

themes: ["docusaurus-theme-openapi-docs"],
```

Ensure that your export default is set to the following:

```ts
export default async function createConfig() {
  return config;
}
```

Ensure that the following imports are added to the top of your docusaurus.config.ts or docusaurus.config.js file:

```ts
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import type * as OpenApiPlugin from "docusaurus-plugin-openapi-docs";
import type * as Plugin from "@docusaurus/types/src/plugin";
}
```

Ensure that whiskey is added to your navbar as per the below:

```ts
  themeConfig: {
    // Replace with your project's social card
    image: 'img/hungovercoders.png',
    navbar: {
      title: 'Hungovercoders',
      logo: {
        alt: 'My Site Logo',
        src: 'img/hungovercoders.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Tutorial',
        },
        {
          type: 'docSidebar',
          sidebarId: 'whiskeySidebar',
          position: 'left',
          label: 'Whiskey',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/hungovercoders/hungovercoders',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
```

### Configure Sidebar

Ensure that whiskey is added to your sidebar.ts or sidebar.js as well:

```ts
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [{type: 'autogenerated', dirName: 'tutorial'}],
  whiskeySidebar: [{type: 'autogenerated', dirName: 'whiskey'}],
```

## Generate API Docs

Using the following command generate the API docs:

```bash
yarn docusaurus gen-api-docs all
```

These will appear under the /docs/whiskey/api/v1/ directory of your docusaurus website.

```txt
docs/
  whiskey/
    api/
      v1/
        *.mdx
```

![Whiskey MDX Files]({{ site.baseurl }}/assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/docusaurus_whiskey_mdx_directory.PNG)

These mdx files will be the rendered API documentation for your API contract.

If you then run:

```bash
npm start
```

To run your website you will see the whiskey sidebar...

![Whiskey Sidebar]({{ site.baseurl }}/assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/docusaurus_whiskey_sidebar.PNG)

And the stunning API docs 😍

![Whiskey API Docs]({{ site.baseurl }}/assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/docusaurus_whiskey_api.PNG)

## Resolving Issues

If you do get issues with any of the above (which I did on occasion) make sure you try some of the following:

- Revisit the [docusaurus-openapi-template](https://github.com/PaloAltoNetworks/docusaurus-template-openapi-docs/blob/main/docusaurus.config.ts){:target="\_blank"} for reference
- Check the [compatibility matrix](https://github.com/PaloAltoNetworks/docusaurus-openapi-docs#compatibility-matrix){:target="\_blank"} for docusaurus vs the open api docs and ensure they match
- Check out any [open issues](https://github.com/PaloAltoNetworks/docusaurus-openapi-docs/issues){:target="\_blank"} on the docusaurus open api github page
- Try stopping and starting you app again

## Code Examples

One of the coolest things about this plugin is that it renders the code examples for you. This is a great way to ensure that your API contract is up to date and that the code examples are correct. It also means that you can easily copy and paste the code examples into your codebase.

![Whiskey Code Docs Standard]({{ site.baseurl }}/assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/docusaurus_api_example01.PNG)

I found that in order to render some themes correctly I also had to add this code to the prism section of the docusaurus.config.ts or docusaurus.config.js file:

```ts
    prism: {
       additionalLanguages: [
         "csharp",
       ],
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
```

If I didn't do this for example the csharp code examples would not render correctly in the theme I wanted. This only works for some languages. You can see below that the github theme makes the code example look far nicer now.

![Whiskey Code Docs Theme]({{ site.baseurl }}/assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/docusaurus_api_example02.PNG)

And of course I utilise the dracula theme for dark mode!

![Whiskey Code Docs Dark Theme]({{ site.baseurl }}/assets/2025-03-25-render-beautiful-api-contract-docs-with-docusuarus/docusaurus_whiskey_api_dark.PNG)

## Final Docs in Live Site

These are all work in progress but I am utilising these open api docs in both the [hungovercoders](https://docs.hungovercoders.com){:target="\_blank"} website and my new [dogusaurus](https://www.dogusaurus.com/){:target="\_blank"} website, which I aim to be a documentation website for multiple dog related projects!

## Next Steps

I will continue building both my [hungovercoders](https://docs.hungovercoders.com){:target="\_blank"} and [dogusaurus](https://www.dogusaurus.com/){:target="\_blank"} websites and will be adding more contracts to them. I want to add some automated spectral linting to the contracts and add some pre commit hooks as well as some CI/CD pipelines to ensure that the contracts are valid according to best practice and my own rules. I'd also like to potentially serve an API from my azure static website that will simply pass the raw api contracts when requested to make it easier for them to download. I'll also want to look at better methods of versioning which I think is also provided by the open api plugin.

I'll also be adding more contract types such as [data contracts](https://datacontract.com/) and [asyncapi contracts](https://www.asyncapi.com/) to the static/contracts directory and will be rendering them in the same way as the API contracts. I'm really keen on trying some [jinja templates](https://jinja.palletsprojects.com/en/stable/){:target="\_blank"} to make data contracts render in MDX so I can host them in my docusaurus websites too. Exciting times!
