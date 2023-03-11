---
title: "Cookie Consent for your Website"
date: 2023-03-04

author: dataGriff
---

Ok beer and code lovers, I wanted to make sure that I captured consent for analytics for anyone coming to the hungovercoders website.  I'll be honest by the end of my consent rabbit hole I really fancied a can, but instead I'll share my knowledge here with you of how I leverage [Google Tag Manager](https://tagmanager.google.com/) and [Klaro](https://heyklaro.com/docs/klaro?utm_source=hungovercoders) to manage consent. The reason that this is such a great combination is that it is free, extremely customizable and you can manage your consent from a single point.

- [PreRequisities](#prerequisities)
- [Sources](#sources)
- [Enable Google Tag Manager Consent Overview](#enable-google-tag-manager-consent-overview)
- [Capture User Consent with Klaro](#capture-user-consent-with-klaro)
- [Create User Defined Vairables to Hold Each Consent](#create-user-defined-vairables-to-hold-each-consent)
- [Use GTM Consent State Template Variable](#use-gtm-consent-state-template-variable)
- [Use GTM Consent Mode Template Tag](#use-gtm-consent-mode-template-tag)
- [Create Consent Test Tags](#create-consent-test-tags)
- [Preview the Work](#preview-the-work)
- [Submit and Test Site](#submit-and-test-site)

## PreRequisities

As this consent is using [Google Tag Manager](https://tagmanager.google.com/) you will also need this with a container running on your website. In order to have cookie consent on any entry point on your website, you'll need to make sure GTM is installed on every page, and every page going forward.
You'll also need a privacy or terms and condition page for your website in order to direct any questions around consent towards this. The dialog box we build will direct users to this if they have any queries.

## Sources

I did my background learning and stealing from far more learned people than me. Please see [Muhammad Ali's blog](https://muhammadali.xyz/js-simple-cookie-consent/?utm_source=hungovercoders) for a great simple cookie consent explanation, who then put me on to [klaro](https://heyklaro.com/docs/klaro?utm_source=hungovercoders) as an open source consent tool. I then discovered this great video tutorial by [measureschool](https://measureschool.com/?utm_source=hungovercoders) backed up by this [blog post](https://measureschool.com/cookie-consent-banner/). It's also worth reading through [google tag manager consent configuration](https://support.google.com/tagmanager/answer/10718549?hl=en). However I will be summarising all of this into my own brand of hungovercoder succinctness below...

## Enable Google Tag Manager Consent Overview

First of all enable google tag manager consent overview in tag manager. This is by far the best place to start as it immediately gives you an overarching view of the variables that apply consent on each of your tags. You will also see that there a number of built-in consent parameters for tags like GA4 for analytics and advertising. Understanding the names of these variables up-front will help us map our Klaro consent to the consent mechanism out of the box from GTM. To further understand the impact of these built-in variables to google analytics, please see documentation [here](https://support.google.com/analytics/answer/9976101?hl=en).

To enable consent overview, in google tag manager go to Admin > Container Settings and then tick Enable Consent overview.

![GTM Enable Consent Overview]({{ site.baseurl }}/assets/2023-03-11/enable-consent-overview.png)

Navigate back to your tags and click the shield icon, this will show all the consent parameters for each tag you currently have. You can see that there are automatic built-in ones you can leverage and you also have the ability to add your own.

![GTM Enable Consent Overview]({{ site.baseurl }}/assets/2023-03-11/consent-overview-shield.png)

By seeing the built in ones for GA4 we know for example the simple consent we need to capture in order to fairly utilise GA4 analytics with respect to our website users consent.

![GTM Enable Consent Overview]({{ site.baseurl }}/assets/2023-03-11/consent-overview-tags.png)

We are therefore interested in out website user being able to set an analytics (analytics_storage) and advertising (ads_storage) consent mechanism based in the built-in consent flags. We will therefore use this as a guide in our implementation.

## Capture User Consent with Klaro

First create a new workspace in your [Google Tag Manager](https://tagmanager.google.com/) called "consent" so we can do all the work in this isolated workspace from the off. When everything is working we can then preview this to test it and submit to our website.

![GTM Consent Workspace]({{ site.baseurl }}/assets/2023-03-11/klaro-gtm-workspace.png)

Next create a new tag called "Consent Capture" that uses Custom HTML. It is here we will place our open source [klaro](https://heyklaro.com/docs/klaro?utm_source=hungovercoders) code to capture consent. I basically took this [example config.js](https://github.com/kiprotect/klaro/blob/master/dist/config.js) from the github, shortened it into the code below and added the initiation script for klaro for our use specific case to map to the built-in GTM consent we require.

Copy the code below and paste it into your tag to follow exactly what I have done, or take a look at the config to understand more the options you would like to apply. Comments in the code show the changes I made.

```js
<script>
var klaroConfig = {
    version: 1,
    elementID: 'klaro',
    styling: {
        theme: ['light', 'top', 'wide'],
    },
    noAutoLoad: false,
    htmlTexts: true,
    embedded: false,
    groupByPurpose: false,
    storageMethod: 'cookie',
    cookieName: 'consent_klaro', // change cookie name to show consent in name
    cookieExpiresAfterDays: 365,
    default: false, // set the global default to be not consenting
    mustConsent: true, // ensure users have to consent when enter website
    acceptAll: true,
    hideDeclineAll: false,
    hideLearnMore: false,
    noticeAsModal: false,
    translations: {
        zz: {
            privacyPolicyUrl: '/privacy.html', // link to privacy page
        },
        en: {
            consentModal: {
                title: '<u>Cookie Consent</u>', // Modal box heading
                description:
                    'Here you can see and customize the information that we collect about you.', // Modal box text
            },
            analytics: { 
                description: 'Collecting of visitor statistics to understand site traffic and user behaviour without being utilised for marketing',
            },
           marketing: {
                description: 'Marketing to users of the website based on the information collected',
            },
            purposes: {
                analytics: 'Analytics', 
                marketing: 'Marketing', 
            },
        },
    },
    services: [
        {
            name: 'analytics', // this will eventually map to analytics_storage in GTM
            title: 'Analytics',
            default: true, // set to true and hope users nice
            purposes: ['analytics'],
        },
        {
            name: 'marketing',  // this will eventually map to ads_storage in GTM
            title: 'Marketing',
            default: false, // set to false and hope users realise being nice
            purposes: ['marketing'],
        },
    ],
};
</script>
<script defer type="text/javascript" src="https://cdn.kiprotect.com/klaro/v0.7.11/klaro.js"></script>
```

Add a trigger to your tag for "Consent Initialization - All Pages". Your "Consent Capture" tag should now look something like the following.

![GTM Consent Tag]({{ site.baseurl }}/assets/2023-03-11/klaro-consent-capture-tag.png)

To see the new functionality in action go to "Preview" in google tag manager and connect to your website.

![Klaro Consent Pop-Up]({{ site.baseurl }}/assets/2023-03-11/klaro-consent-pop-up.png)

If you for example decline marketing but leave analytics as it is, you can see the variable set correctly in tag assistant.

![GTM Consent Variable]({{ site.baseurl }}/assets/2023-03-11/klaro-consent-variable.png)

Remember this just sets a cookie at this point, it does not map of the any consent values to the behaviour in GTM where we capture data for different use cases, so we need to do this in the next section.

## Create User Defined Vairables to Hold Each Consent

Create a new User-Defined variable called "consentAnalytics". This will hold the conent captured from the klaro consent object above. Set the variable to custom javascript and paste in the code below.

```javascript
function(){
  var cookie = {{consentCapture}}
  if(!cookie){return 'denied'}
  var json = JSON.parse(cookie)
  if(json['analytics']){
    return 'granted'
  }
  else
  { 
  return 'denied'
  }
}
```

Your variable should look like the below.

![GTM Consent Variable Analytics]({{ site.baseurl }}/assets/2023-03-11/consent-variable-analytics.png)

Create a new User-Defined variable called "consentMarketing. This will hold the consent captured from the klaro consent object above. Set the variable to custom javascript and paste in the code below.

```javascript
function(){
  var cookie = {{consentCapture}}
  if(!cookie){return 'denied'}
  var json = JSON.parse(cookie)
  if(json['marketing']){
    return 'granted'
  }
  else
  { 
  return 'denied'
  }
}
```

Your variable should look like the below.

![GTM Consent Variable Marketing]({{ site.baseurl }}/assets/2023-03-11/consent-variable-marketing.png)

## Use GTM Consent State Template Variable

We now want to add a variable that GTM can use to map to the global GTM consent mode we saw in the first section of this blog post. Luckily someone has made this for us as a template so we can go to templates, variable templates and add the GTM consent state. 

![GTM Consent Template Variable]({{ site.baseurl }}/assets/2023-03-11/gtm-consent-template-variable-add.png)

Add this to your workspace and accept the fact its a third party.

![GTM Consent Template Variable Add]({{ site.baseurl }}/assets/2023-03-11/gtm-consent-template-variable-add-workspace.png)

Go to variables and add a new user defined variable called "consentState", which is the template you just added.

![GTM Consent Variable]({{ site.baseurl }}/assets/2023-03-11/gtm-consent-variable-add.png)

In the next section we'll ensure that our klaro consent is mapped to this variable so that GTM consent can pick up the values.

## Use GTM Consent Mode Template Tag

Luckily we have another template we can use, this time a tag. Go to templates and search in the tag templates for "Consent Mode" and add the one shown below.

![GTM Consent Template Tag]({{ site.baseurl }}/assets/2023-03-11/gtm-consent-template-tag-add.png)

Add this to your workspace and accept the fact its a third party.

![GTM Consent Template Tag Add]({{ site.baseurl }}/assets/2023-03-11/gtm-consent-template-tag-add-workspace.png)

Go to Tags and add this new template as a tag called "Consent Mode". Set the Consent Command to be "Update", then configure the rest as below. Note that advertising and analytics are using our new variables that take their value originall from the klaro consent cookie. We just set everything else to be denied for now as we are not using them.

![GTM Tag Consent Mode]({{ site.baseurl }}/assets/2023-03-11/tag-consent-mode.png)

Add a trigger to this tag so that it fires on "Consent Initialization - All Pages".

![GTM Tag Consent Mode Trigger]({{ site.baseurl }}/assets/2023-03-11/tag-consent-mode-trigger.png)

## Create Consent Test Tags

In order to make sure the consent for marketing and analytics is working correctly I added two test tags for every page. First add a new tag called "Consent Test Analytics". Use custom HTML and add the script below which will log the tag firing to the console.

```javascript
<script>
  console.log("Consent Test Analytics Tag Fired")
</script>
```

Your tag should look like this.

![GTM Consent Test Analytics]({{ site.baseurl }}/assets/2023-03-11/consent-test-analytics.png)

Under advanced settings in the tag, for consent settings set the "Require additional consent for tag to fire" to be "analytics_storage". This will be picked up from the GTM consent mode we have added. Have this tag trigger on every page so we can monitor it.

![GTM Consent Test Analytics Settings]({{ site.baseurl }}/assets/2023-03-11/consent-test-analytics-settings.png)

Secondly add a new tag called "Consent Test Marketing". Use custom HTML and add the script below which will log the tag firing to the console.

```javascript
<script>
  console.log("Consent Test Marketing Tag Fired")
</script>
```

Your tag should look like this.

![GTM Consent Test Marketing]({{ site.baseurl }}/assets/2023-03-11/consent-test-marketing.png)

Under advanced settings in the tag, for consent settings set the "Require additional consent for tag to fire" to be "ads_storage". This will be picked up from the GTM consent mode we have added. Have this tag trigger on every page so we can monitor it.

![GTM Consent Test Marketing Settings]({{ site.baseurl }}/assets/2023-03-11/consent-test-marketing-settings.png)

## Preview the Work

## Submit and Test Site
