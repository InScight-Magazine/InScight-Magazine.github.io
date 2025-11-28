---
title: "Science Comics"
permalink: /comics/
---

{% for article in site.categories["comic"] %}
{% assign image = article.permalink | append: article.hero-image %}
## {{ article.title }}
**Comic by {{ article.authors | join:", " }}** | {{ article.date | date: "%b %Y" }}

{{ article.excerpt }}
<br>
<br>
<img src="/assets/images/{{ image }}"/>
{% endfor %}
