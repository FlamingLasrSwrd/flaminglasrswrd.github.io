---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
  layout: home
---

# Posts
{% for p in site.posts %}

  <h3><a href="{{ site.url }}{{ p.url }}">{{ p.title }}</a></h3>
  {{ p.excerpt | markdownify | normalize_whitespace }}

{% endfor %}
