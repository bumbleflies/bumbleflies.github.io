---
layout: compose
includes:
  - path: about.html 
    options:
      title: pages.events.accceu.24.about.title
      body: pages.events.accceu.24.about.body
      markdownify: true
      section: info
      css_class: bg-light
      more_includes:
        - file: obs/carousel.html
          options:
            gallery:
              - slides: &slides_1
                - /assets/img/impressions/accceu-1-1.webp
                - /assets/img/impressions/accceu-1-2.webp
                - /assets/img/impressions/accceu-1-3.webp
              - slides:
                - /assets/img/impressions/accceu-3-1.webp
                - /assets/img/impressions/accceu-3-2.webp
                - /assets/img/impressions/accceu-3-3.webp
              - slides:
                - /assets/img/impressions/accceu-4-1.webp
                - /assets/img/impressions/accceu-4-2.webp
                - /assets/img/impressions/accceu-4-3.webp
              - slides:
                - /assets/img/impressions/accceu-2-1.webp
                - /assets/img/impressions/accceu-2-2.webp
                - /assets/img/impressions/accceu-2-3.webp
  - path: about.html 
    options:
      title: pages.events.accceu.24.next.title
      section: next
      more_includes:
        - file: obs/next.html
  - path: iframe.html
    options:
      title: pages.events.accceu.24.register.title
      section: register
      css_class: bg-light
      iframe:
        url: 'https://docs.google.com/forms/d/e/1FAIpQLSd2saCiWlpytiNAAblTXQuADi36bONEziL8vZArMMaWa4lMRA/viewform?usp=sf_link'
        info: pages.events.accceu.24.register.body
  - path: about.html
    options:
      section: schedule
      title: pages.events.accceu.24.schedule.title
      body: pages.events.accceu.24.schedule.body
      markdownify: true
  - path: about.html
    options:
      css_class: bg-light
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true

namespace: accceu24
permalink: /agiles-camper-coach-camp-24
permalink_en: /agile-camper-coach-camp-24
nav_highlight: pages.events.title
title: pages.events.accceu.24.title
slogan: pages.events.accceu.24.slogan

head:
  styles:
    - url: https://events.bumbleflies.de/accceu23/widget/v1.css
foot:  
  scripts:
    - url: /assets/js/lazy-load.js
  translatable: pages.events.pretix.widget

header:
  title: pages.events.accceu.24.header.title
  text: pages.events.accceu.24.header.text
  button: pages.events.accceu.24.header.button
  buttonlink: "#register"
  image-class: accceu-image

event: 
  name: pages.events.accceu.24.title
  description: pages.events.accceu.24.about.body
  intro: pages.events.accceu.24.next.intro
  date:
      start: 2024-09-06T13:00+01:00
      end: 2024-09-09T18:00+01:00
  images: *slides_1
  cant:
    title: pages.events.accceu.24.cant.title
    body: pages.events.accceu.24.cant.body
---
