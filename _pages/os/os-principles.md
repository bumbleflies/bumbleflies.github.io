---
layout: compose
includes:
  - path: gallery.html
    css_class: bg-light
  - path: about.html 

namespace: os-principles
permalink: /open-space-prinzipien-uebersicht
permalink_en: /open-space-principles
nav_highlight: Open Space
title: pages.os_principles.title

foot:
  scripts:
    - url: /assets/js/lazy-load.js

de: &DEFAULT_DE
  gallery:
    title: "5 Prinzipien und ein Gesetz"
    section: principles
    list:
      - desc: Wer auch immer kommt, es sind die richtigen
        image:
            url: /assets/img/os/1.jpg
            hover:
                title: Prinzip 1
                big: /assets/img/os/OS - Prinzip 1.jpg
      - desc: Was auch immer passiert, ist das einzige was passieren konnte
        image: 
            url: /assets/img/os/2.jpg
            hover:
                title: Prinzip 2
                big: /assets/img/os/OS - Prinzip 2.jpg
      - desc: Es beginnt, wenn die Zeit reif ist
        image: 
            url: /assets/img/os/3.jpg
            hover:
                title: Prinzip 3
                big: /assets/img/os/OS - Prinzip 3.jpg
      - desc: Es ist vorbei, wenn es vorbei ist
        image: 
            url: /assets/img/os/4.jpg
            hover:
                title: Prinzip 4
                big: /assets/img/os/OS - Prinzip 4.jpg
      - desc: Wo auch immer es passiert, ist der richtige Ort
        image: 
            url: /assets/img/os/5.jpg
            hover:
                title: Prinzip 5
                big: /assets/img/os/OS - Prinzip 5.jpg
      - desc: Wann immer du dich an einem Ort befindest, an dem du weder lernst noch etwas beitragen kannst, bewege dich dorthin, wo du das kannst
        image: 
            url: /assets/img/os/law.jpg
            hover:
                title: Gesetz der Mobilität
                big: /assets/img/os/OS - Gesetz.jpg
de-DE:
  <<: *DEFAULT_DE
---
# Open Space Prinzipien
