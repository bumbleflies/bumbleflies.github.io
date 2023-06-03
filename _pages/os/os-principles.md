---
layout: compose
includes:
  - path: gallery.html
    css_class: bg-light
  - path: about.html 
    options:
      css_class: bg-light
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true

namespace: os-principles
permalink: /open-space-prinzipien-uebersicht
permalink_en: /open-space-principles
nav_highlight: pages.openspace.title
title: pages.openspace.principles.title

foot:
  scripts:
    - url: /assets/js/lazy-load.js

gallery:
    title: pages.openspace.principles.gallery.title
    section: principles
    list:
      - desc: pages.openspace.principles.gallery.one.desc
        image:
            url: pages.openspace.principles.gallery.one.image.small
            hover:
                title: pages.openspace.principles.gallery.one.title
                big: pages.openspace.principles.gallery.one.image.big
      - desc: pages.openspace.principles.gallery.two.desc
        image: 
            url: pages.openspace.principles.gallery.two.image.small
            hover:
                title: pages.openspace.principles.gallery.two.title
                big: pages.openspace.principles.gallery.two.image.big
      - desc: pages.openspace.principles.gallery.three.desc
        image: 
            url: pages.openspace.principles.gallery.three.image.small
            hover:
                title: pages.openspace.principles.gallery.three.title
                big: pages.openspace.principles.gallery.three.image.big
      - desc: pages.openspace.principles.gallery.four.desc
        image: 
            url: pages.openspace.principles.gallery.four.image.small
            hover:
                title: pages.openspace.principles.gallery.four.title
                big: pages.openspace.principles.gallery.four.image.big
      - desc: pages.openspace.principles.gallery.five.desc
        image: 
            url: pages.openspace.principles.gallery.five.image.small
            hover:
                title: pages.openspace.principles.gallery.five.title
                big: pages.openspace.principles.gallery.five.image.big
      - desc: pages.openspace.principles.gallery.law.desc
        image: 
            url: pages.openspace.principles.gallery.law.image.small
            hover:
                title: pages.openspace.principles.gallery.law.title
                big: pages.openspace.principles.gallery.law.image.big
---
