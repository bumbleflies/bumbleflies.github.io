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
      pretix:
        url: https://trainings.bumbleflies.de/fast/
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
    - url: https://trainings.bumbleflies.de/fast/widget/v1.css
foot:  
  translatable: pages.learning.fast.book.widget
---
