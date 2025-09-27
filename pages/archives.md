---
title: Archives
permalink: /archives/
---

Complete archive of all _Articles_, _Interviews_ and _Insight Digest_ publications from InScight, sorted by year and category.

{% assign start_year = site.archive-year["start"] %}
{% assign end_year = site.archive-year["end"] %}
<div class="year-list">
{% for year in (start_year..end_year) reversed %}
<a class="button" href="#{{ year }}">{{ year }}</a>
{% endfor %}
</div>

{% for year in (start_year..end_year) reversed %}
<h2 id="{{ year }}">{{ year }}</h2>
<div class="year-list">
{% for pair in site.archives %}
<a class="button" href="#{{ year }}-{{ pair[0] }}">{{ pair[1] }}</a>
{% endfor %}
</div>
{% for pair in site.archives %}
  {% assign category = pair[0] %}
  <h3 id="{{ year }}-{{ pair[0] }}">{{ pair[1] }}</h3>
  {% assign posts = site.posts | where: "category", category %}
  {% for item in posts %}
  {% assign post_year = item.date | date: "%Y" | to_integer %}
  {% if post_year != year %}
  {% continue %}
  {% endif %}
  {% if category != "digest" %}
  <div markdown=1><a href="{{ item.url }}" class="title-link">{{ item.title }}</a>&nbsp;&nbsp;\|&nbsp;&nbsp; {% if item.authors != nil %} <span class="archive-author">_{{ item.authors | join: ", " }}_ </span> &nbsp;&nbsp;\|&nbsp;&nbsp; {% endif %}{{ item.date | date:"%b %d" }}
  </div>
  {% else %}
  {% assign issue = item.issue %}
  <h4>Issue {{ issue }}</h4>
  {% assign filename = "issue" | append: issue %}
  {% for item in site.data.digest[filename] %}
  {% assign slug = item["Title"] | slugify %}
  {% assign link = "/issue" | append: issue | append: "/digest/#" | append: slug %}
  <div markdown=1><a href="{{ link }}" class="title-link">{{ item.Title }}</a>&nbsp;&nbsp;\|&nbsp;&nbsp; <span class="archive-author">_{{ item.Author }}_ </span>
  </div>
  {% endfor %}
  {% endif %}
  {% endfor %}
{% endfor %}
{% endfor %}
