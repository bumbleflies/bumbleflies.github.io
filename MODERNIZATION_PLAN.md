# Modernization Plan: Bumbleflies Website

## Overview

Modernize the bumbleflies.de Jekyll website with a clean, organic design, dark mode support, and enhanced storytelling, while maintaining bilingual functionality and SEO. Test changes in a beta environment at `/beta/` before production rollout.

## Design Goals

- **Visual Style**: Organic/warm aesthetic (Airbnb/Notion-inspired) with rounded corners, soft shadows, friendly community feel
- **Brand Colors**: Bumble yellow (#f1c232), Bumble gray (#5e5e5e), Flies gray (#999999) with tasteful variations
- **Dark Mode**: Automatic based on system preference (prefers-color-scheme)
- **Storytelling**: Enhanced visual narratives showcasing team, impact, client success, and community

## Implementation Phases

### Phase 1: Beta Environment Setup

**Goal**: Create isolated `/beta/` testing environment without affecting live site

**Files to Create**:
- `_config_beta.yml` - Beta-specific Jekyll configuration with baseurl: "/beta"
- `.github/workflows/build-deploy-beta.yml` - Beta deployment workflow

**Files to Modify**:
- `_includes/head.html` - Add noindex meta tag for beta
- `_layouts/default.html` - Add beta environment indicator banner

**Implementation Steps**:
1. Create `_config_beta.yml`:
   ```yaml
   baseurl: "/beta"
   url: "https://bumbleflies.de"
   beta_mode: true
   # Inherit all other settings from _config.yml
   ```

2. Add GitHub Actions workflow for beta builds:
   - Trigger: pushes to `beta` branch
   - Build command: `jekyll build -c _config.yml,_config_beta.yml`
   - Deploy to `/beta/` path on staging server

3. Add beta indicator banner in layouts:
   ```liquid
   {% if site.beta_mode %}
   <div class="beta-banner">BETA - Testing New Design</div>
   {% endif %}
   ```

**Success Criteria**:
- Beta site accessible at bumbleflies.de/beta/
- All URLs properly prefixed with /beta/
- Beta banner visible
- Tests pass against beta build

---

### Phase 2: Modern Color System with Dark Mode

**Goal**: Implement CSS variable-based color system supporting automatic dark mode

**Files to Create**:
- `_sass/base/_css-variables.scss` - Core color system with dark mode support
- `_sass/themes/_dark-mode.scss` - Dark mode overrides

**Files to Modify**:
- `_data/style.yml` - Update color definitions
- `assets/css/bumble.scss` - Import new color system
- `_sass/components/_navbar.scss` - Use CSS variables
- `_sass/layout/_masthead.scss` - Use CSS variables
- All component SCSS files - Replace hard-coded colors

**Implementation Steps**:

1. Create CSS variables in `_sass/base/_css-variables.scss`:
   ```scss
   :root {
     /* Brand Colors */
     --color-bumble-yellow: #f1c232;
     --color-bumble-yellow-light: #f7dc6f;
     --color-bumble-yellow-dark: #d4a017;
     --color-bumble-gray: #5e5e5e;
     --color-flies-gray: #999999;

     /* Semantic Colors - Light Mode */
     --color-primary: var(--color-bumble-yellow);
     --color-background: #ffffff;
     --color-surface: #f8f9fa;
     --color-text: #212529;
     --color-text-muted: #6c757d;
     --color-border: #dee2e6;

     /* Spacing & Effects */
     --border-radius: 12px;
     --border-radius-sm: 8px;
     --border-radius-lg: 16px;
     --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.08);
     --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.12);
     --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.16);
   }
   ```

2. Add dark mode overrides:
   ```scss
   @media (prefers-color-scheme: dark) {
     :root {
       --color-primary: #f7dc6f; /* Lighter yellow for dark bg */
       --color-background: #1a1a1a;
       --color-surface: #2d2d2d;
       --color-text: #e0e0e0;
       --color-text-muted: #a0a0a0;
       --color-border: #404040;
       --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.3);
       --shadow-md: 0 4px 16px rgba(0, 0, 0, 0.4);
       --shadow-lg: 0 8px 24px rgba(0, 0, 0, 0.5);
     }
   }
   ```

3. Update `_data/style.yml`:
   ```yaml
   # Remove hard-coded highlight color
   # Colors now managed via CSS variables
   ```

4. Replace color usage throughout SCSS:
   - `color: $primary` → `color: var(--color-primary)`
   - `background: #fff` → `background: var(--color-background)`
   - `color: #212529` → `color: var(--color-text)`

**Success Criteria**:
- Dark mode automatically activates based on OS/browser preference
- All colors properly switch in dark mode
- Brand colors maintain proper contrast ratios (WCAG AA)
- No hard-coded colors remain in SCSS

---

### Phase 3: Modern Design System

**Goal**: Implement organic, warm design patterns with rounded corners, soft shadows, modern typography

**Files to Create**:
- `_sass/base/_typography-modern.scss` - Enhanced font system
- `_sass/components/_cards.scss` - Card component system
- `_sass/components/_buttons-modern.scss` - Modern button styles
- `_sass/layout/_grid-modern.scss` - Flexible grid system

**Files to Modify**:
- `_sass/base/_mixins.scss` - Update font mixins
- `_sass/components/_navbar.scss` - Modern nav styling with blur effect
- `_sass/layout/_masthead.scss` - Softer hero sections
- `_sass/layout/gallery-hover.scss` - Smoother transitions
- `assets/css/custom.css` - Remove in favor of organized SCSS

**Implementation Steps**:

1. Enhanced Typography (`_sass/base/_typography-modern.scss`):
   ```scss
   :root {
     --font-heading: "Montserrat", -apple-system, system-ui, sans-serif;
     --font-body: "Noto Sans", -apple-system, system-ui, sans-serif;
     --font-serif: "Noto Serif", Georgia, serif;

     --font-size-xs: 0.75rem;
     --font-size-sm: 0.875rem;
     --font-size-base: 1rem;
     --font-size-lg: 1.125rem;
     --font-size-xl: 1.25rem;
     --font-size-2xl: 1.5rem;
     --font-size-3xl: 1.875rem;
     --font-size-4xl: 2.25rem;
   }

   body {
     font-family: var(--font-body);
     font-size: var(--font-size-base);
     color: var(--color-text);
     background: var(--color-background);
     line-height: 1.6;
   }

   h1, h2, h3, h4, h5, h6 {
     font-family: var(--font-heading);
     font-weight: 600;
     line-height: 1.2;
   }
   ```

2. Card System (`_sass/components/_cards.scss`):
   ```scss
   .card-modern {
     background: var(--color-surface);
     border-radius: var(--border-radius);
     box-shadow: var(--shadow-sm);
     padding: 2rem;
     transition: all 0.3s ease;

     &:hover {
       box-shadow: var(--shadow-md);
       transform: translateY(-4px);
     }
   }
   ```

3. Modern Buttons (`_sass/components/_buttons-modern.scss`):
   ```scss
   .btn-modern {
     border-radius: var(--border-radius-sm);
     padding: 0.75rem 1.5rem;
     font-weight: 500;
     box-shadow: var(--shadow-sm);
     transition: all 0.2s ease;

     &:hover {
       box-shadow: var(--shadow-md);
       transform: translateY(-2px);
     }
   }
   ```

4. Modern Navigation with blur effect:
   ```scss
   .navbar {
     background: rgba(255, 255, 255, 0.9);
     backdrop-filter: blur(10px);
     box-shadow: var(--shadow-sm);

     @media (prefers-color-scheme: dark) {
       background: rgba(26, 26, 26, 0.9);
     }
   }
   ```

5. Softer hero sections with overlays:
   ```scss
   .masthead {
     border-radius: 0 0 var(--border-radius-lg) var(--border-radius-lg);
     position: relative;

     &::after {
       content: '';
       position: absolute;
       inset: 0;
       background: linear-gradient(
         to bottom,
         rgba(0, 0, 0, 0.3),
         rgba(0, 0, 0, 0.5)
       );
       border-radius: inherit;
     }
   }
   ```

**Success Criteria**:
- Consistent rounded corners across all components
- Soft shadows with proper dark mode variants
- Smooth transitions and hover effects
- Typography scales properly on mobile
- All components feel cohesive and "warm"

---

### Phase 4: Storytelling Enhancements

**Goal**: Add components for metrics, testimonials, enhanced team profiles, and photo stories

**Files to Create**:
- `_includes/metrics.html` - Impact metrics showcase
- `_includes/testimonials.html` - Client testimonial carousel
- `_includes/team-enhanced.html` - Enhanced team profiles with bios
- `_includes/photo-story.html` - Photo gallery with captions/stories
- `_data/metrics.yml` - Impact statistics data
- `_data/testimonials.yml` - Client testimonial data

**Files to Modify**:
- `_data/team.yml` - Add bio, expertise, fun facts
- `_pages/about.md` - Use enhanced components
- `_pages/index.md` - Add metrics to homepage
- `_includes/gallery.html` - Add caption support

**Implementation Steps**:

1. **Impact Metrics Component** (`_includes/metrics.html`):
   ```html
   <section class="metrics-section">
     <div class="container">
       <h2>{% t pages.metrics.title %}</h2>
       <div class="metrics-grid">
         {% for metric in site.data.metrics %}
         <div class="metric-card card-modern">
           <div class="metric-icon">{{ metric.icon }}</div>
           <div class="metric-value">{{ metric.value }}</div>
           <div class="metric-label">{% t metric.label %}</div>
         </div>
         {% endfor %}
       </div>
     </div>
   </section>
   ```

2. **Metrics Data** (`_data/metrics.yml`):
   ```yaml
   - icon: "🎯"
     value: "200+"
     label: "pages.metrics.events_hosted"
   - icon: "👥"
     value: "3,000+"
     label: "pages.metrics.participants"
   - icon: "🏢"
     value: "50+"
     label: "pages.metrics.organizations"
   - icon: "🌍"
     value: "15+"
     label: "pages.metrics.countries"
   ```

3. **Testimonials Component** (`_includes/testimonials.html`):
   ```html
   <section class="testimonials-section">
     <div class="container">
       <h2>{% t pages.testimonials.title %}</h2>
       <div class="testimonials-carousel">
         {% for testimonial in site.data.testimonials %}
         <div class="testimonial-card card-modern">
           <div class="testimonial-content">
             "{{ testimonial.quote }}"
           </div>
           <div class="testimonial-author">
             <img src="{{ testimonial.avatar }}" alt="{{ testimonial.name }}">
             <div>
               <div class="author-name">{{ testimonial.name }}</div>
               <div class="author-role">{{ testimonial.role }}</div>
               <div class="author-company">{{ testimonial.company }}</div>
             </div>
           </div>
         </div>
         {% endfor %}
       </div>
     </div>
   </section>
   ```

4. **Enhanced Team Profiles** - Update `_data/team.yml`:
   ```yaml
   - name: John Doe
     pic: john.webp
     position: Co-Founder
     social:
       - title: linkedin
         url: https://linkedin.com/in/johndoe
     bio_key: pages.team.john.bio
     expertise:
       - Open Space
       - FAST Agile
       - Facilitation
     fun_fact_key: pages.team.john.fun_fact
   ```

5. **Photo Story Gallery** (`_includes/photo-story.html`):
   ```html
   <div class="photo-story-grid">
     {% for photo in include.photos %}
     <div class="photo-story-item">
       <img src="{{ photo.src }}" alt="{{ photo.alt }}" loading="lazy">
       <div class="photo-caption">
         <h4>{{ photo.title }}</h4>
         <p>{{ photo.description }}</p>
       </div>
     </div>
     {% endfor %}
   </div>
   ```

**Success Criteria**:
- Metrics section displays key achievements prominently
- Testimonials showcase client success stories
- Team profiles tell personal stories and expertise
- Photo galleries have contextual narratives
- All storytelling elements work in both languages

---

### Phase 5: Performance Optimizations

**Goal**: Optimize loading performance, fonts, images, and add progressive enhancement

**Files to Create**:
- `_includes/critical-css.html` - Inlined critical CSS
- `sw.js` - Service worker for offline caching
- `_sass/utilities/_lazy-load.scss` - Lazy loading styles

**Files to Modify**:
- `_includes/head.html` - Critical CSS, resource hints, font optimization
- `_layouts/default.html` - Service worker registration
- `assets/css/bumble.scss` - Split into critical and deferred
- `_purge/purge.sh` - Update for new CSS structure

**Implementation Steps**:

1. **Critical CSS Strategy**:
   - Inline above-the-fold CSS in `<head>`
   - Defer non-critical CSS with `media="print" onload="this.media='all'"`
   - Critical: navbar, hero, typography, layout grid
   - Deferred: animations, gallery, footer, forms

2. **Font Loading Optimization** in `_includes/head.html`:
   ```html
   <!-- Preconnect to font CDN -->
   <link rel="preconnect" href="https://fonts.googleapis.com">
   <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

   <!-- Preload critical fonts -->
   <link rel="preload" as="font" type="font/woff2"
         href="/assets/fonts/montserrat-v18-latin-600.woff2" crossorigin>

   <!-- Load fonts with display: swap -->
   <style>
     @font-face {
       font-family: 'Montserrat';
       font-style: normal;
       font-weight: 600;
       font-display: swap;
       src: url('/assets/fonts/montserrat-v18-latin-600.woff2') format('woff2');
     }
   </style>
   ```

3. **Enhanced Image Lazy Loading**:
   ```html
   <img src="placeholder.svg"
        data-src="actual-image.webp"
        loading="lazy"
        class="lazy-image"
        alt="Description">
   ```

4. **Service Worker** (`sw.js`):
   ```javascript
   // Cache static assets
   const CACHE_NAME = 'bumbleflies-v1';
   const urlsToCache = [
     '/',
     '/assets/css/bumble.css',
     '/assets/css/bootstrap.min.css',
     '/assets/img/header-bg.webp'
   ];

   self.addEventListener('install', event => {
     event.waitUntil(
       caches.open(CACHE_NAME)
         .then(cache => cache.addAll(urlsToCache))
     );
   });
   ```

5. **Resource Hints**:
   ```html
   <!-- DNS prefetch for external resources -->
   <link rel="dns-prefetch" href="https://www.google-analytics.com">

   <!-- Preload critical images -->
   <link rel="preload" as="image" href="{{ site.data.style.header-image }}">
   ```

**Success Criteria**:
- Lighthouse Performance score > 90
- First Contentful Paint < 1.5s
- Largest Contentful Paint < 2.5s
- Total Blocking Time < 200ms
- Cumulative Layout Shift < 0.1
- Fonts load without FOUT/FOIT

---

### Phase 6: Testing & Quality Assurance

**Goal**: Ensure quality, accessibility, cross-browser compatibility, and SEO

**Files to Create**:
- `_tests/test_dark_mode.py` - Dark mode CSS validation
- `_tests/test_modern_components.py` - New component testing
- `_tests/test_performance.py` - Performance regression tests
- `_tests/test_accessibility.py` - WCAG compliance tests

**Files to Modify**:
- `_tests/conftest.py` - Add beta build fixture
- `_tests/test_on_every_page.py` - Add modern component checks

**Testing Checklist**:

1. **Functional Testing**:
   - [ ] All pages render correctly in beta
   - [ ] Navigation works with /beta/ prefix
   - [ ] Language switching maintains /beta/ path
   - [ ] Forms submit correctly
   - [ ] Links are not broken
   - [ ] Gallery modals work
   - [ ] Carousels advance properly

2. **Visual Testing**:
   - [ ] Light mode colors match brand guidelines
   - [ ] Dark mode has proper contrast (WCAG AA)
   - [ ] Rounded corners consistent across components
   - [ ] Shadows render properly
   - [ ] Typography scales on mobile
   - [ ] Images lazy load correctly
   - [ ] Animations are smooth (60fps)

3. **Accessibility Testing** (WCAG 2.1 AA):
   - [ ] Color contrast ratios pass (4.5:1 text, 3:1 UI)
   - [ ] Keyboard navigation works
   - [ ] Focus indicators visible
   - [ ] Alt text on all images
   - [ ] ARIA labels on interactive elements
   - [ ] Headings in logical order
   - [ ] Form labels properly associated

4. **Cross-Browser Testing**:
   - [ ] Chrome/Edge (latest 2 versions)
   - [ ] Firefox (latest 2 versions)
   - [ ] Safari (latest 2 versions, iOS)
   - [ ] Dark mode works in all browsers
   - [ ] CSS variables supported (fallbacks if needed)

5. **Performance Testing**:
   - [ ] Lighthouse scores (Performance, Accessibility, Best Practices, SEO)
   - [ ] Core Web Vitals pass
   - [ ] Image optimization verified
   - [ ] CSS/JS minified
   - [ ] No render-blocking resources

6. **SEO Testing**:
   - [ ] Beta has noindex meta tag
   - [ ] Production has proper meta tags
   - [ ] Structured data validates
   - [ ] Sitemap updated
   - [ ] Robots.txt correct

7. **Bilingual Testing**:
   - [ ] All German content displays correctly
   - [ ] All English content displays correctly
   - [ ] Language switcher works in beta
   - [ ] i18n keys resolve properly

**Success Criteria**:
- All pytest tests pass
- Lighthouse scores > 90 across all categories
- No accessibility violations
- Cross-browser compatibility confirmed
- Bilingual functionality maintained

---

### Phase 7: Rollout Strategy

**Goal**: Safe, monitored rollout from beta to production with rollback capability

**Rollout Steps**:

1. **Week 7: Beta Testing** (Current)
   - Deploy to /beta/ path
   - Internal team testing
   - Gather feedback
   - Fix issues

2. **Week 8: Staging Deployment**
   - Merge beta branch to master
   - Deploy to GitHub Pages (staging)
   - Share with select clients for feedback
   - Monitor analytics on staging

3. **Week 9: Production Soft Launch**
   - Deploy to production
   - Keep /beta/ available as feature preview
   - Monitor error logs and analytics
   - A/B test key metrics (bounce rate, time on site, conversions)

4. **Week 10: Full Rollout**
   - Remove beta environment
   - Update documentation
   - Announce redesign to mailing list
   - Monitor performance and user feedback

**Rollback Plan**:
- Keep previous stable branch tagged
- If critical issues arise:
  1. Revert `stable` branch to previous tag
  2. Trigger deployment webhook
  3. Site rolls back in <5 minutes
- Fix issues in beta environment
- Re-test before re-deploying

**Monitoring**:
- Google Analytics: Track bounce rate, session duration, page views
- Search Console: Monitor indexing, core web vitals, mobile usability
- Error tracking: Check server logs for 404s, broken links
- User feedback: Monitor social media, email feedback

**Success Metrics** (Compare before/after):
- Lighthouse Performance score improvement
- Reduced bounce rate
- Increased average session duration
- Improved mobile engagement
- Maintained or improved SEO rankings
- Positive user feedback

---

## Critical Files Summary

### Must Create (New Files):
1. `_config_beta.yml` - Beta environment config
2. `_sass/base/_css-variables.scss` - Color system with dark mode
3. `_sass/base/_typography-modern.scss` - Modern typography
4. `_sass/components/_cards.scss` - Card component system
5. `_sass/components/_buttons-modern.scss` - Modern button styles
6. `_includes/metrics.html` - Impact metrics component
7. `_includes/testimonials.html` - Testimonial showcase
8. `_includes/photo-story.html` - Photo story gallery
9. `_data/metrics.yml` - Metrics data
10. `_data/testimonials.yml` - Testimonial data

### Must Modify (Existing Files):
1. `_data/style.yml` - Update color system
2. `assets/css/bumble.scss` - Import new styles
3. `_sass/components/_navbar.scss` - Modern nav with blur
4. `_sass/layout/_masthead.scss` - Softer hero sections
5. `_includes/head.html` - Critical CSS, resource hints
6. `_layouts/default.html` - Beta banner, service worker
7. `_data/team.yml` - Enhanced team data
8. `_pages/about.md` - Use new storytelling components
9. `_pages/index.md` - Add metrics section
10. `.github/workflows/build-deploy.yml` - Beta deployment

## Risk Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Beta breaks bilingual routing | High | Test both languages thoroughly, maintain jekyll-multiple-languages-plugin compatibility |
| Dark mode has poor contrast | Medium | Test with contrast analyzers, follow WCAG AA guidelines |
| Performance regression | Medium | Monitor Lighthouse scores at each phase, optimize incrementally |
| CSS variables unsupported in old browsers | Low | Provide fallbacks, acceptable to not support IE11 |
| Breaking existing URLs | High | Never change permalinks, test all internal links |
| Build time increases | Low | Monitor CI/CD duration, optimize if needed |

## Timeline Estimate

- **Phase 1** (Beta Setup): 2-3 days
- **Phase 2** (Color System): 3-4 days
- **Phase 3** (Design System): 5-7 days
- **Phase 4** (Storytelling): 5-7 days
- **Phase 5** (Performance): 3-5 days
- **Phase 6** (Testing): 5-7 days
- **Phase 7** (Rollout): 2 weeks

**Total**: 6-8 weeks for complete implementation

## Next Steps

1. Create beta environment and deploy initial test
2. Implement color system with dark mode
3. Incrementally apply modern design patterns
4. Add storytelling components with real content
5. Optimize performance
6. Comprehensive testing
7. Staged rollout to production

Each phase can be developed, tested, and reviewed independently before moving to the next.