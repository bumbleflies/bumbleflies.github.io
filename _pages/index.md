---
layout: compose
includes:
  - path: gallery.html
    css_class: bg-light
  - path: clients.html
    options:
      section: customer
      max-height: 100px
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
  - path: team.html

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

clients:
  section: customer
  max-height: 100px
  list:
    - title: "BSH"
      url: 'https://www.bsh-group.com/'
      logo: /assets/img/clients/bsh-logo.png
    - title: "Siemens AG"
      url: 'https://www.siemens.com/de/de.html'
      logo: /assets/img/clients/siemens-logo.png
    - title: "Wohnungshelden"
      url: 'https://www.wohnungshelden.de/'
      logo: /assets/img/clients/wohnungshelden-logo.png

gallery:
  title: pages.home.gallery.title
  text: pages.home.gallery.text
  section: services
  list:
    - title: pages.home.gallery.items.effective_collaboration.title
      desc: pages.home.gallery.items.effective_collaboration.desc
      image: 
        url: /assets/img/services/bumblespace_effective-workshop.webp
        copyright: bumbleflies UG
    - title: pages.home.gallery.items.big_room.title
      desc: pages.home.gallery.items.big_room.desc
      image: 
        url: /assets/img/services/bumblespace_pi-planning.webp
        copyright: bumbleflies UG
    - title: pages.home.gallery.items.online_events.title
      desc: pages.home.gallery.items.online_events.desc
      image: 
        url: /assets/img/services/bumblespace_online-events.webp
        copyright: bumbleflies UG
---
