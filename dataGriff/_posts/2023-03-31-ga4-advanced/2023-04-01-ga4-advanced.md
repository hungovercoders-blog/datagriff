---
title: "Advanced Quick Start for Google Analytics 4 Using GTM"
date: 2023-04-01

author: dataGriff
---

We learned how to stumble our way into a google analytics setup in our last blog post, but what if we want to add extra data? What if we want to understand if our website is converting??? Lets dive deeper into leveraging google analytics, GTM and some data layer shenanigans to leverage some awesome insights!

## Pre-Requisites

You're going to need a website, a [google account](https://myaccount.google.com/) so that you can leverage [google analytics](https://analytics.google.com/analytics/web/)  and [google tag manager](https://tagmanager.google.com/). I recommend this previous post for a [quickstart](https://www.hungovercoders.com/blog/datagriff/2023/03/27/ga4-gtm-quickstart.html) if you're coming in cold!

## Adding a Custom Dimension to GA4 with the Data Layer

First make some data available in the data layer and add it as a GTM variable. To do this follow the methods in this [blog post](https://www.hungovercoders.com/blog/datagriff/2023/02/27/data-layer.html). We can then add this is a dimension in our google analytics to analyse.

In your google analytics container go to your property, then go to admin, then custom definitions. Create a new custom dimension here with the parameter name that matches the data layer variable name you setup in GTM.

### Monitor Dimension in GA4

## Adding a Custom Event

### Turn Event into Conversion

### Monitor Conversion in GA4

## Create an Audience

### Trigger Event For Member Added

## Synch to Big Query