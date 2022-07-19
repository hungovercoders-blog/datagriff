---
title: "Welcome to hungovercoders blog"
---

I'm glad you are here. I plan to talk about ...

{% for category in site.categories %}
  <h3>{{ tag[0] }}</h3>
  <ul>
    {% for post in category[1] %}
      <li><a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
{% endfor %}
