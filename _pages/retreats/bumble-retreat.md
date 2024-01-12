---
layout: compose
includes:
  - path: about.html
    options:
      title: pages.retreats.bumbleretreat.about.title
      body: pages.retreats.bumbleretreat.about.body
      markdownify: true
      section: info
      css_class: bg-light
      more_includes:
        - file: obs/carousel.html
          options:
            gallery:
              - slides: &slides_1
                - /assets/img/impressions/obs-1-3.webp
                - /assets/img/services/bumblespace_effective-workshop.webp
                - /assets/img/impressions/retreat-1-3.webp
  - path: about.html
    options:
      title: pages.retreats.bumbleretreat.info.title
      body: pages.retreats.bumbleretreat.info.body
      markdownify: true
      section: info

namespace: bumble-retreat
permalink: /bumble-retreat
nav_highlight: pages.retreats.title
title: pages.retreats.bumbleretreat.title

header:
  title: pages.retreats.bumbleretreat.header.title
  text: pages.retreats.bumbleretreat.header.text
  button: pages.retreats.bumbleretreat.header.button
  buttonlink: "mailto:info@bumbleflies.de"

foot:  
  scripts:
    - url: /assets/js/lazy-load.js

---
