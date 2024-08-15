---
title: "Protecting Code Quality with Trunk.io"
date: 2024-08-15
author: dataGriff
description: "Protecting Code Quality with Trunk.io"
image:
  path: /workspace/datagriff/docs/assets/2024-08-15-protecting-code-quality-with-trunk.io/link.png
tags: Git VSCode Trunk.io
---

I recently went down a rabbit hole of [VS code extensions](https://www.freecodecamp.org/news/best-vscode-extensions/){:target="\_blank"} and whilst doing some extension exploration of my own I came across one that looked interesting called [trunk](https://marketplace.visualstudio.com/items?itemName=Trunk.io){:target="\_blank"}. I mused that this could help me with [trunk based development](https://www.thoughtworks.com/en-gb/insights/blog/enabling-trunk-based-development-deployment-pipelines){:target="\_blank"} along with my consistently poor data quality (what can I say, I am a fairly lazy hungovercoder). I quickly became intoxicated with everything that [trunk.io](https://trunk.io/){:target="\_blank"} had to offer and integrated it into my workflow to easily protect my code quality before committing to main!

- [Pre-Requisites](#pre-requisites)
- [What is Trunk?](#what-is-trunk)
- [Create Trunk Account](#create-trunk-account)
- [Initialise Trunk](#initialise-trunk)
- [Code Quality](#code-quality)
  - [Create some Bad Example Code](#create-some-bad-example-code)
  - [Trunk Check](#trunk-check)
  - [Trunk Format](#trunk-format)
- [Enable Precommits](#enable-precommits)
- [New Gitworkflow](#new-gitworkflow)
- [Mega Tidy Commit Example](#mega-tidy-commit-example)

## Pre-Requisites

- [Github Account](https://github.com/){:target="\_blank"}
- [Git](https://git-scm.com/downloads){:target="\_blank"}
- [VS Code](https://code.visualstudio.com/download){:target="\_blank"}

As always I will be using the mighty [gitpod](https://gitpod.io){:target="\_blank"} so I won't need to configure anything other than spinning up a workspace.

## What is Trunk?

[Trunk](https://trunk.io/) is the best thing in the world for lazy and terrified developers like myself who still want to ship code as fast and easily as possible. The focus is on developer experience and automating those aspects you know are important but can often get overlooked as you race to the finish line. Their four main products are as follows:

- **[Code Quality](https://trunk.io/code-quality){:target="\_blank"}**: This is the first and last code linter you will ever need. The code quality product leverages linters already available and automatically adds them to your code base when you install trunk. The whole trunk approach is **configurable with a yaml file. The code quality aspect is what I will be focused on in this blog.
- **[Merge Queue](https://trunk.io/merge-queue){:target="\_blank"}**: 
- **[CI Analytics](https://trunk.io/ci-analytics){:target="\_blank}"**: 
- **[Flaky Tests](https://trunk.io/flaky-tests){:target="\_blank"}**: 

If I could play with all of these trunk toys right now I would. Watch this space for more experimentation in between meals. Now to get started with Trunk and code quality...

## Create Trunk Account

First sign-up to [Trunk](https://trunk.io/){:target="\_blank"} at [app.trunk.io](https://app.trunk.io/){:target="\_blank"}. If you're concerned about costs dear not as they offer a [free tier](https://trunk.io/pricing)[Trunk](https://trunk.io/){:target="\_blank"} which is unlimited on public repos and free for up to five committers on private repos (thank you [Trunk](https://trunk.io/){:target="\_blank"}!).  

![Trunk Welcome]({ site.baseurl }/assets/date_blog/trunk_welcome.PNG)

## Initialise Trunk

To initialise trunk you first need to install the CLI as per the docs by running the below.

```bash
curl https://get.trunk.io -fsSL | bash -s -- -y
trunk upgrade
```

## Code Quality

### Create some Bad Example Code

I found this particularly easy 

### Trunk Check

### Trunk Format

## Enable Precommits

## New Gitworkflow

## Mega Tidy Commit Example

I first installed trunk on my datagriff blog and it is here that I had that first "wow" moment of how powerful trunk could be in doing a big tidy up of my code in the real world. Here is the link to the commit and also a screenshot below showing how much of the code, and images, it brought up to standard for me. I am highly likely going to be embedded trunk in all my workflows and adding as a standard to my gitpod configuration files. Sweet sweet code protection is just what a gung-ho, lazy and terrified hungovercoder needs!
