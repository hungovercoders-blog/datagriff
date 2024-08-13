---
title: "Adding Comments to Jekyll Minima Blog on Github Pages with Giscus"
date: 2023-11-11
author: dataGriff
description: Adding Comments to Jekyll Minima Blog on Github Pages with Giscus
image:
  path: /assets/2023-11-11-blog-comments-giscus/link.png
tags: Blog Github Giscus Jekyll
---

I wanted to start getting feedback for my [github pages](https://pages.github.com/){:target="\_blank"} hosted [jekyll minima](https://github.com/jekyll/minima){:target="\_blank"} backed blog posts. These could possibly be scathing drunkards furious with my methods, so that we may enter an educational debate, or simply feedback on how to improve areas as I am always busting to elevate my code! I came across [giscus](https://giscus.app/){:target="\_blank"} and found that this was very simple to do by backing it with [github discussions](https://docs.github.com/en/discussions){:target="\_blank"} as follows...

- [Prerequisites](#prerequisites)
- [Create Public Discussions Repo](#create-public-discussions-repo)
- [Generate Giscus Javascript](#generate-giscus-javascript)
- [Add Footer File to \_includes Folder](#add-footer-file-to-_includes-folder)
- [Comments Now Appear on Blog](#comments-now-appear-on-blog)

## Prerequisites

- [Github Account](https://www.github.com){:target="\_blank"}
- [Github pages](https://pages.github.com/){:target="\_blank"} blog backed with [jekyll minima](https://github.com/jekyll/minima){:target="\_blank"}.

## Create Public Discussions Repo

First create a public repo called ".discussions" in your github personal account or organisation.

![.discussions Repo]({{ site.baseurl }}/assets/2023-11-11-blog-comments-giscus/discussions_repo.PNG)

Then you need to enable discussions on your github personal account or organisation.

![Enable Discussions]({{ site.baseurl }}/assets/2023-11-11-blog-comments-giscus/discussions_enable.PNG)

## Generate Giscus Javascript

Navigate to [giscus app](https://giscus.app/){:target="\_blank"} and enter the following details;

- The language for your comments
- The repo that contains your blog that you want comments on
- I set the discussions category to be announcements
- I chose the them to be light but you can choose what you like.
- I pretty much chose defaults for everything else...

It will genertae some code that looks something like this:

```html
<div class="wrapper">
  <script
    src="https://giscus.app/client.js"
    data-repo="hungovercoders-blog/datagriff"
    data-repo-id="R_kgDOJT_U2A"
    data-category="Announcements"
    data-category-id="DIC_kwDOJT_U2M4CavN-"
    data-mapping="pathname"
    data-strict="0"
    data-reactions-enabled="1"
    data-emit-metadata="0"
    data-input-position="bottom"
    data-theme="light"
    data-lang="en"
    crossorigin="anonymous"
    async
  ></script>
</div>
```

## Add Footer File to \_includes Folder

Add a footer file to the \_includes folder of your blog repo.

![Footer File Directory]({{ site.baseurl }}/assets/2023-11-11-blog-comments-giscus/footer_file_directory.PNG)

Copy and paste this [footer script](https://github.com/jekyll/minima/blob/master/_includes/footer.html){:target="\_blank"} sourced from [Jekyll Minima source page](https://github.com/jekyll/minima){:target="\_blank"} into this footer file. Now add in the javascript that you generated from the [giscus app](https://giscus.app/){:target="\_blank"}. You directory structure and footer file content should look something like the below.

![Footer File]({{ site.baseurl }}/assets/2023-11-11-blog-comments-giscus/footer_file.PNG)

## Comments Now Appear on Blog

You can now see the comments functionality on this blog post in the footer below and in all my previous posts! You can now add a comment by logging in with your github account and sending me some feedback. Easy peasy.

These comments also appear in the [discussions](https://github.com/hungovercoders-blog/datagriff/discussions){:target="\_blank"} of the blog repo as this is what backs this functionality.

![Discussions Blog Repo]({{ site.baseurl }}/assets/2023-11-11-blog-comments-giscus/discussions_blog.PNG)

Where you can navigate to the individual blog posts and see the comments as per the "data-mapping" setting that you applied in giscus.

![Discussions Blog Post]({{ site.baseurl }}/assets/2023-11-11-blog-comments-giscus/discussions_blog_post.PNG)

I look forward to hearing from you!
