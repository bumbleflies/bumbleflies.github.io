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
              - slides: &slides_1
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

pretix: &offer
    url: 'https://events.bumbleflies.de/obs-4/'
head:
  styles:
    - url: https://events.bumbleflies.de/obs-4/widget/v1.css
foot:  
  scripts:
    - url: https://pretix.eu/widget/v1.de.js
    - url: /assets/js/lazy-load.js

header:
  title: pages.events.obs.header.title
  text: pages.events.obs.header.text
  button: pages.events.obs.header.button
  buttonlink: "#tickets"

event: 
  name: pages.events.obs.title
  description: pages.events.obs.about.body
  intro: pages.events.obs.next.intro
  date:
      start: 2023-10-11T18:00+01:00
      end: 2023-10-11T22:00+01:00
  location:
    name: pages.events.obs.next.location.name
    url: pages.events.obs.next.location.url
    header: pages.events.obs.next.location.header
    body: pages.events.obs.next.location.body
    address:
      street: "Schleißheimer Str. 25"
      locality: München
      code: 80333
      country: DE
  images: *slides_1
  offer: 
    <<: *offer
    from: 2023-08-19T01:02+01:00
    price: 10
  cant:
    title: pages.events.obs.cant.title
    body: pages.events.obs.cant.body
---
