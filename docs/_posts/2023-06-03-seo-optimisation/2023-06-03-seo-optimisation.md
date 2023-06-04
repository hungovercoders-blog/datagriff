---
title: "SEO What's Occurring? | Basic Search Engine Optimisation"
date: 2023-06-03
author: dataGriff
description: Supercharge your web page with meta tag optimization, SEO analysis, and AI-powered content assistance from ChatGPT
image:
  path: /assets/2023-06-03-seo-optimisation/link.png
tags: SEO
---

I realised not enough people were coding under the influence and visiting the hungovercoders website. I simply could not understand why not everyone in the world was coming to this awesome site. I heard the letters SEO and thought - what's occurring? A quick test found that the SEO score of the site was under 20%. Here is what I found out to improve the SEO of [www.hungovercoders.com](www.hungovercoders.com) and [blog.hungovercoders.com](blog.hungovercoders.com)!

I may have been on Barry Island when I thought of the title of this blog post and nothing [ChatGPT](https://chat.openai.com/) was going to say was going to make me change that.

- [Useful Links and Tools](#useful-links-and-tools)
- [Importance of Meta Tags](#importance-of-meta-tags)
- [Meta Tags on Jekyll Sites](#meta-tags-on-jekyll-sites)
- [Analyse Site SEO Performance with Seobility](#analyse-site-seo-performance-with-seobility)
  - [Create a Project](#create-a-project)
  - [Adding Txt to Domain](#adding-txt-to-domain)
- [Create a Sitemap](#create-a-sitemap)
- [Google Search Console](#google-search-console)
- [Manual ChatGPT Usage](#manual-chatgpt-usage)
- [Future Thoughts](#future-thoughts)

## Useful Links and Tools

- [Meta Tags Checker](https://metatags.io/) - Great for checking your meta tags are working as expected and how they will look in search results and social media link sharing.
- [Seobility](https://www.seobility.net) - Great free tool which was my first real insights into SEO performance for my webpages. Also recommend downloading the [seo check](https://play.google.com/store/apps/details?id=net.seobility.seocheck&hl=en&gl=US&pli=1) mobile app provided by seobility which appears to have unlimited site checks! Great to see taking the steps below how your score can go up... and its slightly addictive!
- [XML-Sitemaps](https://www.xml-sitemaps.com/) - Used this for generating sitemaps.
- [Google Search Console](https://search.google.com/search-console) - Further insights into seo optimisation and a staple tool of google users. I found as my sites currently have such low traffic though it hasn't been as useful as seobility above.
- [Google Search Console Training Videos](https://www.youtube.com/playlist?list=PLKoqnv2vTMUOnQn-lNDfT38X9gA_CHxTo) - Further insights into using google search console.
- [ChatGPT](https://chat.openai.com/) - Likely going to take over the world and feature in a number of blogs going forward - but at the moment just super useful for optimising your content and meta tags.

## Importance of Meta Tags

Meta tags are pieces of html at the top of a webpage. Each of them contributes in different ways to search engine optimisation and how text or images appear in links. If you navigate to [www.hungovercoders.com](www.hungovercoders.com), then right-click and view page source, you will see the HTML and something that looks like the below in the head. I've removed the css links and the google tag manager scripts from html - but these would be at the end - just to focus on the importance of this meta section.

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">

  <!-- Primary Meta Tags -->
  <title>Hungovercoders | Coding Under the Influence</title>
  <meta name="title"
    content="Hungovercoders | Coding Under the Influence<">
  <meta name="description"
    content="Explore our technical blogs and discover innovative solutions which indulge in the fun side of topics like film, geek culture, music, local food, beer, and breweries.">
  <meta name="author" content="Richard Griffiths">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://www.hungovercoders.com/">
  <meta property="og:title"
    content="Hungovercoders | Coding Under the Influence">
  <meta property="og:description"
    content="Explore our technical blogs and discover innovative solutions which indulge in the fun side of topics like film, geek culture, music, local food, beer, and breweries.">
  <meta property="og:image" content="https://www.hungovercoders.com/assets/meta_image.png">

  <!-- Twitter -->
  <meta property="twitter:card" content="summary_large_image">
  <meta property="twitter:url" content="https://www.hungovercoders.com/">
  <meta property="twitter:title"
    content="Hungovercoders | Coding Under the Influence">
  <meta property="twitter:description"
    content="Explore our technical blogs and discover innovative solutions which indulge in the fun side of topics like film, geek culture, music, local food, beer, and breweries.">
  <meta property="twitter:image" content="https://www.hungovercoders.com/assets/meta_image.png">

  <link rel="icon" type="image/png" sizes="16x16" href="assets/logo3.ico">
  <link rel="apple-touch-icon" type="image/png" sizes="16x16" href="assets/logo3.ico">

 <!-- Scripts and GTM after meta -->

</head>
  <body>
     <!-- Content -->
  </body>
</html>
```

The title and description are the important meta tags for key word search optimisation and how your content will appear in web searches. The html ```<title>``` tag is what provides the description at the top of your webpage.

The first html```<meta name="title">``` is what creates the text at the top of search results. The other two title sections then for 'og' and 'twitter' are for general social media content and twitter respectively. I have chosen to keep the title consistent everywhere so the same message is always displayed.

The html ```<meta name="description">``` is what creates underneath the title in search results or the more detailed text below social media links the other meta descriptions. Again I have chosen to keep all these consistent to make it easier.

![Meta Search Results]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/meta-search-results.png)

The  html```<meta name="viewport" content="width=device-width, initial-scale=1.0">``` is key to ensure that your webpage displays appropriately sized on any screen that it is displayed upon. This was a bit of a revelation!

We then also have a number of image tags that have different purposes. The two images at the end, html```<link rel="icon"``` and html```<link rel="apple-touch-icon"``` are what create icons either at the top of your webpage tab or on apple tablet style devices respectively. Both recommended as improving performance in SEO.

We then have the social media images in html```<meta property="og:image"``` and html```<meta property="twitter:image"```. These are the images that will be shown when you share your links on social media.

You'll notice that search engines and social media might take a little while to get the updated meta tags that you want to share. This was when I discovered [meta tags](https://metatags.io/) which allows you to pop in the link to your website and confirm everything is working correctly. Nice!

![Meta Validator]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/meta-validator.png)

## Meta Tags on Jekyll Sites

For blog posts being generated by Jekyll I wanted to know how meta tags were controlled by the yaml that you use to autogenerate blog posts. Luckily this was fairly straight forward and those devils at Jekyll had made everything really easy.

At the top of each blog post you can add yaml that looks like this:

```yaml
---
title: "SEO What's Occurring? | Basic Search Engine Optimisation"
date: 2023-06-03
author: dataGriff
description: Supercharge your web page with meta tag optimization, SEO analysis, and AI-powered content assistance from ChatGPT.
image:
  path: /assets/2023-06-03-seo-optimisation/link.png
tags: SEO
---
```

The title and description complete the respective meta tags everywhere as expected and the image also caters for the image tags. I tend to check my new blog posts on [meta tags](https://metatags.io/) now before posting them to the world on social media to confirm everything is tickety boo.

## Analyse Site SEO Performance with Seobility

Going down the rabbit hole of SEO I came across [Seobility](https://www.seobility.net) and found that I had an extremely low SEO score on a number of my sites. I won't go into every aspect of the check here as you can just put your webpage through the [tool](https://www.seobility.net/en/seocheck/) for free and see for yourself the great output. [Seobility](https://www.seobility.net) has a limited number of calls on the free tier but I found I could use the [seo check](https://play.google.com/store/apps/details?id=net.seobility.seocheck&hl=en&gl=US&pli=1) mobile app as much as I wanted.

The great thing about this SEO check tool is it gives you a score and a breakdown of all the things you want to try and fix in great detail.

![SEO Check Overview]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/seo-check-overview.png)

As a quick checklist based on the output of the tools ensure you always consider the following to improve your SEO:

- Ensure you have good [meta tags](#importance-of-meta-tags) in your html header as per the above and that they are complete.
- Make sure you declare the doctype, the language and use the viewport setting in your html.
- Create a [sitemap](#create-sitemap) (see below).
- Make sure your meta tags, h1 and content on the site are all of the appropriate length and share common textual themes.
- Promote everything on social media and tell your mam about your website in order to improve backlinks.

There are loads of tools on this website that I am still exploring but I have gone from a score of about 20% to over 70% or 80% on my websites now, so I still have work to do!

![SEO Check Tools]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/seo-check-tools.png)

### Create a Project

With the free tier you can create one project in seobility that you will then see in your [dashboard](https://www.seobility.net/en/dashboard/).

![SEO Check Dashboard]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/seo-check-dashboard.png)

There is again a huge swathe of tooling to get stuck in to here and one of my favourites is the ranking page. Here you can add keywords to check the ranking of and you can see that hungovercoders is offically the number one rank for the keyword hungovercoders! (drops mic, sips can)

![SEO Check Ranking]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/seo-check-rankings.png)

### Adding Txt to Domain

In order to allow Seoility and google search console to crawl your site you'll be asked at some point to add a TXT to your domain. I use namecheap and these additions look something like this under the Advanced DNS.

![TXT Records]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/txt-records.png)

You can then confirm these additions by using nslookup.

e.g. to check TXT

```bash
nslookup -q=txt hungovercoders.com
```
e.g. to check CNAME

```bash
nslookup -q=cname hungovercoders.com
```

e.g to check the IP address and domain name system (DNS) record

```bash
nslookup hungovercoders.com
```

## Create a Sitemap

One of the things that came our of using [Seobility](https://www.seobility.net) and exploring [Google Search Console](https://search.google.com/search-console) was that a sitemap could be useful. A sitemap just being a file in XML that represents the pages of your website. I found and utilised the tool [XML-Sitemaps](https://www.xml-sitemaps.com/) to generate these for now. Crawlers will now find a sitemap at [www.hungovercoders.com/sitemap.xml](www.hungovercoders.com/sitemap.xml) and [blog.hungovercoders.com/sitemap.xml](blog.hungovercoders.com/sitemap.xml) which should assist in them understanding the website content so improving search engine optimisation.

e.g.

```xml
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">
<!--  created with Free Online Sitemap Generator www.xml-sitemaps.com  -->
  <url>
    <loc>https://www.hungovercoders.com/</loc>
    <lastmod>2023-05-28T18:45:42+00:00</lastmod>
    <priority>1.00</priority>
  </url>
  <url>
    <loc>https://www.hungovercoders.com/breweries/</loc>
    <lastmod>2023-05-01T16:52:24+00:00</lastmod>
    <priority>0.80</priority>
  </url>
</urlset>
```

I'll look to update this regularly now and hopefully automate the process in code at somepoint as there seems to be a number of options after a quick search ([sitemap-generator](https://pypi.org/project/sitemap-generator/), [python-sitemap-generator](https://github.com/wiejakp/python-sitemap-generator) etc).

## Google Search Console

Another tool that had been recommend to me was [Google Search Console](https://search.google.com/search-console). I haven't found it as useful as Seobility tooling yet but I think this was because of my distinct lack of volume so this should only get more interesting.

I have now uploaded a sitemap to google search console and you can also see:

- The total number of google web search clicks.
- The total number of impressions and the total number of clicks with average click through rate.
- Average ranking position.
- What pages are indexed and force them to be indexed.

![Google Search Console]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/google-search-console.png)

## Manual ChatGPT Usage

And so it begins... yes during this process I needed to generate content for my landing pages quite quickly on [www.hungovercoders.com](www.hungovercoders.com) and [blog.hungovercoders.com](blog.hungovercoders.com). This became a lot of fun as I started putting [ChatGPT](https://chat.openai.com/) through its paces to help me. For example I could start of with some content like this for the blog landing page.

"A website that has technical blog posts that use fun topics such as beer, geek, food, film and music for inspiration"

Then I could ask chatgpt to make it more "alcoholic".. and voila! Boozey and epic content!

![Content More Alcoholic]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/chatgpt-more-alcoholic.png)

Once I started playing with this I also realised I could use it to optimise my meta tag information and have them interact with each other.

![ChatGPT Meta Tags]({{ site.baseurl }}/assets/2023-06-03-seo-optimisation/chatgpt-meta-tags.png)

The current content on [www.hungovercoders.com](www.hungovercoders.com) and [blog.hungovercoders.com](blog.hungovercoders.com) are a combination of a few beers and my first foray into prompt engineering... I hope this will only get better and that I only use the robots for good, not evil.

## Future Thoughts

Ok, ChatGPT might have taken over the world by my next blog post, and who knows if its me or a robot writing them (I promise I'll throw in my usual charm so you know it's me), but here are my thoughts on automation to perhaps make general website generation easier.

- Automate sitemap generation and upload to relevant tooling.
- Automate validation of meta tags.
- Create [ChatGPT](https://chat.openai.com/) integrated content creator or validator that analyses your website for desired keyword optimisation that either feeds back on a regular cadence, or letting it drive and change the content dynamically... A bit of an experiment that one and would likely need another model to check for semantics and inappropriate language, but its definitely at the back of my mind to try.

Keep coding under the influence and keep searching for fun!
