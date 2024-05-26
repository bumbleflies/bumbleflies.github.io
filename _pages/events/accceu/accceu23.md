---
layout: compose
includes:
  - path: about.html 
    options:
      title: pages.events.accceu.23.about.title
      body: pages.events.accceu.23.about.body
      markdownify: true
      section: info
      css_class: bg-light
      more_includes:
        - file: obs/carousel.html
          options:
            gallery:
              - slides: &slides_1
                - /assets/img/impressions/accceu23/accceu-1-1.webp
                - /assets/img/impressions/accceu23/accceu-1-2.webp
                - /assets/img/impressions/accceu23/accceu-1-3.webp
              - slides:
                - /assets/img/impressions/accceu23/accceu-3-1.webp
                - /assets/img/impressions/accceu23/accceu-3-2.webp
                - /assets/img/impressions/accceu23/accceu-3-3.webp
              - slides:
                - /assets/img/impressions/accceu23/accceu-4-1.webp
                - /assets/img/impressions/accceu23/accceu-4-2.webp
                - /assets/img/impressions/accceu23/accceu-4-3.webp
              - slides:
                - /assets/img/impressions/accceu23/accceu-2-1.webp
                - /assets/img/impressions/accceu23/accceu-2-2.webp
                - /assets/img/impressions/accceu23/accceu-2-3.webp
  - path: about.html 
    options:
      title: pages.events.accceu.23.next.title
      body: pages.events.accceu.23.next.intro
      markdownify: true
      section: next
  - path: about.html
    options:
      css_class: bg-light
      section: schedule
      title: pages.events.accceu.23.schedule.title
      body: pages.events.accceu.23.schedule.body
      markdownify: true
  - path: about.html
    options:
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true

namespace: accceu23
permalink: /agiles-camper-coach-camp-23
permalink_en: /agile-camper-coach-camp-23
nav_highlight: pages.events.title
title: pages.events.accceu.23.title
slogan: pages.events.accceu.23.slogan

header:
  title: pages.events.accceu.23.header.title
  text: pages.events.accceu.23.header.text
  button: pages.events.accceu.23.header.button
  buttonlink: "#info"
  image-class: accceu-image

event: 
  name: pages.events.accceu.23.title
  description: pages.events.accceu.23.about.body
  intro: pages.events.accceu.23.next.intro
  images: *slides_1
  cant:
    title: pages.events.accceu.23.cant.title
    body: pages.events.accceu.23.cant.body
---
