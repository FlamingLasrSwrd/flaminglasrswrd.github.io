---
  layout: page
  title: "Active"
---
<ul>
{% for post in site.categories.active %}
<li>
  <a href="{{ post.url }}">{{ post.title }}</a>
  {{ post.excerpt | markdownify | normalize_whitespace }}
</li>
{% endfor %}
</ul>
