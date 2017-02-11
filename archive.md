---
  layout: page
  title: "Archive"
---

<ul>
{% for post in site.categories.archive %}
<li>
  <a href="{{ post.url }}">{{ post.title }}</a>
  {{ post.excerpt | markdownify | normalize_whitespace }}
</li>
{% endfor %}
</ul>
