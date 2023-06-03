# Bumbleflies homepage
made possible with
- [jekyll](https://jekyllrb.com/)
- [agency-theme](https://github.com/raviriley/agency-jekyll-theme)

## Build
### Install bundles
```bash
bundle install
```
### Build site
```bash
bundle exec jekyll build
```
### Serve locally
```bash
bundle exec jekyll serve
```

## Conventions
### Location of markdown files
Pages are located in [_pages](_pages) directory

### Template construction
Every page needs to have at least
```
---
layout: <layout>
namespace: <name>
permalink: <url-name>
permalink_en: <url-name>
nav_highlight: <navigation title to highlight (referencing i18n-key)>
title: <page title (referencing i18n-key)>
---
```
- `layout` is the [template](_layouts) to be used to render the page
- `namespace` is used to resolve translated url when used with `{% tl <namespace> %}`
- `permalink` and `permalink_en` denote the url-names of the site in different languages
- `nav_highlight` references the same i18n-key which is used in [navigation](_data/navigation.yml) in order to highlight when the page is selected
- `title` is the i18n-key to resolve the title

### i18n
The page uses i18n in languages defined in [_config.yml](_config.yml) and resolves key by looking them up in [_i18n directory](_i18n).
#### Translate keys
Key are resolved using
```markdown
{% t key.to.look.up %}
```
usually, keys aren't resolved directly from i18n files, but from page variables. 

##### Example
Given you have a markdown file like this

`index.md`
```markdown
---
layout: default
title: pages.home.title
----
```

and your translation file contains a structure like this

`en.yml`
```markdown
pages:
  home:
    title: My Home
```

in order to translate the title for example in the title, you have to use the translation function like so

`_layouts/default.html`
```html
<title>{% page.title %}</title>
```
In such a way, the `default`template can be used for all pages, which specify a title i18n-key

#### Chaining
This comes with some limitations: this statement cannot be used in order to chain variables, linke for example
```markdown
{% t key.to.look.up | markdownify %}
```
This will produce an error like

    Missing i18n key: key.to.look.up | markdownify
    Using translation '' from default language: de
    Liquid Exception: no implicit conversion of nil into String in /_layouts/<layout>.html
In order to fix this, you need to use the `capture` function
```markdown
{% capture translated_content %}{% t key.to.look.up %}{% endcapture %}
{{ translated_content | markdownify }}
```
### Navigation
The navigation is constructed from [navigation template file](_data/navigation.yml), also containing i18n lookup keys.

## Next Event

The information text for the next event can be found in the [i18n folder](_i18n) in the `next.md` file