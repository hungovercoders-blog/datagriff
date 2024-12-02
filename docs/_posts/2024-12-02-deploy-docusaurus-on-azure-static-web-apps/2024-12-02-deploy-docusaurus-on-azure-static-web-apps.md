---
title: "Deploy docusaurus on Azure Static Web Apps"
date: 2024-12-02
author: dataGriff
description: "Deploy docusaurus on Azure Static Web Apps"
image:
  path: assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/link.png
tags: Azure Docusuaurus
---

I've been meaning to move the hungovercoders website over to [docusaurus](https://docusaurus.io/){:target="\_blank"} for a while after seeing it as the basis for [event catalog](https://www.eventcatalog.dev/){:target="\_blank"} among other [cool community shared demos](https://docusaurus.io/showcase){:target="\_blank"}. Whilst experimenting I found how easy it was to deploy to [Azure Static Web Apps](https://docs.microsoft.com/en-us/azure/static-web-apps/overview){:target="\_blank"} using the [vs code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps){:target="\_blank"}. Below is how to create the template docusaurus website and deploy it to azure static web apps.

- [Pre-Requisites](#pre-requisites)
- [Docusaurus Start](#docusaurus-start)
- [Deploy Azure Static Webapp](#deploy-azure-static-webapp)
- [Adding a Gitpod Configuration File](#adding-a-gitpod-configuration-file)
- [Custom Domain - Dogusaurus](#custom-domain---dogusaurus)

## Pre-Requisites

- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}
- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [Azure Account](https://www.portal.azure.com){:target="\_blank"}
- [Visual Studio Code Azure Static Web App Extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-azurestaticwebapps){:target="\_blank"}

As always I will be using the mighty [gitpod](https://gitpod.io){:target="\_blank"} so I won't need to configure anything other than spinning up a workspace.

## Docusaurus Start

Create a new github repository and call it something appropriate for your website, or call it "docusaurus" if you are just experimenting. Open your repository using gitpod by either appending `https://gitpod.io/#` to the start of your repository url or by clicking the gitpod button in the top right of your repository page. The [gitpod default image](https://www.gitpod.io/docs/configure/workspaces/workspace-image){:target="\_blank"} comes with nodejs and npm installed so you can then start developing straight away.

![Gitpod Open]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/gitpod_open.PNG)

Once this has opened, run the following command to install docusaurus and create the new project:

```bash
npx create-docusaurus@latest www classic
```

I chose typescript for the language but you can choose javascript if you prefer.

![Docusaurus Install]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/docusaurus_install.PNG)

This will take a little while and will create a new docusaurus project in the `www` folder using the classic theme. Change into the `www` folder and run the following to start the development server:

```bash
cd www
npm start
```

You will see the development site running at [http://localhost:3000](http://localhost:3000).

![Docusaurus Start]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/docusaurus_start.PNG)

You now have the basic docusaurus site running that you can start developing against.

![Docusaurus Running]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/docusaurus_running.PNG)

The cool thing about docusaurus is if you make a change then the site will automatically reload with the new changes.

![Docusaurus Reload]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/docusaurus_reload.gif)

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

![Azure Static Web App]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/azure_static_web_app.gif)

The extension will then create a new github action in your repository under the .github/workflows directory which will automatically deploy your site to azure static web apps whenever you push to the main branch. If you now push to the main branch you should see a github action start running which will deploy your site to azure static web apps.

![Github Action]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/github_action.PNG)

You can then go into azure and see your new static web app running.

![Azure Docusaurus]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/azure_docusaurus.PNG)

If you click on the URL you will see your new docusaurus site running in azure static web apps! How quick was that!

![Azure Docusaurus Site]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/azure_docusaurus_site.PNG)

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

This will ensure that npm install and build are done as part of a pre-requisite to the workspace starting, then it will run `npm start` so that your docusaurus site will always open on startup. Note I have also added some extensions which will make my life easier going forwards! You can now open your repository in gitpod and your docusaurus site will automatically start running. To make it even fasterI also recommend configuring a gitpod pre-build that will ensure your development workspace is ready to go as soon as you open it.

## Custom Domain - Dogusaurus

I decided before moving my hungovercoders site over to docusaurus that I would experiment with a custom domain. I have a lot of SEO logic and process to transfer over! I chose [dogusaurus.com](https://www.dogusaurus.com){:target="\_blank"} as it was available and lines up with a few of the dog themed domain names I have been using for my projects. I followed the [instructions here](https://learn.microsoft.com/en-us/azure/static-web-apps/custom-domain-external){:target="\_blank"} to add the custom domain to my azure static web app. Its really easy and took about 10 minutes.

First copy the unique url from your azure static website in the azure portal.

![Azure Unique URL]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/azure_unique_url.PNG)

Then create a new cname record in your domain provider and set the value to be the unique url from azure.

![Domain Name Namecheap]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/domain_name_namecheap.PNG)

Then add a custom domain in in the azure static webapp.

![Domain Name Azure Address]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/domain_name_cname_azure_address.PNG)

Make sure you enter your custom domain address when creating.

![Domain Name Azure]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/domain_name_cname_azure.PNG)

Then voila! You have your docusaurus site running on a custom domain!

![Custom Domain Running]({{ site.baseurl }}/assets/2024-12-02-deploy-docusaurus-on-azure-static-web-apps/custom_domain_running.PNG)
