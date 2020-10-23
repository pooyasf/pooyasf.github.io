---
layout: page
title: photos
permalink: /photos/
description: My collection of photos from all over Iran.
nav: true
---

<div class="photos grid">

  {% assign sorted_photos = site.photos | sort: "importance" %}
  {% for photos in sorted_photos %}
  <div class="grid-item">
    {% if photos.redirect %}
    <a href="{{ photos.redirect }}" target="_blank">
    {% else %}
    <a href="{{ photos.url | relative_url }}">
    {% endif %}
      <div class="card hoverable">
        {% if photos.img %}
        <img src="{{ photos.img | relative_url }}" alt="photos thumbnail">
        {% endif %}
        <div class="card-body">
          <h2 class="card-title text-lowercase">{{ photos.title }}</h2>
          <p class="card-text">{{ photos.description }}</p>
          <div class="row ml-1 mr-1 p-0">
            {% if photos.github %}
            <div class="github-icon">
              <div class="icon" data-toggle="tooltip" title="Code Repository">
                <a href="{{ photos.github }}" target="_blank"><i class="fab fa-github gh-icon"></i></a>
              </div>
              {% if photos.github_stars %}
              <span class="stars" data-toggle="tooltip" title="GitHub Stars">
                <i class="fas fa-star"></i>
                <span id="{{ photos.github_stars }}-stars"></span>
              </span>
              {% endif %}
            </div>
            {% endif %}
          </div>
        </div>
      </div>
    </a>
  </div>
{% endfor %}

</div>
