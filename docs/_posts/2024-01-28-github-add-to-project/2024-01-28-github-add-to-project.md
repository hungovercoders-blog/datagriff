---
title: "Automating Adding Issues to Github Projects"
date: 2024-01-28
author: dataGriff
description: Automating Adding Issues to Github Projects
image:
  path: /assets/2024-01-28-github-add-to-project/link.png
tags: Github
---

Being a hungover coder it can be difficult to remember all the ideas you've had or which ones you are currently working on... I've therefore invested in [github projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects){:target="_blank"} and organised all my work (at least for now). One of the constraints of the github projects is that even if you link a repo, the issues or bugs are not automatically added to your project board. Below are three ways to ensure issues are automatically added to the board of your choosing!

- [Prerequisites](#prerequisites)
- [Hungovercoders Github Template](#hungovercoders-github-template)
- [Linking a Repo to a Project](#linking-a-repo-to-a-project)
- [Method 1: Project Automation](#method-1-project-automation)
- [Method 2: Template Issues and Bugs](#method-2-template-issues-and-bugs)
- [Method 3: Github Actions](#method-3-github-actions)

## Prerequisites

- [Github](https://github.com/){:target="_blank"} - To utilise any of the tips below you're going to want to be working in github.
- [Github Project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) - You'll want to setup a github project to collate all your work and make it visible. The hungovercoders team board can be seen below.

![Github Project]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/github_project.png)

## Hungovercoders Github Template

A lot of the exploration work I carry out for hungovercoders I now carry out in this [template.github.platform](https://github.com/hungovercoders/template.github.platform){:target="_blank"} repository. It allows me to experiment and test practices before I roll them out to other projects. Keep an eye on this repo for cheatsheets and automation that you can leverage across your github repositories, including the ones from this blog post.

## Linking a Repo to a Project

The first thing I did was link a github project to a repo as per the screenshot below.

![Project Link]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/project_link.png)

This however does not mean that issues raised for that repo automatically get added to that project board - it appears to be just a nice link. This led me on to the three methods described below to ensure the issues raised from the repo landed on the board that I wanted.

## Method 1: Project Automation

The official method to ensure issues are added to your project is to use the project workflows now available, in particular the "auto-add to project".

![Project Automation]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/project_automation.png)

I tried this first but then quickly found out you could only do one repository at a time and there is a limit of 5 workflows per project(!). This wasn't going to be sustainable so I looked elsewhere...

## Method 2: Template Issues and Bugs

I found that you could create template issues, pull requests and bugs in your repository by placing them in the .github/ISSUE_TEMPLATE directory. You can see some examples in the hungover coders github template repo [here](https://github.com/hungovercoders/template.github.platform/tree/main/.github/ISSUE_TEMPLATE){:target="_blank"}. These will then appear under your issues area of that repository as quickstarts for desired input.

The markdown style, whilst more intuitive, does not support automated project linkage, but the yaml files do. Therefore if you create something like this as an issue.yml file in the ISSUE_TEMPLATE folder...

```yaml
name: Issue
description: Create an Issue
title: "[Issue]: "
labels: ["value", "cost","quality","happy"]
projects: ["hungovercoders/5"]
assignees:
  - self
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to raise this issue!

  - type: textarea
    id: what-happened
    attributes:
      label: What happened?
      description: Also tell us, what did you expect to happen?
      placeholder: Tell us what you see!
      value: "An idea happened!"
    validations:
      required: true
```

Then leverage this yaml based template to create the desired ticket, that will automatically link to the project you state.

![Template Usage]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/template_usage.png)

However... If anyone still creates a vanilla issue it will not link tot he project you want and work be visible where you need it to be! I am also a big fan of the [github mobile app](https://github.com/mobile){:target="_blank"} where I want to raise issues quickly on the go and it only supports standard issues without leaving to go to the browser for the templates. I therefore did some googling, maybe some chatgpt-ing, I can't remember anymore and discovered the solution in the next section.

## Method 3: Github Actions

The catch-all method of ensuring that any issue raised lands on the board of your choice is to leverage the [add to project github action](https://github.com/actions/add-to-project){:target="_blank"}. The action code can be found in the hungovercoders template [here](https://github.com/hungovercoders/template.github.platform/blob/main/.github/workflows/add-to-project.yml){:target="_blank"} and can also be seen below.

```yaml
name: Add Issues to Project

on:
  issues:
    types:
      - opened

jobs:
  add-to-project:
    name: Add issue to project
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.4.1
        with:
          # You can target a project in a different organization
          # to the issue
          project-url: ${{ vars.TEMPLATE_TEAM_PROJECT }}
          github-token: ${{ secrets.WORK_MANAGEMENT }}
```

Rather than hardcode the project in the action, as I will likely have this action in a number of places, you can see I have setup github global variables for the team project URLs so its easier for me to change in one place if I need to.

![Github Variables]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/github_variables.png)

The PAT token I generated from my own user and placed that as an organisation level secret.

![Github Secrets]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/github_secrets.png)

Whenever I raise an issue now on a repo (even from the mobile app!) that has this workflow installed, from any github account I might add, it will kick off that action and ensure the issue is assigned to the project you have chosen. No more forgetting of ideas now and all my work lands on the hungovercoders board. Victory! (I may have to keep an eye on action minutes but it takes a few seconds to run so should be ok...)

![Github Action]({{ site.baseurl }}/assets/2024-01-28-github-add-to-project/github_action.png)