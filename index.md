---
layout: compose
includes:
  - path: gallery.html
    css_class: bg-light
  - path: clients.html
  - path: about.html 
    css_class: bg-light
  - path: team.html

namespace: home
permalink: /
permalink_en: /
nav_highlight: Home
title: pages.home.title

de: &DEFAULT_DE
  header:
    title: Willkommen bei den bumbleflies
    text: WIR LIEBEN OPEN SPACE!
    button: Schreib uns
    buttonlink: "mailto:info@bumbleflies.de"
  gallery:
    title: "Leistungen"
    text: "So unterstützen wir dich"
    section: services
    list:
      - title: 'Effektive Kollaboration'
        desc: 'Wir helfen dir, deine Meetings und Workshops effektiv, interaktiv und kollaborativ zu gestalten.<br/>Du wirst überrascht sein, wie viel Energie das bei deinen Mitarbeiter:innen freisetzt.'
        image: 
            url: /assets/img/services/bumblespace_effective-workshop.webp
            copyright: bumbleflies UG
      - title: 'Online Big-Room-Meetings'
        desc: 'Wir organisieren für dich dein nächstes Big-Room-Meeting (z.B. PI-Planning) für alle deine Teams. Egal ob 20, 200 oder mehr Personen.<br/>Wir sorgen für den produktiven Rahmen, damit ihr euch auf die Inhalte konzentrieren könnt.'
        image: 
          url: /assets/img/services/bumblespace_pi-planning.webp
          copyright: bumbleflies UG
      - title: 'Online Events'
        desc: 'Wir organisieren für dich ein Event, bei dem Teambuilding, Austausch und Spaß im Vordergrund stehen.<br/>Ihr habt euch seit einem Jahr nicht mehr gesehen und sucht den Kontakt zu den Kollegen? Dann ist das genau das richtige.'
        image: 
          url: /assets/img/services/bumblespace_online-events.webp
          copyright: bumbleflies UG
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

de-DE:
  <<: *DEFAULT_DE
---
