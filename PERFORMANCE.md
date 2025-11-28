# Performance Optimization Guide

This document describes the performance optimization strategy implemented for the bumbleflies.de website and provides guidelines for maintaining optimal performance.

## Table of Contents

1. [Overview](#overview)
2. [Critical Rendering Path Optimization](#critical-rendering-path-optimization)
3. [Font Loading Strategy](#font-loading-strategy)
4. [Image Optimization](#image-optimization)
5. [JavaScript Optimization](#javascript-optimization)
6. [Performance Targets](#performance-targets)
7. [Testing & Validation](#testing--validation)
8. [Best Practices](#best-practices)

## Overview

The performance optimization strategy focuses on improving Core Web Vitals and achieving Lighthouse Performance scores > 90. Key optimizations include:

- **Critical CSS inlining** to eliminate render-blocking stylesheets
- **Font preloading** with font-display: swap to prevent FOIT
- **Deferred CSS loading** for non-critical stylesheets
- **JavaScript deferral** to prevent blocking
- **Lazy loading** for images with smooth transitions
- **Resource hints** (dns-prefetch, preconnect) for faster external resource loading

## Critical Rendering Path Optimization

### What is Critical vs Non-Critical CSS?

**Critical CSS** is the minimal CSS required to render above-the-fold content on the initial page load. This includes:

- CSS variables (design tokens)
- Base typography and reset styles
- Navigation bar styles
- Hero/masthead styles (header)
- Layout grid (Bootstrap container/row essentials)
- Dark mode variables

**Non-Critical CSS** includes everything else:

- Bootstrap full framework
- Font Awesome icons
- Custom components below the fold
- Footer styles
- Form styles
- Animations and transitions

### Implementation

#### Critical CSS Inlining

File: `_includes/critical-css.html`

Critical CSS is inlined directly in the `<head>` section of every page for immediate availability without requiring an HTTP request. This CSS is kept under 14KB to fit within the first HTTP/2 packet.

**How to update critical CSS:**

1. Identify above-the-fold elements on your most important pages
2. Extract only the CSS needed for those elements
3. Include design tokens (CSS variables) that are used everywhere
4. Test on mobile viewport (smallest screen size)
5. Validate size: `wc -c _includes/critical-css.html` should be < 14000 bytes

#### Deferred Non-Critical CSS

File: `_includes/head.html`

Non-critical stylesheets are loaded using the "media print trick":

```html
<link rel="preload" href="style.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
<link rel="stylesheet" href="style.css" media="print" onload="this.media='all'">
```

This technique:
1. Preloads the stylesheet asynchronously
2. Loads it with `media="print"` (doesn't block rendering)
3. Changes media to `all` when loaded via JavaScript
4. Falls back to normal `<link>` in `<noscript>` for non-JS browsers

**Files loaded this way:**
- `bootstrap.min.css` - Full Bootstrap framework
- `all.min.css` - Font Awesome icons
- `font-faces.css` - Font face declarations
- `custom.css` - Custom link styling
- `bumble.css` - Main compiled SCSS
- `flag-icons.min.css` - Language flag icons

## Font Loading Strategy

### Preloading Critical Fonts

File: `_includes/font-preload.html`

Critical fonts are preloaded to ensure they're available as soon as possible:

**Preloaded fonts:**
1. **Montserrat Bold (700)** - Used for headings in hero/masthead
2. **Montserrat Regular (400)** - Used for secondary headings
3. **Roboto Condensed Regular** - Used for body text

**Why these fonts?**
These are the fonts used in above-the-fold content. Preloading them prevents layout shifts and ensures text is visible immediately.

### Font Display Strategy

File: `assets/css/font-faces.css`

All font faces use `font-display: swap` to prevent FOIT (Flash of Invisible Text):

```css
@font-face {
  font-family: 'Montserrat';
  font-display: swap;
  /* ... */
}
```

**What this means:**
- Text is shown immediately using fallback fonts
- Custom fonts swap in when loaded
- No invisible text during font loading

### Font Format Priority

Fonts are declared with multiple formats for browser compatibility:

1. **WOFF2** - Modern browsers (best compression, preferred)
2. **WOFF** - Older modern browsers
3. **TTF** - Legacy browsers
4. **EOT/SVG** - Very old browsers (IE9, legacy iOS)

**File locations:**
- `/assets/font/*.woff2` - Primary format
- `/assets/font/*.woff` - Fallback format

## Image Optimization

### Lazy Loading Utilities

File: `_sass/utilities/_lazy-load.scss`

Comprehensive lazy loading styles with multiple strategies:

#### 1. Native Lazy Loading

Use HTML's native `loading="lazy"` attribute for automatic lazy loading:

```html
<img src="image.webp" loading="lazy" alt="Description">
```

**When to use:**
- All images below the fold
- Gallery images
- Team photos
- Any non-critical images

**When NOT to use:**
- Hero/masthead background images (preloaded instead)
- Logo
- Above-the-fold content images

#### 2. Blur-Up Effect

For progressive loading with blur placeholders:

```html
<div class="lazy-image-wrapper">
  <img src="placeholder-small.jpg" class="lazy-placeholder" alt="">
  <img data-src="full-image.jpg" loading="lazy" alt="Description">
</div>
```

**How it works:**
1. Small blurred placeholder loads immediately
2. Full image loads lazily
3. Placeholder fades out when full image loads

#### 3. Skeleton Loading

For content blocks while loading:

```html
<div class="lazy-skeleton">
  Loading content...
</div>
```

Add `.loaded` class via JavaScript when content is ready.

#### 4. Aspect Ratio Boxes

Prevent Cumulative Layout Shift (CLS):

```html
<div class="lazy-aspect-ratio ratio-16-9">
  <img src="image.webp" loading="lazy" alt="Description">
</div>
```

**Available ratios:**
- `.ratio-16-9` - Widescreen (56.25%)
- `.ratio-4-3` - Standard (75%)
- `.ratio-1-1` - Square (100%)
- `.ratio-3-2` - Classic photo (66.67%)
- `.ratio-21-9` - Ultrawide (42.86%)

### Image Preloading

File: `_includes/head.html`

Critical images are preloaded with priority hints:

```html
<!-- High priority for hero image -->
<link rel="preload" as="image" fetchpriority="high" href="{{ site.data.style.header-image }}" type="image/webp">

<!-- Low priority for below-fold images -->
<link rel="preload" as="image" fetchpriority="low" href="{{ site.data.style.accceu-image }}" type="image/webp">
```

**Priority levels:**
- `fetchpriority="high"` - Above-the-fold, critical images
- `fetchpriority="low"` - Below-the-fold, nice-to-have images
- No attribute - Default browser priority

### Image Format Recommendations

1. **WebP** - Use for all images (supported by all modern browsers)
2. **AVIF** - Consider for even better compression (newer format)
3. **Provide fallbacks** - Use `<picture>` element for older browsers:

```html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" loading="lazy" alt="Description">
</picture>
```

### Image Size Guidelines

- **Hero images:** Max 1920x1080px, optimized WebP < 200KB
- **Content images:** Max 1200px width, < 100KB
- **Thumbnails:** 300-600px width, < 50KB
- **Icons:** SVG preferred, or PNG < 10KB

**Optimization tools:**
- ImageOptim (Mac)
- Squoosh.app (web-based)
- cwebp (command line for WebP)

## JavaScript Optimization

### Deferral Strategy

File: `_layouts/default.html`

All JavaScript is deferred to prevent render blocking:

```html
<!-- Critical dependencies loaded with defer -->
<script src="jquery-slim.min.js" defer></script>
<script src="bootstrap.bundle.min.js" defer></script>

<!-- Custom scripts loaded with defer -->
<script src="agency.min.js" defer></script>
```

**defer vs async:**

- **defer:** Downloads in parallel, executes after HTML parsing (maintains order)
- **async:** Downloads in parallel, executes immediately (breaks order)

**When to use defer:**
- Scripts that depend on DOM being ready
- Scripts with dependencies on other scripts
- Most third-party libraries (jQuery, Bootstrap)

**When to use async:**
- Analytics scripts (Google Analytics, etc.)
- Third-party widgets that are self-contained
- Ads scripts

### Inline JavaScript

Small, critical JavaScript is inlined at the end of `<body>` for immediate execution:

**Current inline scripts:**
- Lazy loading enhancement (adds `.loaded` class to images)
- Intersection Observer fallback for older browsers

**Guidelines for inline scripts:**
- Keep under 1KB if possible
- Only for critical functionality
- No external dependencies
- Works without defer/async

## Performance Targets

### Core Web Vitals

Target metrics for optimal user experience:

| Metric | Target | Good | Needs Improvement | Poor |
|--------|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | < 2.5s | < 2.5s | 2.5s - 4.0s | > 4.0s |
| **FID** (First Input Delay) | < 100ms | < 100ms | 100ms - 300ms | > 300ms |
| **CLS** (Cumulative Layout Shift) | < 0.1 | < 0.1 | 0.1 - 0.25 | > 0.25 |
| **FCP** (First Contentful Paint) | < 1.5s | < 1.8s | 1.8s - 3.0s | > 3.0s |
| **TBT** (Total Blocking Time) | < 200ms | < 200ms | 200ms - 600ms | > 600ms |

### Lighthouse Scores

Target Lighthouse scores across categories:

- **Performance:** > 90 (primary focus)
- **Accessibility:** > 95
- **Best Practices:** > 95
- **SEO:** > 95

### Page Weight Targets

Optimize for fast loading even on slower connections:

- **Initial HTML:** < 50KB (compressed with gzip/brotli)
- **Critical CSS:** < 14KB (inlined)
- **Total CSS:** < 100KB (all stylesheets combined)
- **Total JS:** < 150KB (all scripts combined)
- **Total Page Weight:** < 1MB (including all resources)

### Speed Index Targets

Measure how quickly content is visually displayed:

- **3G Connection:** < 5s
- **4G Connection:** < 2s
- **Desktop/WiFi:** < 1s

## Testing & Validation

### Tools for Performance Testing

#### 1. Lighthouse (Chrome DevTools)

**How to run:**
1. Open Chrome DevTools (F12)
2. Go to "Lighthouse" tab
3. Select "Performance" category
4. Click "Analyze page load"

**What to check:**
- Performance score > 90
- Metrics (LCP, TBT, CLS)
- Opportunities (render-blocking resources)
- Diagnostics (minimize main-thread work)

#### 2. PageSpeed Insights

**URL:** https://pagespeed.web.dev/

**How to use:**
1. Enter your page URL
2. Run test for both Mobile and Desktop
3. Check Core Web Vitals
4. Review field data (real user metrics)

**Key sections:**
- Core Web Vitals Assessment
- Opportunities (potential improvements)
- Diagnostics (issues to fix)
- Passed Audits (what's working)

#### 3. WebPageTest

**URL:** https://www.webpagetest.org/

**Advanced testing:**
1. Enter URL
2. Select test location and device
3. Choose connection speed (3G, 4G, Cable)
4. Run test

**Metrics to check:**
- Speed Index
- First Byte Time
- Start Render
- Visually Complete
- Filmstrip view (visual progress)
- Waterfall chart (resource loading)

#### 4. Chrome User Experience Report (CrUX)

**What it is:** Real user metrics from Chrome users

**How to access:**
- PageSpeed Insights (field data section)
- Chrome DevTools > Lighthouse > View Trace
- BigQuery (for detailed analysis)

**Why it matters:** Shows actual user experience, not just synthetic tests

### Local Testing

#### Build and serve locally:

```bash
# Build site
bundle exec jekyll build

# Serve locally
bundle exec jekyll serve

# Test with Chrome Lighthouse
# Open http://localhost:4000 in Chrome
# Run Lighthouse audit
```

#### Test critical CSS size:

```bash
# Check critical CSS file size (should be < 14000 bytes)
wc -c _includes/critical-css.html

# Check if critical CSS is being inlined
curl http://localhost:4000 | grep -A 100 "Critical CSS"
```

#### Validate deferred CSS:

```bash
# Check that stylesheets are deferred
curl http://localhost:4000 | grep 'media="print"'

# Verify preload hints
curl http://localhost:4000 | grep 'rel="preload"'
```

### Performance Budget

Set performance budgets to prevent regressions:

**Resource budgets:**
```json
{
  "html": { "max": 50 },
  "css": { "max": 100 },
  "js": { "max": 150 },
  "images": { "max": 500 },
  "fonts": { "max": 100 }
}
```

**Timing budgets:**
```json
{
  "FCP": 1500,
  "LCP": 2500,
  "TBT": 200,
  "CLS": 0.1
}
```

**How to enforce:**
- Use Lighthouse CI in GitHub Actions
- Fail builds if budgets exceeded
- Monitor trends over time

## Best Practices

### Adding New CSS

**For critical CSS:**
1. Add only if needed above-the-fold
2. Keep total size under 14KB
3. Test on mobile viewport
4. Use CSS variables when possible

**For non-critical CSS:**
1. Add to appropriate SCSS file in `_sass/`
2. Let Jekyll compilation handle it
3. Will be automatically deferred

**Avoid:**
- Inline styles in HTML (use classes)
- `!important` (proper specificity instead)
- Large vendor prefixes (use autoprefixer)

### Adding New Fonts

**Before adding:**
1. Check if existing fonts can work
2. Consider system font stack as alternative
3. Evaluate file size impact

**If necessary:**
1. Host fonts locally (don't use Google Fonts CDN)
2. Use WOFF2 format (best compression)
3. Add to `assets/font/` directory
4. Declare in `assets/css/font-faces.css` with `font-display: swap`
5. Preload in `_includes/font-preload.html` if critical
6. Subset fonts to include only needed glyphs

**Font subsetting:**
```bash
# Install pyftsubset
pip install fonttools

# Subset to Latin characters only
pyftsubset font.ttf \
  --output-file=font-subset.woff2 \
  --flavor=woff2 \
  --layout-features="*" \
  --unicodes="U+0020-007F,U+00A0-00FF"
```

### Adding New Images

**Image checklist:**
1. Use WebP format (or AVIF for even better compression)
2. Optimize before adding to repo
3. Add responsive images with `srcset` if multiple sizes needed
4. Use `loading="lazy"` for below-the-fold images
5. Provide `width` and `height` attributes to prevent CLS
6. Use descriptive `alt` text for accessibility

**Optimization workflow:**
```bash
# Convert to WebP
cwebp -q 85 input.jpg -o output.webp

# Optimize WebP
cwebp -q 85 -m 6 -af input.jpg -o output.webp

# For PNGs with transparency
cwebp -q 85 -m 6 -alpha_q 85 input.png -o output.webp
```

**Responsive images:**
```html
<img src="image-800w.webp"
     srcset="image-400w.webp 400w,
             image-800w.webp 800w,
             image-1200w.webp 1200w"
     sizes="(max-width: 600px) 400px,
            (max-width: 1000px) 800px,
            1200px"
     loading="lazy"
     width="1200"
     height="800"
     alt="Description">
```

### Adding New JavaScript

**Decision tree:**

1. **Is it critical for initial render?**
   - Yes → Inline in `<head>` (keep tiny, < 1KB)
   - No → Continue to step 2

2. **Does it depend on other scripts?**
   - Yes → Use `defer` attribute
   - No → Continue to step 3

3. **Is it third-party/analytics?**
   - Yes → Use `async` attribute
   - No → Use `defer` attribute

**Example:**
```html
<!-- Critical, tiny script - inline -->
<script>/* Critical JS */</script>

<!-- Depends on jQuery - defer -->
<script src="app.js" defer></script>

<!-- Analytics - async -->
<script src="analytics.js" async></script>
```

### Maintaining Performance

**Regular checks:**
1. Run Lighthouse audit before every release
2. Monitor Core Web Vitals via PageSpeed Insights
3. Check page weight hasn't increased significantly
4. Test on slow 3G connection periodically
5. Review and update critical CSS when layout changes

**Regression prevention:**
1. Set up Lighthouse CI in GitHub Actions
2. Fail builds if performance score drops below threshold
3. Review performance impact of new dependencies
4. Regular audits of unused CSS/JS

**Monitoring:**
1. Use Google Search Console for Core Web Vitals
2. Set up Real User Monitoring (RUM) if needed
3. Track performance trends over time
4. Alert on performance degradation

### Jekyll Build Performance

**Optimizing Jekyll builds:**

```bash
# Build with production settings
JEKYLL_ENV=production bundle exec jekyll build

# Incremental builds (development only)
bundle exec jekyll build --incremental

# Profile build to find slow steps
bundle exec jekyll build --profile
```

**Jekyll performance tips:**
1. Minimize use of expensive Liquid filters
2. Cache computed values in data files
3. Use includes sparingly (they add build time)
4. Consider static JSON API generation instead of runtime generation

### Purging Unused CSS

File: `_purge/purge.sh`

Regular CSS purging removes unused styles:

```bash
cd _purge
./purge.sh
```

**What it does:**
1. Downloads latest CSS from live site
2. Builds site to `_site/`
3. Analyzes which CSS is actually used
4. Removes unused CSS rules
5. Optimizes Font Awesome subset
6. Updates font files

**When to run:**
- After major CSS changes
- Before major releases
- When adding new Font Awesome icons
- Monthly maintenance

**Important:** Add new Font Awesome icons to `_purge/purge-fa.py` before purging.

## Troubleshooting

### Common Issues

#### Issue: Critical CSS exceeds 14KB

**Solution:**
1. Remove non-critical styles from `_includes/critical-css.html`
2. Focus only on above-the-fold content
3. Use CSS variables more (they compress well)
4. Minify inline CSS (remove comments, whitespace)

#### Issue: Fonts loading slowly

**Solution:**
1. Verify fonts are preloaded in `_includes/font-preload.html`
2. Check `font-display: swap` is set in font-faces
3. Subset fonts to reduce file size
4. Use fewer font weights/styles if possible

#### Issue: Images causing layout shifts (high CLS)

**Solution:**
1. Add explicit `width` and `height` attributes to images
2. Use aspect ratio containers (`.lazy-aspect-ratio`)
3. Ensure background images have min-height set
4. Preload critical images

#### Issue: JavaScript blocking rendering

**Solution:**
1. Verify all `<script>` tags have `defer` or `async`
2. Move non-critical scripts to end of `<body>`
3. Consider code splitting for large scripts
4. Minimize inline scripts

#### Issue: Low Lighthouse score despite optimizations

**Checklist:**
1. Clear browser cache and re-test
2. Test in incognito mode
3. Check for render-blocking resources in waterfall
4. Verify critical CSS is actually inlined
5. Test on mobile device, not just emulator
6. Check for large third-party scripts

### Debug Tools

**Chrome DevTools Performance tab:**
1. Record page load
2. Look for long tasks (> 50ms)
3. Check for layout shifts
4. Identify render-blocking resources

**Coverage tab:**
1. Open DevTools > Coverage
2. Record page load
3. See unused CSS/JS percentages
4. Consider removing or lazy-loading unused code

**Network tab:**
1. Check resource sizes
2. Verify compression (gzip/brotli)
3. Look for 404s or failed requests
4. Check resource timing

## Resources

### Official Documentation

- [Web.dev - Web Vitals](https://web.dev/vitals/)
- [MDN - Performance](https://developer.mozilla.org/en-US/docs/Web/Performance)
- [Google PageSpeed Insights](https://pagespeed.web.dev/)
- [Lighthouse Documentation](https://developers.google.com/web/tools/lighthouse)

### Tools

- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)
- [WebPageTest](https://www.webpagetest.org/)
- [Squoosh - Image Optimization](https://squoosh.app/)
- [Font Subsetter](https://everythingfonts.com/subsetter)

### Articles & Guides

- [Critical CSS](https://web.dev/extract-critical-css/)
- [Font Loading Strategies](https://web.dev/font-best-practices/)
- [Lazy Loading Images](https://web.dev/lazy-loading-images/)
- [Optimizing JavaScript](https://web.dev/fast/#optimize-your-javascript)

---

**Last Updated:** 2025-11-28

**Maintained by:** bumbleflies development team

For questions or suggestions, please open an issue on GitHub.
