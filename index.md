---
layout: page
title: Home
---

<div id="home">
  <ul class="posts">
    {% for post in site.posts limit:1 %}
		<li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
		<hr>
		{{ post.content }}
    {% endfor %}
	<hr>
	<h1>Recent Posts</h1>
	{% for post in site.posts offset:1 limit:10 %}
		<li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
	{% endfor %}
  </ul>
</div>