---
title: "Quick Start for Google Analytics 4 Using Google Tag Manager"
date: 2023-03-27
author: dataGriff

description: This is how you can quickly setup a google analytics 4 property using google tag manager to monitor your website traffic

image:
  path: /assets/2023-03-27-ga4-gtm-quickstart/link.png

tags: google-tag-manager google-analytics
---

I want google analytics 4 on my website and I want it now. How else can I ensure that all the hungovercoders are learning all the best tech and finding their local breweries?? The following shows you how to setup a GA4 property and hook it up to your website with google tag manager...

- [Pre-Requisites](#pre-requisites)
- [Why use Google Analytics 4 and GTM?](#why-use-google-analytics-4-and-gtm)
- [Creating a GA Account, Property and Data Stream](#creating-a-ga-account-property-and-data-stream)
  - [Account](#account)
  - [Property](#property)
  - [Data Stream](#data-stream)
- [Using a GTM Container with Standard Tags](#using-a-gtm-container-with-standard-tags)
  - [Account and Container](#account-and-container)
  - [Add Container to Your Website](#add-container-to-your-website)
  - [Create New GTM Workspace](#create-new-gtm-workspace)
  - [GA4 Variables](#ga4-variables)
  - [GA4 Configuration Tag](#ga4-configuration-tag)
  - [Preview and Monitor Page Views in GA4](#preview-and-monitor-page-views-in-ga4)
  - [Consent Mode Setup](#consent-mode-setup)
  - [Publish](#publish)

## Pre-Requisites

You're going to need a [google account](https://myaccount.google.com/) so that you can leverage [google analytics](https://analytics.google.com/analytics/web/) and [google tag manager](https://tagmanager.google.com/). There's then a nice [google platform homepage](https://marketingplatform.google.com/home) you can use as a portal to leverage these tools (among others).

## Why use Google Analytics 4 and GTM?

[Google analytics 4](https://developers.google.com/analytics/devguides/collection/ga4) is a great tool to monitor your website with very minimal effort. It offers a huge amount of built in analytics out of the box, it integrates well into google tag manager and allows you to synch a million rows of event data to [big query](https://cloud.google.com/bigquery) absolutely free - daily! I also have a preference to use [google tag manager](https://tagmanager.google.com/) to manage all GA integration over the site tag as once in place it allows complete management of analytics from GTM without the need for website deploys.

The following setup will look something like the below.

![GA GTM Map]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-gtm-map.drawio.png)

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

We'll create a GTM account first that we'll consider as mapping at the same level to the GA account we setup previously. The container for GTM will then map to the data stream we created in GA. We could end up with multiple containers mapping to multiple data streams that roll up to a single property in GA, but for now this is our simple quickstart.

### Account and Container

In google tag manager click create account.

![GA Create Data Stream]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-create-account_0.png)

Fill in your details and click create.

![GA Create Data Stream]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-create-account.png)

### Add Container to Your Website

Go to Admin, copy the code and paste it on every page of your website.

![GTM Install]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-install.png)

### Create New GTM Workspace

In google tag manager, to keep all your setup work isolated, in create a new workspace called "setup".

### GA4 Variables

In Variables, create a new constant User-Defined Variable called "GA Measurement ID". Copy and paste your google analytics measurement ID into here. You'll either have this saved from earlier or you can get it from your relevant google analytics web data stream.

![GA Variable ID]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm_variable_ga_id.png)

### GA4 Configuration Tag

Then go to tags > New.

![GTM New Tag]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-new-tag.png)

Add a new tag for google analytics: GA4 configuration. Set the measurement ID to be the GA4 MeasurementID you setup in the previous step. Add a trigger and set it to all pages then save your tag.

![GTM New Tag]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-tag-ga-config.png)

### Preview and Monitor Page Views in GA4

With GTM tags setup for Google Analytics 4 and firing on all page views, we should be able to preview out GTM work and see page views firing in google analytics.

First click preview in your "setup" workspace.

![GTM New Tag]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-preview.png)

Enter in your domain URL and click connect.

![GTM New Tag]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-url.png)

Navigate the website and confirm you can see tags firing on each page view.

![GTM New Tag]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-tag-fire.png)

Then go to google analytics, go to reports, choose "real time" and you should see your first page views!

![GA Page Views]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/ga-page-views.png)

### Consent Mode Setup

In order to start collecting google analytics data for real you really should setup consent on your website to ensure customers know what data is being collected about them. You can set this up using this cookie consent mechanism as per this previous [blog post](https://www.hungovercoders.com/blog/datagriff/2023/03/11/cookie-consent.html).

### Publish

Now that you are happy that your tag is firing and sending your first page views to google analytics (with consent!), you can now publish your container to make it live on your website. To do this click submit in your GTM workspace...

![GTM Submit]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-submit.png)

Then click publish...

![GTM Submit]({{ site.baseurl }}/assets/2023-03-31-ga4-gtm-quickstart/gtm-publish.png)

Now that it's published you should go to your website, navigate a few pages and confirm you can see it in your google analytics property.

Now crack open a can of something lite and watch all those users flood in to your site via the wonders of google analytics. Good code-lite solution for analytics, plenty of time leftover to earn tomorrows hangover.
