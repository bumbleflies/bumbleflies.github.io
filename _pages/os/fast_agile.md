---
layout: compose
includes:
  - path: about.html
    options:
      title: pages.openspace.fast_agile.about.title
      body: pages.openspace.fast_agile.about.body
      markdownify: true
      section: info
      css_class: bg-light
  - path: gallery.html
  - path: about.html
    options:
      title: pages.openspace.fast_agile.explain.title
      body: pages.openspace.fast_agile.explain.body
      markdownify: true
      section: info
      css_class: bg-light

namespace: fast_agile
permalink: /fast_agile
nav_highlight: pages.openspace.title
title: pages.openspace.fast_agile.title

header:
  title: pages.openspace.fast_agile.header.title
  text: pages.openspace.fast_agile.header.text
  button: pages.openspace.fast_agile.header.button
  buttonlink: "#download"

gallery:
  height: 283
  title: pages.openspace.fast_agile.gallery.title
  section: download
  list:
    - desc: pages.openspace.fast_agile.gallery.user_guide.de.desc
      image:
        url: pages.openspace.fast_agile.gallery.user_guide.de.image.small
        copyright: "[Cron Technologies LLC](https://www.fastagile.io/), bumbleflies UG"
        hover:
          title: pages.openspace.fast_agile.gallery.user_guide.de.title
          big_download: /assets/img/fast_agile/FASTGuide2.12 - GERMAN.pdf
    - desc: pages.openspace.fast_agile.gallery.value_cycle.desc
      image:
        url: pages.openspace.fast_agile.gallery.value_cycle.image.small
        hover:
          title: pages.openspace.fast_agile.gallery.value_cycle.title
          big: pages.openspace.fast_agile.gallery.value_cycle.image.big
    - desc: pages.openspace.fast_agile.gallery.user_guide.en.desc
      image:
        url: pages.openspace.fast_agile.gallery.user_guide.en.image.small
        copyright: "[Cron Technologies LLC](https://www.fastagile.io/), bumbleflies UG"
        hover:
          title: pages.openspace.fast_agile.gallery.user_guide.en.title
          big_download: /assets/img/fast_agile/FASTGuide2.12.pdf

foot:
  scripts:
    - url: /assets/js/lazy-load.js
---
