---
title: "Track Your Beer with a Tag"
date: 2023-02-20

author: dataGriff
---

You have a load of lovely links on your website that link to external alcoholic partners. How do you keep track of your beer fuelled journeys when a customer goes to those beer-infused partners?? With google tag manager and some tasty javascript, that's how!


- [PreRequisites](#prerequisites)
- [Create a Tag](#create-a-tag)
- [Create a Trigger](#create-a-trigger)
- [Test your Trigger](#test-your-trigger)
- [Publish your Changes](#publish-your-changes)

## PreRequisites

Ok you're going to need to setup [google tag manager](https://support.google.com/tagmanager/answer/6103696?hl=en) on your website. Once this is done you can setup a trigger and a tag as below.

## Create a Tag

Use a custom HTML and add the following Javascript. This will fire for any external links on your website.

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

Create a trigger on just links. Do it for all link clicks in this case. You can also add a delay to state if you want to ensure the tag fires.

## Test your Trigger

Once you're done, click preview and go to your website to check that the tag is firing.

## Publish your Changes

Finally submit and the changes will be published to the website.
