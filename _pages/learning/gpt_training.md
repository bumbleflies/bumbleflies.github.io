---
layout: compose
includes:
  - path: about.html
    options:
      title: pages.learning.ai.about.title
      body: pages.learning.ai.about.body
      markdownify: true
      section: overview
  - path: pretix.html
    options:
      section: book
      css_class: bg-light
      pretix: &offer
        url: https://trainings.bumbleflies.de/master-gpt/
        problems: pages.learning.ai.book.problem
  - path: about.html
    options:
      title: pages.learning.ai.contents.title
      body: pages.learning.ai.contents.body
      markdownify: true
      section: content

namespace: gpt-training
permalink: /gpt-training
nav_highlight: pages.learning.title
title: pages.learning.ai.title
slogan: pages.learning.ai.slogan

header:
  title: pages.learning.ai.header.title
  text: pages.learning.ai.header.text
  button: pages.learning.ai.header.button
  buttonlink: "#book"

head:
  styles:
    - url: https://trainings.bumbleflies.de/master-gpt/widget/v1.css
foot:  
  translatable: pages.learning.ai.book.widget

event: 
  name: pages.learning.ai.about.title
  description: pages.learning.ai.about.body
  date:
      start: 2024-01-15T00:00+01:00
      end: 2024-06-30T00:00+01:00
  location:
    name: pages.learning.ai.location.name
    url: pages.learning.ai.location.url
  offers:
    - url: https://trainings.bumbleflies.de/master-gpt/4003783/
      from: 2024-01-15T00:00+01:00
      price: 70
    - url: https://trainings.bumbleflies.de/master-gpt/4003815/
      from: 2024-01-15T00:00+01:00
      price: 200
    - url: https://trainings.bumbleflies.de/master-gpt/4003815/
      from: 2024-01-15T00:00+01:00
      price: 200
---
