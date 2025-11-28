# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a bilingual (German/English) Jekyll-based static website for bumbleflies.de, using the agency-jekyll-theme as a base. The site is deployed to both GitHub Pages (staging) and a custom live server through GitHub Actions workflows.

## Development Commands

### Initial Setup
```bash
# Install Ruby dependencies (if bundler 2.4.x permission issues occur)
mkdir ~/.gems_cache
bundle config path ~/.gems_cache
bundle install
```

### Build and Serve
```bash
# Build the site (outputs to _site/)
bundle exec jekyll build

# Build to custom directory (e.g., _test_site/ for testing)
bundle exec jekyll build -d _test_site

# Serve locally (default: http://localhost:4000)
bundle exec jekyll serve
```

### Testing
```bash
# Install Python test dependencies
pip install -r _tests/requirements.txt

# Run all tests (requires built site in _test_site/)
pytest _tests/

# Run specific test file
pytest _tests/test_on_every_page.py
```

### CSS and Font Optimization
```bash
cd _purge
./purge.sh  # Downloads latest CSS, builds site, purges unused CSS/fonts
```

**Important**: New Font Awesome icons must be manually added to `_purge/purge-fa.py` before purging.

## Architecture

### Internationalization (i18n)
- **Languages**: German (default) and English (`_config.yml` languages: ["de", "en"])
- **Translation files**: `_i18n/de.yml` and `_i18n/en.yml` contain all translatable strings
- **Markdown content**: `_i18n/de/` and `_i18n/en/` directories contain localized markdown files
- **URL structure**: German pages at root (`/ueber-uns`), English pages in `/en/` subdirectory (`/en/about`)

#### Using Translations
```liquid
{% t key.to.look.up %}
```

Pages define i18n keys in frontmatter which are resolved in templates:
```yaml
---
title: pages.home.title  # References _i18n/de.yml -> pages.home.title
---
```

**Limitation**: Cannot chain filters directly with translation. Use capture instead:
```liquid
{% capture translated_content %}{% t key.to.look.up %}{% endcapture %}
{{ translated_content | markdownify }}
```

### Page Structure
All pages in `_pages/` require this frontmatter:
```yaml
---
layout: <layout>           # Template from _layouts/
namespace: <name>          # For translated URL resolution with {% tl <namespace> %}
permalink: <url>           # German URL
permalink_en: <url>        # English URL
nav_highlight: <i18n-key>  # Matches navigation.yml entry to highlight active nav item
title: <i18n-key>          # Page title i18n key
---
```

### Layouts
- `_layouts/compose.html` - Compose page from multiple includes with options
- `_layouts/standard.html` - Standard single-content page
- `_layouts/default.html` - Base HTML structure
- `_layouts/google-form.html` - Embed Google Forms
- `_layouts/redirect.html` - Redirect pages

### Navigation
Defined in `_data/navigation.yml` with i18n keys. Supports nested submenus.

### Background Images
Multi-step process required to add new background images:

1. Add entry to `_data/style.yml`:
   ```yaml
   my-image: "/assets/img/my-header.webp"
   ```

2. Create SCSS variable in `assets/css/bumble.scss`:
   ```scss
   $my-image: "{{ site.data.style.my-image }}";
   ```

3. Define CSS class in `_sass/_header_images.scss`:
   ```scss
   &.my-image {
     background-image: url("#{$my-image}");
   }
   ```

4. (Optional) Add preload to `_includes/head.html`:
   ```html
   <link rel="preload" as="image" href="{{ site.data.style.my-image }}" type="image/webp">
   ```

5. Use in page frontmatter:
   ```yaml
   header:
     image-class: my-image
   ```

## CI/CD Pipeline

### Workflow Structure
- `build-deploy.yml` - Main workflow triggered on all branch pushes
  - Calls `part_build_test.yml` - Builds site and runs pytest tests
  - Calls `part_deploy_stage.yml` - Deploys to GitHub Pages (staging)
  - Calls `part_deploy_live.yml` - Pushes to `stable` branch and triggers live deployment webhook

### Deployment Targets
- **Staging**: GitHub Pages (automatic from `_site/` artifact)
- **Live**: Custom server at bumbleflies.de (triggered via webhook after pushing to `stable` branch)

### Main Branch
The default and main branch is `master`.

## Directory Structure

- `_pages/` - Page markdown files with frontmatter
- `_layouts/` - HTML templates
- `_includes/` - Reusable HTML components
- `_sass/` - SCSS stylesheets (compiled to CSS)
- `_i18n/` - Translation files (de.yml, en.yml) and localized markdown
- `_data/` - YAML data files (navigation, style, team, etc.)
- `_tests/` - Python pytest tests
- `_site/` - Built site (git-ignored)
- `_test_site/` - Test build output (git-ignored)
- `_purge/` - CSS/font optimization scripts
- `_externals/` - Git submodules (agency-jekyll-theme, flag-icons)
- `assets/` - Static assets (images, CSS, JS, fonts)

## External Dependencies

- Jekyll with github-pages gem
- jekyll-multiple-languages-plugin for i18n
- agency-jekyll-theme (git submodule in `_externals/`)
- flag-icons (git submodule in `_externals/`)
- Bootstrap 4.6.2
- Font Awesome icons

## Testing Notes

Tests use pytest with BeautifulSoup to validate:
- HTML structure and content on all pages
- Sitemap validity
- Redirects
- Rich results/structured data
- Language-specific page content

The `conftest.py` fixture builds the site to `_test_site/` and serves it on localhost:8000 for testing.
