---
title: "Track Your Beer with a Tag"
date: 2023-02-20

author: dataGriff
---

You have a load of lovely links on your website that link to external alcoholic partners. How do you keep track of your beer fuelled journeys when a customer goes to those beer-infused partners?? With google tag manager and some tasty javascript, that's how!


- [PreRequisites](#prerequisites)
- [Create a Workspace](#create-a-workspace)
- [Create a Tag](#create-a-tag)
- [Create a Trigger](#create-a-trigger)
- [Test your Trigger](#test-your-trigger)
- [Publish your Changes](#publish-your-changes)

## PreRequisites

Ok you're going to need to setup [google tag manager](https://support.google.com/tagmanager/answer/6103696?hl=en) on your website. Once this is done you can setup a trigger and a tag it as below.

## Create a Workspace

In tag manager create a workspace that describes your and the work you are going to perform ({user}-{work}). This is the equivalent to a git branch as it will disappear at the end once you submit into to the default workspace (which is live!).

![GTM Workspace]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/workspace.png)

## Create a Tag

Create a custom HTML tag.

![GTM Tag]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/tag.png)

Add the following javascript which will append a tracking id for any external links on pages that the tag is triggered on.

```javascript
<script type="text/javascript">
  function create_UUID(){
    var dt = new Date().getTime();
    var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = (dt + Math.random()*16)%16 | 0;
        dt = Math.floor(dt/16);
        return (c=='x' ? r :(r&0x3|0x8)).toString(16);
    });
    return uuid;
}
  
  
    // Set the domain/URL to your website.
    var myDomain = "www.hungovercoders.com";
    // Grab all links (anchor tags)
    var links = document.getElementsByTagName('a');
    // Loop through all links
    Array.prototype.forEach.call(links, function (link) {
        // If we find a link that does not go to my domain
        if ( link.href.indexOf(myDomain) < 0 ) {
           // Take the href and append the UTM parameters
           link.href += '?TrackingId='+create_UUID();
        }
    });
</script>
```

## Create a Trigger

Create a trigger on just links. You can do it on all links or add a filter to match on such as "beer" below which means the tag will only fire on the beer link. You can also add a delay to state if you want to ensure the tag fires.

![GTM Trigger]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/trigger.png)

## Test your Trigger

Once you're done, click preview and go to your website to check that the tag is firing.

![GTM Preview]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/preview.png)

Set the URL of what you want to debug.

![GTM URL]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/url.png)

You see that the TrackingId has been added to the beers page url due to the tag firing.

![GTM URL]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/firing.png)

## Publish your Changes

Finally submit and the changes will be published to the real website.

![GTM Preview]({{ site.baseurl }}/assets/2023-02-21-track-your-beer-with-a-tag/preview.png)
