---
layout: compose
includes:
  - path: gallery.html
    css_class: bg-light
  - path: clients.html
    options:
      section: customer
      clients:
        - title: "BSH"
          url: 'https://www.bsh-group.com/'
          logo: /assets/img/clients/bsh-logo.png
        - title: "Siemens AG"
          url: 'https://www.siemens.com/de/de.html'
          logo: /assets/img/clients/siemens-logo.png
        - title: "Wohnungshelden"
          url: 'https://www.wohnungshelden.de/'
          logo: /assets/img/clients/wohnungshelden-logo.png

  - path: about.html 
    options:
      css_class: bg-light
      title: pages.about.title
      text: pages.about.text
      body: pages.about.body
      markdownify: true
  - path: team.html
    options:
      title: pages.team.title
      subtext: pages.team.subtext
      section: team

namespace: home
permalink: /
permalink_en: /
nav_highlight: pages.home.title
title: pages.home.title

header:
  title: pages.home.header.title
  text: pages.home.header.text
  button: pages.home.header.button
  buttonlink: "mailto:info@bumbleflies.de"

gallery:
  title: pages.home.gallery.title
  text: pages.home.gallery.text
  section: services
  list:
    - title: pages.home.gallery.items.app_development.title
      desc: pages.home.gallery.items.app_development.desc
      image: 
        url: /assets/img/bumblefly-blue.png
        copyright: bumbleflies UG
    - title: pages.home.gallery.items.lego_minecraft.title
      desc: pages.home.gallery.items.lego_minecraft.desc
      image: 
        url: /assets/img/bumblefly-blue.png
        copyright: bumbleflies UG
    - title: pages.home.gallery.items.workshops.title
      desc: pages.home.gallery.items.workshops.desc
      image: 
        url: /assets/img/bumblefly-blue.png
        copyright: bumbleflies UG
    - title: pages.home.gallery.items.openspace_coaching.title
      desc: pages.home.gallery.items.openspace_coaching.desc
      image:
        url: /assets/img/bumblefly-blue.png
        copyright: bumbleflies UG
---
