---
layout: compose
includes:
  - path: about.html
    options:
      title: pages.learning.fast.about.title
      body: pages.learning.fast.about.body
      markdownify: true
      section: overview
      css_class: bg-light
  - path: about.html
    options:
      title: pages.learning.fast.contents.title
      body: pages.learning.fast.contents.body
      markdownify: true
      section: content

namespace: fast-training
permalink: /fast-training
nav_highlight: pages.learning.title
title: pages.learning.fast.title

header:
  title: pages.learning.fast.header.title
  text: pages.learning.fast.header.text
  button: pages.learning.fast.header.button
  buttonlink: "#book"

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
        copyright: "[Cron Technologies LLC](https://www.fastagile.io/)"
        hover:
          title: pages.openspace.fast_agile.gallery.user_guide.en.title
          big_download: /assets/img/fast_agile/FASTGuide2.12.pdf

foot:
  scripts:
    - url: /assets/js/lazy-load.js
---
