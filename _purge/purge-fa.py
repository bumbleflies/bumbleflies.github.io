#!/usr/bin/fontforge
import os
import sys

import fontforge

if len(sys.argv) < 2:
    print(f'Usage: fontforge -script {sys.argv[0]} <font dir> <desc dir>')
    sys.exit()


inDir = os.path.abspath(sys.argv[1])
outDir = os.path.abspath(sys.argv[2])

fonts = {'fas': 'fa-solid-900.svg', 'far': 'fa-regular-400.svg', 'fab': 'fa-brands-400.svg'}
exts = ['svg', 'ttf', 'woff', 'woff2', 'eot']

icons = {'fas': ['download', 'bars', 'times', 'chevron-right', 'plus', 'language', 'angle-left', 'angle-right'],
         'fab': ['twitter', 'linkedin-in', 'github', 'mastodon']
         }

print(icons)
for font in icons:
    f = fontforge.open(inDir + '/' + fonts[font])

    for icon in icons[font]:
        f.selection.select(('more', None), icon)

    for i in f.selection:
        try:
            name, width = f[i].glyphname, f[i].width
            print(font, i, name, width)
        except:
            pass

    f.selection.invert()
    for i in f.selection.byGlyphs:
        f.removeGlyph(i)

    filePath = outDir + '/' + fonts[font].rsplit('.', 1)[0]
    for ext in exts:
        f.generate(filePath + '.' + ext)
        print(filePath + '.' + ext, 'generated')

    os.remove(filePath + '.afm')
