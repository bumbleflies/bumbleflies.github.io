---
layout: compose
includes:
  - path: about.html 
    options:
      title: pages.events.obs.about.title
      body: pages.events.obs.about.body
      section: info
      css_class: bg-light
      more_includes:
        - file: obs/carousel.html
          options:
            gallery:
              - slides:
                - /assets/img/impressions/obs-3-1.webp
                - /assets/img/impressions/obs-3-2.webp
                - /assets/img/impressions/obs-3-3.webp
              - slides:
                - /assets/img/impressions/obs-2-1.webp
                - /assets/img/impressions/obs-2-2.webp
                - /assets/img/impressions/obs-2-3.webp
              - slides:
                - /assets/img/impressions/obs-1-1.webp
                - /assets/img/impressions/obs-1-2.webp
                - /assets/img/impressions/obs-1-3.webp
  - path: about.html 
    options:
      title: pages.events.obs.next.title
      section: next
      more_includes:
        - file: obs/next.html
          options:
            info_file: _events/next.md
  - path: obs/tickets.html
    css_class: bg-light
  - path: about.html
    options:
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true

namespace: obs
permalink: /open-bumble-space
permalink_en: /open-bumble-space
nav_highlight: pages.events.title
title: pages.events.obs.title

pretix:
    url: 'https://events.bumbleflies.de/obs-3/'
head:
  styles:
    - url: https://events.bumbleflies.de/obs-3/widget/v1.css
foot:  
  scripts:
    - url: https://pretix.eu/widget/v1.de.js
    - url: /assets/js/lazy-load.js

header:
    title: pages.events.obs.header.title
    text: pages.events.obs.header.text
    button: pages.events.obs.header.button
    buttonlink: "#tickets"
de: &DEFAULT_DE
  next:
    title: Alle Infos zum nächsten Event
de-DE:
  <<: *DEFAULT_DE
---
