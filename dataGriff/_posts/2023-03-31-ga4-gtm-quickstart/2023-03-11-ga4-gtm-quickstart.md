---
title: "Quick Start for Google Analytics 4 Using GTM"
date: 2023-03-31

author: dataGriff
---

I want google analytics 4 on my website and I want it now. How else can I ensure that all the hungovercoders are learning all the best tech and finding their local breweries??

- [Pre-Requisites](#pre-requisites)
- [Why use Google Analytics 4?](#why-use-google-analytics-4)
- [Creating a GA Account, Property and Data Stream](#creating-a-ga-account-property-and-data-stream)
  - [Account](#account)
  - [Property](#property)
  - [Data Stream](#data-stream)
- [Using a GTM Container with Standard Tags](#using-a-gtm-container-with-standard-tags)
  - [Account \& Container](#account--container)
  - [Consent Mode Setup](#consent-mode-setup)
  - [GA4 Configruation Tag](#ga4-configruation-tag)
  - [Page Views](#page-views)
- [Monitoring Page Views in GA4](#monitoring-page-views-in-ga4)
- [Adding a Custom Dimension with Data Layer](#adding-a-custom-dimension-with-data-layer)
  - [Monitor Dimension in GA4](#monitor-dimension-in-ga4)
- [Adding a Custom Event](#adding-a-custom-event)
  - [Turn Event into Conversion](#turn-event-into-conversion)
  - [Monitor Conversion in GA4](#monitor-conversion-in-ga4)
- [Create an Audience](#create-an-audience)
  - [Trigger Event For Member Added](#trigger-event-for-member-added)
- [Synch to Big Query](#synch-to-big-query)

## Pre-Requisites

You're going to need a [google account](https://myaccount.google.com/) so that you can leverage [google analytics](https://analytics.google.com/analytics/web/) and [google tag manager](https://tagmanager.google.com/). There's then a nice [google platform homepage](https://marketingplatform.google.com/home) you can use as a portal to leverage these tools (among others).

## Why use Google Analytics 4?

[Google analytics 4](https://developers.google.com/analytics/devguides/collection/ga4) is a great tool to monitor your website with very minimal effort. It offers a huge amount of built in analytics out of the box, it integrates well into google tag manager and allows you to synch a million rows of event data to [big query](https://cloud.google.com/bigquery) absolutely free - daily! I also have a preference to use [google tag manager](https://tagmanager.google.com/) to manage all GA integration over the site tag as once in place it allows complete management of analytics from GTM without the need for website deploys.

## Creating a GA Account, Property and Data Stream

The hierarchy for a google analytics setup is an account, a property and a data stream. The Account tends to be at a business level where you will have a separate legal entity. A property would then map to a brand within that entity. A data stream would then be a particular website or app, where iOs and Android applications need to be separate data streams. The streams all link up to a single property view though so you can see all the interactions from an overall perspective.

### Account

First go to your [google analytics](https://analytics.google.com/analytics/web/), then go to admin and create an account.

![Create GA Account]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-create-account.png)

Give the GA account a name and accept the defaults.

![GA Account Name]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-create-account_2.png)

### Property

Create a property and update local settings.

![GA Property]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-create-account_3.png)

Update your business information and then create.

### Data Stream

In admin click create data stream for web (as we're doing a webpage in this instance).

![GA Create Data Stream]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-create-datastream.png)

Name the website explicitly and call the data stream the same name.

![GA Create Data Stream]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-create-datastream_1.png)

Once created, copy the measurement id ready to use in GTM to configure GA later.

![GA Create Data Stream]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-create-datastream_2.png)

## Using a GTM Container with Standard Tags

### Account & Container

In gtm click create account

fill in details for account and container

### Consent Mode Setup

Setup consent mode as per blog.

### GA4 Configruation Tag

### Page Views

## Monitoring Page Views in GA4

## Adding a Custom Dimension with Data Layer

### Monitor Dimension in GA4

## Adding a Custom Event

### Turn Event into Conversion

### Monitor Conversion in GA4

## Create an Audience

### Trigger Event For Member Added

## Synch to Big Query





