# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Worktree Context: Multi-Repo Setup

This is a git worktree for the **bumbleflies.de redesign project** (Phase 1+ implementation).

**Worktree Structure:**
- `bumbleflies.github.io/` — Main Jekyll site (current production)
- `bumbleflies.github.io/beta/` — Astro 4.3.0 redesign (new site, in development)
- `container/` — Symlink to `/home/cda/dev/infrastructure/container` (infrastructure)
- `PHASE_1_SUMMARY.md` — Phase 1 completion status and architecture decisions

**Project Overview:**
Transform bumbleflies.de from a facilitator-focused site to a full transformation shop. Stack: Astro + DecapCMS, static hosting (Netlify). See the full spec at `/home/cda/dev/infrastructure/bumbleflies/PROJECT_HANDOFF.md`.

## Project Overview

This is the Bumbleflies homepage (`bumbleflies.de`), a Jekyll-based static site with:
- **Multilingual support**: German (de) and English (en) via `jekyll-multiple-languages-plugin`
- **Theme**: Agency Jekyll Theme (`jekyll-agency`)
- **CI/CD**: GitHub Actions with build, test, stage, and production deployment pipelines
- **Testing**: Python-based (pytest) integration tests that validate the built site

## Development Commands

### Setup & Installation

```bash
# Install Ruby dependencies
bundle install

# If bundler permission error occurs (bundler 2.4.x):
mkdir ~/.gems_cache
bundle config path ~/.gems_cache
```

### Build & Serve

```bash
# Build the site locally
bundle exec jekyll build

# Serve locally at http://localhost:4000
bundle exec jekyll serve

# Build to a specific directory (used by tests)
bundle exec jekyll build -d _test_site
```

### Testing

```bash
# Install test dependencies
pip install -r _tests/requirements.txt

# Run all tests
pytest _tests/

# Run a specific test file
pytest _tests/test_homepage_team.py

# Run tests with verbose output
pytest _tests/ -v

# Run a specific test function
pytest _tests/test_homepage_team.py::test_team_section_exists -v
```

### CSS Optimization

```bash
# Purge unused CSS and FontAwesome icons
cd _purge
./purge.sh
```

## Working with the Astro Beta Site

The new redesigned site is in `bumbleflies.github.io/beta/`:

```bash
cd bumbleflies.github.io/beta

# Install dependencies
npm install

# Serve locally at http://localhost:3000
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

**Key files:**
- `astro.config.mjs` — Astro configuration (static output to dist/)
- `src/pages/` — Page routes (Astro file-based routing)
- `src/components/` — Reusable components
- `src/layouts/` — Page templates (base Layout.astro)
- `.github/workflows/build-beta.yml` — Docker build CI/CD pipeline
- `Dockerfile` — Multi-stage build (Node 20 → Nginx Alpine)

**Docker Images:**
Docker images are auto-built in CI to `bumblecode/web:beta` (Docker Hub) on push to `feature/bumbleflies-redesign`. Docker builds must happen in CI only, not locally.

**Auto-Deployment (Dev Watchtower):**
The beta service on `servyy-test` is configured with `com.centurylinklabs.watchtower.scope=dev` in `container/bumbleflies/docker-compose.yml`. This means:
- New `bumblecode/web:beta` images are automatically pulled and deployed
- No manual `docker compose up -d beta` needed
- Service auto-updates whenever a new image is built in CI

### Astro Beta Site Messaging

**Hero Section:**
- Headline: "Four ways we work with your team" (German: "Vier Wege, wie wir mit euch arbeiten")
- Emphasis: "your/euch" (italicized) — highlights partnership/WE-YOU relationship
- Shows 4 engagement packages: Quick Start, Use-Case Sprint, AI Adoption, Custom Program
- Component: `src/components/Hero.astro`

**How We Work Section:**
- Heading: "One path. Four stations." (German: "Ein Weg. Vier Stationen.")
- Details the Talk → Decide → Build → Embed methodology
- Component: `src/components/StationFlow.astro`

**Messaging Alignment:**
- Hero emphasizes *offering flexibility* (4 engagement options)
- StationFlow emphasizes *consistent methodology* (one proven process)
- Both sections are visually distinct on the homepage but convey complementary messages

**Assets:**
- Favicon: `public/favicon.ico` (reused from Jekyll legacy site, linked in `src/components/Layout.astro`)

## Architecture & Key Concepts

### Directory Structure

```
bumbleflies.github.io/
├── _pages/              # Markdown pages (in _pages/ not root)
├── _layouts/            # Page templates (default, standard, compose, google-form, redirect)
├── _includes/           # Reusable template components
├── _data/               # YAML data files for configuration
│   ├── navigation.yml   # Main navigation menu
│   ├── team.yml         # Team member data
│   ├── style.yml        # Color and image variables
│   └── ...
├── _i18n/               # Translation files (en.yml, de.yml)
├── _sass/               # SCSS stylesheets
│   ├── base/            # Variables, mixins, page styles
│   ├── components/      # Buttons, navbar
│   └── layout/          # Masthead, services, team, contact, footer
├── assets/
│   ├── css/             # Compiled CSS (bumble.scss is the main source)
│   ├── img/             # Images (organized by section)
│   ├── js/              # JavaScript
│   └── fonts/           # Font files
├── _tests/              # Python pytest tests
└── _config.yml          # Jekyll configuration
```

### Page Template Structure

Every markdown file in `_pages/` requires front matter:

```yaml
---
layout: <layout-name>           # e.g., standard, default, compose
namespace: <name>               # Used for translated URL resolution with {% tl %}
permalink: <url-de>             # German URL path
permalink_en: <url-en>          # English URL path
nav_highlight: <i18n-key>       # Navigation item to highlight
title: <i18n-key>               # Page title (resolved from i18n)
---
```

Common layouts:
- **default**: Basic layout with header/footer
- **standard**: Standard page layout
- **compose**: Composite layout for multi-section pages
- **google-form**: Embeds a Google Form
- **redirect**: Redirect page

### Internationalization (i18n)

The site uses `jekyll-multiple-languages-plugin` with translations in `_i18n/en.yml` and `_i18n/de.yml`.

Key patterns:
- **Page-level translation**: Front matter `title:` field references an i18n key
- **Template-level translation**: `{% t key.to.look.up %}` (simple variables only)
- **Chaining filters**: Use `{% capture %}` to capture translated content before applying filters
  ```liquid
  {% capture translated_content %}{% t key.to.look.up %}{% endcapture %}
  {{ translated_content | markdownify }}
  ```

URL translations: Use `{% tl namespace %}` in templates to resolve the current page's localized URL.

### Styling & Design System

**Color & Image Variables** (`_data/style.yml`):
- Defines primary colors, images, and other design tokens
- Variables are accessible in SCSS as `{{ site.data.style.variable-name }}`

**SCSS Processing** (`bumble.scss`):
- Compiles with Jekyll's SCSS processor (note the YAML front matter)
- Imports SCSS variables from `_data/style.yml`
- Organizes styles into: base, components, and layout modules
- Header images are defined in `_header_images.scss`

**Adding Background Images**:
1. Add YAML entry to `_data/style.yml` (e.g., `new-page-image: "/assets/img/new.webp"`)
2. Import as SCSS variable in `bumble.scss` (e.g., `$new-page-image: "{{ site.data.style.new-page-image }}"`)
3. Create style rule in `_sass/_header_images.scss`
4. (Optional) Add preload link to `_includes/head.html` for performance
5. Use the CSS class in page YAML: `header: image-class: new-page-image`

### Testing

Tests are in `_tests/` and validate the *built* site (`_site/`). The test fixture automatically:
1. Builds Jekyll to `_test_site/`
2. Runs an HTTP server on localhost:8000
3. Executes tests against the running site

Key test modules:
- **test_on_every_page.py**: Common checks (links, headers, structure)
- **test_on_every_en_page.py**: English-specific checks
- **test_homepage_team.py**: Team section validation
- **test_rich_results.py**: Schema.org markup validation
- **test_sitemap.py**: Sitemap validation
- **test_redirects.py**: URL redirect validation

## Data Files & Configuration

### `_data/` Files

- **navigation.yml**: Menu structure (uses i18n keys for labels)
- **team.yml**: Team member data (image paths, names, roles)
- **style.yml**: Design tokens (colors, image paths)
- **footer.yml**: Footer configuration
- **social.yml**: Social media links
- **image.yml**: Image metadata
- **files.yml**: File references

All `_data/` values are accessible in templates via `site.data.<filename>.<key>`.

### `_config.yml` Important Settings

```yaml
languages: ["de", "en"]           # Supported languages
default_locale_in_subfolder: false # Don't use /de/, /en/ subfolders
locale: "de-DE"                    # Default locale
exclude_from_localizations: [...]  # Don't translate these assets
plugins:                           # Active Jekyll plugins
  - jekyll-multiple-languages-plugin
  - jekyll-github-metadata
  - jekyll-redirect-from
  - jekyll-agency
```

## Common Workflows

### Adding a New Page

1. Create markdown file in `_pages/` (e.g., `_pages/new-section/my-page.md`)
2. Add front matter with `layout`, `namespace`, `permalink_de`, `permalink_en`, `nav_highlight`, and `title`
3. Add translation keys to `_i18n/en.yml` and `_i18n/de.yml`
4. Update `_data/navigation.yml` if it should appear in nav
5. Add any required background images following the image workflow above
6. Run `bundle exec jekyll serve` to test locally
7. Run `pytest _tests/` to validate

### Updating Translations

1. Edit `_i18n/en.yml` (English) and `_i18n/de.yml` (German)
2. Use hierarchical keys (e.g., `pages.section.key`)
3. Rebuild site to see changes: `bundle exec jekyll build`

### Modifying Navigation

Edit `_data/navigation.yml` to add/remove menu items. Navigation items reference i18n keys for labels and page namespaces for URL resolution.

### Updating Team Data

Edit `_data/team.yml` with member details. The layout in `_includes/team.html` renders this data. Images should be placed in `assets/img/team/`.

## Deployment & CI/CD

The site has a multi-stage deployment pipeline (via GitHub Actions):

- **Build & Test** (part_build_test.yml): Builds Jekyll, uploads artifacts, runs pytest
- **Deploy to Stage** (part_deploy_stage.yml): Deploys to staging environment
- **Deploy to Live** (part_deploy_live.yml): Deploys to production

Triggered by: `build-deploy.yml` workflow orchestrator.

## Notes & Quirks

- **Page location**: Pages go in `_pages/`, not the root directory.
- **i18n Chaining**: `{% t key | filter %}` does NOT work; use `{% capture %}` instead.
- **SCSS Processing**: `bumble.scss` must have YAML front matter (`---`) for Jekyll to process it.
- **Font Awesome**: New FA icons must be added to `_purge/purge-fa.py` before running the purge script.
- **Bundler Permissions**: Modern Ruby/Bundler may require configuring a user-writable gems cache.
- **Site Directory**: The built site goes to `_site/` (or `_test_site/` during tests).
- **Link Handling**: Test suite validates all links; broken redirects or missing translations will fail CI/CD.

## Troubleshooting

**Build fails with permission error**: Run `bundle config path ~/.gems_cache` (see README.md).

**Tests fail**: Ensure `bundle exec jekyll build` succeeded. If markup changed, verify `_includes/` and `_layouts/` are correct.

**Styles not updating**: Clear Jekyll cache and rebuild: `rm -rf _site && bundle exec jekyll build`.

**i18n keys missing**: Check both `_i18n/en.yml` and `_i18n/de.yml` have matching keys at the same path.

## Redesign Phase Status

See `PHASE_1_SUMMARY.md` in the worktree root for completed work, GitHub Actions setup, and next phases (2-6).

**Current phase:** Phase 1 Complete (Scaffold, CI/CD, Core Components)

**Next phases:** Design System, Page Templates, Content Migration, DecapCMS Setup, Review, Go Live (3-4 weeks remaining)

**Key Reference Docs:**
- `/home/cda/dev/infrastructure/bumbleflies/PROJECT_HANDOFF.md` — Complete spec (1000+ lines)
- `/home/cda/dev/infrastructure/bumbleflies/DELIVERABLES_SUMMARY.md` — Quick reference
- `/home/cda/dev/infrastructure/bumbleflies/REDESIGN_SPEC.md` — Design details
- `/home/cda/dev/infrastructure/bumbleflies/CASE_STUDIES_REAL.md` — Case study templates
