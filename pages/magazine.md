---
title: Magazine Releases
permalink: /magazine/
---

{% for issue in site.data.magazines %}
{% assign permalink = issue["permalink"] %}
{% assign current = site.posts | where_exp: "item" , "item.permalink contains permalink" %}
<div class="magazine-summary" markdown=1>
<h3 class="mag-header"> #{{ issue["issue-number"] }} | {{ issue["month"] }} {{ issue["year"] }} <span><a class="reveal" href="{{issue["permalink"]}}"> Browse</a> <a class="reveal" target="_blank" href="/assets/magazines/issue{{issue['issue-number']}}.pdf"> Download</a></span></h3>
<ul>
{% for perm in issue["highlights"] %}
{% assign post = current | find_exp: "post" , "post.permalink contains perm" %}
<li><span class="magazine-summary-title">{{ post.title }}</span><span class="archive-author">{{ post.authors | join: ", " }}</span></li>
{% endfor %}

</ul>
</div>
<hr>
{% endfor %}
