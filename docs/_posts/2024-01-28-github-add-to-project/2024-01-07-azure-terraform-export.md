---
title: "Automating Adding Issues to Github Projects"
date: 2024-01-28
author: dataGriff
description: Automating Adding Issues to Github Projects
image:
  path: /assets/2024-01-28-github-add-to-project/link.png
tags: Github
---

Being a hungover coder it can be difficult to remember all the ideas you've had or which ones you are currently working on... I've therefore invested in [github projects](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/quickstart-for-projects) and organised all my work (at least for now). One of the constraints of the github projects is that even if you link a repo, the issues or bugs are not automatically added to your project board. Below are three ways to ensure issues are automatically added to the board of your choosing!

- [Prerequisites](#prerequisites)
- [Hungovercoders Github Template](#hungovercoders-github-template)
- [Linking a Repo to a Project](#linking-a-repo-to-a-project)
- [Method 1: Project Automation](#method-1-project-automation)
- [Method 2: Template Issues and Bugs](#method-2-template-issues-and-bugs)
- [Method 3: Github Actions](#method-3-github-actions)

## Prerequisites

- [Github](https://github.com/){:target="_blank"} - To utilise any of the tips below you're going to want to be working in github.

## Hungovercoders Github Template

A lot of the exploration work I carry out for hungovercoders I now carry out in this [template.github.platform](https://github.com/hungovercoders/template.github.platform) repository. It allows me to experiment and test practices before I roll them out to other projects. Keep an eye on this repo for cheatsheets and automation that you can leverage across your github repositories, including the ones from this blog post.

## Linking a Repo to a Project

The first thing I did was link a github project to a repo as per the screenshot below.

This however does not mean that issues raised automatically get added to that project board - it appears to be just a nice link. This led me on to the three methods described below to ensure the issues raised from the repo landed on the board that I wanted.

## Method 1: Project Automation

The official method to ensure issues are added to your project is to use the project workflows now available, in particular the "auto-add to project". 

I tried this first but then quickly found out you could only do one repository at a time and there is a limit of 5 workflows per project(!). This wasn't going to be sustainable so I looked elsewhere. I am currently keeping an eye on this issue which may completely negate the need for the below, but in the meantime...

## Method 2: Template Issues and Bugs

I found that you could create template issues, pull requests and bugs in your repository by placing them in the .github/ISSUE_TEMPLATE directory. You can see some examples in the hungover coders github template repo [here](https://github.com/hungovercoders/template.github.platform/tree/main/.github/ISSUE_TEMPLATE). These will then appear under your issues area of that repository as quickstarts for desired input.

The markdown style, whilst more intuitive, does not support automated project linkage, but the yaml files do. Therefore if you create something like this:

Then leverage this yaml based template to create the desired ticket, that will automatically link to the project you state.

However... If anyone still creates a vanilla issue it will not link tot he project you want and be work visible where you need it to be! I am also a big fan of the github app where I want to raise issues quickly on the go and it only supports standard issues without leaving to go to the browser for the templates. I therefore did some googling, maybe some chatgpt-ing, I can't remember anymore and discovered the solution in the next section.

## Method 3: Github Actions

The catch-all method of ensuring that any issue raised lands on the board of your choice is to leverage a github action. The action code can be found in the hungovercoders template [here]() and can also be seen below.

Rather than hardcode the project in the action, as I will likely have this action in a number of places, I have setup global variables for team project URLs like this:

The PAT token I generated from my own user and placed that as an organisation level secret. 

Whenever I raise an issue now on a repo (even from the mobile app!) that has this workflow installed, it will kick off that action and ensure the issue is assigned to the project you have chosen. No more forgetting of ideas now and all my work lands on the hungovercoders board. Victory!