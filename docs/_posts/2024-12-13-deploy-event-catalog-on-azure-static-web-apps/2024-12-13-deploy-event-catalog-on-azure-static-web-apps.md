---
title: "Deploy Event Catalog on Azure Static Web Apps"
date: 2024-12-13
author: dataGriff
description: "Deploy Event Catalog on Azure Static Web Apps"
image:
  path: assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/link.png
tags: Azure Event Catalog
---

This blog is a bit of a cheat as its pretty much the same as my [previous post](https://blog.hungoveercoders.com/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/){:target="\_blank"} but this time I am deploying the [event catalog](https://www.eventcatalog.dev/){:target="\_blank"} website to [Azure Static Web Apps](https://docs.microsoft.com/en-us/azure/static-web-apps/overview){:target="\_blank"} using the [vs code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps){:target="\_blank"}. Below is how to create the template event catalog website and deploy it to azure static web apps.

- [Pre-Requisites](#pre-requisites)
- [Event Catlog Start](#event-catlog-start)
- [Deploy Azure Static Webapp](#deploy-azure-static-webapp)
- [Adding a Gitpod Configuration File](#adding-a-gitpod-configuration-file)
- [Custom Domain - Events.Hungovercoders](#custom-domain---eventshungovercoders)

## Pre-Requisites

- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}
- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [Azure Account](https://www.portal.azure.com){:target="\_blank"}
- [Visual Studio Code Azure Static Web App Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps){:target="\_blank"}

As always I will be using the mighty [gitpod](https://gitpod.io){:target="\_blank"} so I won't need to configure anything other than spinning up a workspace.

## Event Catlog Start

Create a new github repository and call it something appropriate for your website, or call it "eventcatalog" if you are just experimenting. Open your repository using gitpod by either appending `https://gitpod.io/#` to the start of your repository url or by clicking the gitpod button in the top right of your repository page. The [gitpod default image](https://www.gitpod.io/docs/configure/workspaces/workspace-image){:target="\_blank"} comes with nodejs and npm installed so you can then start developing straight away.

![Gitpod Open]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/gitpod_open.PNG)

Once this has opened, run the following command to install docusaurus and create the new project:

```bash
npx @eventcatalog/create-eventcatalog@latest www
```

Set your organisation name when prompted and then press enter.

![Event Catalog Install]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_install.PNG)

This will take a little while and will create a new event catalog project in the `www` folder.

![Event Catalog Installed]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_installed.PNG)

Change into the `www` folder and run the following to start the development server:

```bash
cd www
npm run dev
```

You will see the development site running at [http://localhost:3000](http://localhost:3000) once the command completes.

![Event Catalog Start]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_start.PNG)

Now you have the basic event catalog site running that you can start developing against.

![Event Catalog Started]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_started.PNG)

The cool thing about event catalog is if you make a change then the site will automatically reload with the new changes.

![Event Catalog Reload]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_reload.gif)

## Deploy Azure Static Webapp

First ensure all your most recent changes are committed and pushed to your repository. You can run git status to confirm everything is up to date.

```bash
git status
```

![Git Status]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/git_status.PNG)

Now press CTRL + SHIFT + P to open the command palette and type "Azure Static Web Apps: Create New Static Web App" and press enter. You then just have to set the following:

- Choose the subscription you want to use
- Choose the region
- Choose the name of the azure static web app

![Azure Static Web App]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_static_web_app.gif)

The extension will then create a new github action in your repository under the .github/workflows directory which will automatically deploy your site to azure static web apps whenever you push to the main branch. If you now push to the main branch you should see a github action start running which will deploy your site to azure static web apps.

![Github Action]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/github_action.PNG)

You can then go into azure and see your new static web app running.

![Azure Event Catalog]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/azure_event_catalog.PNG)

If you click on the URL you will see your new event catalog site running in azure static web apps! How quick was that!

![Azure Event Catalog Site]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/azure_event_catalog_site.PNG)

## Adding a Gitpod Configuration File

To ensure that your can quickly run your docusaurus site whenever you open your project in gitpod, you can add a `.gitpod.yml` file to the root of your repository with the following content:

```yaml
tasks:
  - init: |
      cd www
      npm install && npm run build
    command: npm start

vscode:
  extensions:
    - dracula-theme.theme-dracula
    - 42Crunch.vscode-openapi
    - asyncapi.asyncapi-preview
    - xyc.vscode-mdx-preview
    - unifiedjs.vscode-mdx
    - ms-azuretools.vscode-azurestaticwebapp
    - github.vscode-github-actions
    - usernamehw.errorlens
    - oderwat.indent-rainbow
```

This will ensure that npm install and build are done as part of a pre-requisite to the workspace starting, then it will run `npm start` so that your event catalog site will always open on startup. Note I have also added some extensions which will make my life easier going forwards! You can now open your repository in gitpod and your event ctalog site will automatically start running. To make it even faster I also recommend configuring a gitpod pre-build that will ensure your development workspace is ready to go as soon as you open it.

## Custom Domain - Events.Hungovercoders

I decided to keep my event catalog close to my hungovercoders domain and I am going to host event catalog on [events.hungovercoders.com](https://events.hungovercoders.com){:target="\_blank"}.

First copy the unique url from your azure static website in the azure portal.

![Azure Unique URL]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/azure_unique_url.PNG)

Then create a new cname record in your domain provider and set the value to be the unique url from azure.

![Domain Name Namecheap]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/domain_name_namecheap.PNG)

Then add a custom domain in in the azure static webapp.

![Domain Name Azure Address]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_azure_add_custom_domain.PNG)

Make sure you enter your custom domain address when creating.

![Domain Name Azure]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/event_catalog_azure_add_custom_domain_3.PNG)

Then voila! You have your docusaurus site running on a custom domain!

![Custom Domain Running]({{ site.baseurl }}/assets/2024-12-13-deploy-event-catalog-on-azure-static-web-apps/custom_domain_running.PNG)
