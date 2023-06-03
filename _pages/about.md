---
layout: compose
includes:
  - path: about.html 
    options:
      css_class: bg-light
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true
  - path: team.html
    options:
      title: pages.team.title
      subtext: pages.team.subtext
      section: team

namespace: about
permalink: /ueber-uns
permalink_en: /about
nav_highlight: pages.about.title
title: pages.about.title
---