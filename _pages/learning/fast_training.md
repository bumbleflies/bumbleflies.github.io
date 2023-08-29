---
layout: compose
includes:
  - path: about.html
    options:
      title: pages.learning.fast.about.title
      body: pages.learning.fast.about.body
      markdownify: true
      section: overview
  - path: pretix.html
    options:
      section: book
      css_class: bg-light
      pretix: &offer
        url: https://trainings.bumbleflies.de/fast-2/
        problems: pages.learning.fast.book.problem
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
slogan: pages.learning.fast.slogan

header:
  title: pages.learning.fast.header.title
  text: pages.learning.fast.header.text
  button: pages.learning.fast.header.button
  buttonlink: "#book"

head:
  styles:
    - url: https://trainings.bumbleflies.de/fast-2/widget/v1.css
foot:  
  translatable: pages.learning.fast.book.widget

event: 
  name: pages.learning.fast.about.title
  description: pages.learning.fast.about.body
  date:
      start: 2023-11-28T09:00+01:00
      end: 2023-11-29T18:00+01:00
  location:
    name: pages.learning.fast.location.name
    url: pages.learning.fast.location.url
  offer: 
    <<: *offer
    from: 2023-01-01T01:02+01:00
    price: 900
---
