---
title: "Deploying Containerised React App with Runtime Environment Variables"
date: 2024-03-31
author: dataGriff
description: Deploying Containerised React App with Runtime Environment Variables
image:
  path: /assets/2024-04-21-container-react-runtime-variables/link.png
tags: React Docker Azure Containers Terraform
---

React is a fickle beast when it comes to runtime environment variables and after visiting some of the distilleries on [whiskey.hungovercoders.com](whiskey.hungovercoders.com) it becomes an even trickier prospect to handle. My goal was to ensure that I could reference the appropriate API url for each react application in each environment as I deployed them with terraform in Azure container apps. After reading this extremely help [post](https://www.freecodecamp.org/news/how-to-implement-runtime-environment-variables-with-create-react-app-docker-and-nginx-7f9d42a91d70/) from the awesome [freecodecamp.org](https://www.freecodecamp.org/), that did all the work for me, and then adding a little of my own brand hungovercoding, the outcome was a success!

## Pre-Requisites

## Containerised React App

## React Runtime Environment Variables

## Deploying Dynamic API URL Runtime Variable with Terraform