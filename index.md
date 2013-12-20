---
layout: page
title: Home
---

<div id="home">
    <div class="span10">
        {% for post in site.posts limit:1 %}
            <span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a>
            <hr>
            {{ post.content }}
        {% endfor %}
        <hr>
        <div>
            <h1>Recent Posts</h1>
            <ul class="posts">
                {% for post in site.posts offset:1 limit:10 %}
                    <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
                {% endfor %}
            </ul>
        </div>
    </div>
</div>
