---
title: "Data Layer with Javascript"
date: 2023-02-27

author: dataGriff
---

I wanted to make some local breweries available to the browser client side so I can then use this in tagging exploits. Below talks through how I can make these alcoholic hotpots available in the data layer!


- [PreRequisities](#prerequisities)
- [What is the Data Layer?](#what-is-the-data-layer)
- [Setup a Basic Web Page with DataLayer](#setup-a-basic-web-page-with-datalayer)
- [Observe the Values of the DataLayer](#observe-the-values-of-the-datalayer)

## PreRequisities

- You can do this with notepad but I use [VS Code](https://code.visualstudio.com/) as my IDE and text editor.
- I recommend the [live server VS code extension](https://code.visualstudio.com/) to easily test running web pages in a browser.

## What is the Data Layer?

The data layer is a Javascript object that stores key value pairs client side in a browser. You can access this in chrome for example by going to developer tools, going to the console, typing in dataLayer on a page that has this object implemented, and hey presto there's the data layer! This object is commonly used to push data into web analytics tools such as google tag manager for insights. In google tag manager implementations it will be referred to as dataLayer.

## Setup a Basic Web Page with DataLayer

Its quite straight forward to setup a basic data layer. You first initiate an empty dataLayer at the start of your script. Then you can initiate custom events with dataLayer.push. It is important to always add an event value with the data layer push event so its easier for any users of the data to understand the context of any other labels. Below shows a basic webpage with some buttons that push the brewery name into the dataLayer on a click event. Copy and paste this into a breweries.html file.

```html
<head>
    <script>
        window.dataLayer = window.dataLayer || [];
    </script>
</head>
<body>
    <h1>Breweries</h1>
    <button onclick="window.dataLayer.push({'event': 'Click','brewery': 'Tiny Rebel'});">Tiny Rebel</button>
    <button onclick="window.dataLayer.push({'event': 'Click','brewery': 'Crafty Devil'});">Crafty Devil</button>
</body>
```

If you are using VS code open this with live server or if you are using a simple text editor just open the file in your favourite browser. You should see a simple web page with two buttons.

![Simple Page]({{ site.baseurl }}/assets/2023-02-27-data-layer/simplepage.png)

## Observe the Values of the DataLayer

Now to observer the values in the data layer. Open your developer tools and in the console type dataLayer and then press return. You should at first see an empty object as below.

![Empty Data Layer]({{ site.baseurl }}/assets/2023-02-27-data-layer/emptydatalayer.png)

Now click a button and type in dataLayer again, press return and you should see a brewery value available in the dataLayer as a result of a click event. This is now available to be use in tag manager tools.

![Click01]({{ site.baseurl }}/assets/2023-02-27-data-layer/click01.png)

If you click the other button and repeat the process you should then see the new brewery value and another click event.

![Click02]({{ site.baseurl }}/assets/2023-02-27-data-layer/click02.png)
