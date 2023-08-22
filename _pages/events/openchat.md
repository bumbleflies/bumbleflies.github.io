---
layout: compose
includes:
  - path: about.html 
    options:
      title: pages.events.openchat.about.title
      body: pages.events.openchat.about.body
      markdownify: true
      section: info
      css_class: bg-light
  - path: about.html 
    options:
      title: pages.events.openchat.next.title
      section: next
      more_includes:
        - file: obs/next.html
        - file: obs/carousel.html
          options:
            gallery:
              - slides: &slides_1
                - /assets/img/impressions/openchat-1-1.webp
                - /assets/img/impressions/openchat-1-2.webp
                - /assets/img/impressions/openchat-1-3.webp
  - path: obs/tickets.html
    css_class: bg-light
  - path: about.html
    options:
      section: schedule
      title: pages.events.openchat.schedule.title
      body: pages.events.openchat.schedule.body
      markdownify: true
  - path: about.html
    options:
      css_class: bg-light
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true

namespace: openchat
permalink: /openchat
nav_highlight: pages.events.title
title: pages.events.openchat.title
slogan: pages.events.openchat.slogan

pretix: &offer
    url: 'https://events.bumbleflies.de/openchat/'
head:
  styles:
    - url: https://events.bumbleflies.de/openchat/widget/v1.css
foot:  
  scripts:
    - url: /assets/js/lazy-load.js
  translatable: pages.events.pretix.widget

header:
  title: pages.events.openchat.header.subtitle
  text: pages.events.openchat.header.title
  button: pages.events.accceu.header.button
  buttonlink: "#tickets"

event: 
  name: pages.events.openchat.title
  description: pages.events.openchat.about.body
  intro: pages.events.openchat.next.intro
  date:
      start: 2023-11-14T10:00+01:00
      end: 2023-11-15T18:00+01:00
  location:
    name: pages.events.openchat.location.name
    url: pages.events.openchat.location.url
    header: pages.events.openchat.location.header
    body: pages.events.openchat.location.body
    address:
      street: "August-Everdings-Str. 20"
      locality: München
      code: 81671
      country: DE
  images: *slides_1
  offer: 
    <<: *offer
    from: 2023-09-01T01:02+01:00
    price: 500
  cant:
    title: pages.events.openchat.cant.title
    body: pages.events.openchat.cant.body
---
