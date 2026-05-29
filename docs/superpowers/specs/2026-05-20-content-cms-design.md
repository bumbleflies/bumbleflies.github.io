# Content Management & Astro Collections Design
**Date:** 2026-05-20  
**Project:** bumbleflies.de redesign — content phase  
**Status:** Design approved, ready for implementation planning

---

## Executive Summary

Rather than deploying a separate DecapCMS backend, content will live as Markdown/YAML files in Git. Astro's native content collections system will load and validate the files at build time. Christian/Sebastian edit via GitHub UI or local Git. Changes trigger GitHub Actions rebuilds automatically.

**Why this approach:**
- No infrastructure to maintain (no separate CMS backend)
- Single source of truth (Git)
- Leverages existing CI/CD pipeline
- Simple for editors: familiar Git workflow or GitHub web UI
- Type-safe content (Astro collections with TypeScript schemas)

---

## 1. Content Structure

### Directory Organization
```
bumbleflies.github.io/
├── beta/
│   ├── src/
│   │   ├── pages/                 (existing — Astro pages)
│   │   ├── components/            (existing — Astro components)
│   │   ├── styles/                (existing — CSS)
│   │   └── content/               (NEW — content collections)
│   │       ├── config.ts          (collection schema definitions)
│   │       ├── case-studies/
│   │       │   ├── siemens.md
│   │       │   ├── leaguesphere.md
│   │       │   ├── manage-agile.md
│   │       │   └── dialograum-geld.md
│   │       ├── testimonials/
│   │       │   └── (individual quote files, optional initially)
│   │       ├── team/
│   │       │   ├── christian.md
│   │       │   ├── sebastian.md
│   │       │   └── christoph.md
│   │       └── pages/
│   │           ├── services.md
│   │           └── about.md
```

### Collection Types

**Case Studies** (`case-studies/`)
- Frontmatter fields: title, slug, service, company, duration, outcome, quote, image
- Body: Markdown (problem statement, engagement details, results)
- Purpose: Display on dedicated case studies page

**Testimonials** (`testimonials/`)
- Frontmatter fields: author, role, company, quote, image
- Body: (minimal — mostly frontmatter)
- Purpose: Pull quotes throughout site, testimonial carousel

**Team** (`team/`)
- Frontmatter fields: name, role, bio, image
- Body: Markdown (extended biography, optional)
- Purpose: Team profiles section (About page or dedicated page)

**Pages** (`pages/`)
- Frontmatter fields: title, slug
- Body: Markdown (full content)
- Purpose: Editable page content (Services, About, etc.)

---

## 2. Astro Collections Configuration

### File: `beta/src/content/config.ts`

Defines schema for each collection:

```typescript
import { defineCollection, z } from 'astro:content';

const caseStudies = defineCollection({
  schema: z.object({
    title: z.string(),
    slug: z.string().unique(),
    service: z.enum(['Talk', 'Decide', 'Build & Embed', 'Full Journey']),
    company: z.string(),
    duration: z.string().optional(),
    outcome: z.string(),
    quote: z.string(),
    image: z.string().optional(),
    published: z.boolean().default(true),
  }),
});

const testimonials = defineCollection({
  schema: z.object({
    author: z.string(),
    role: z.string(),
    company: z.string(),
    quote: z.string(),
    image: z.string().optional(),
    published: z.boolean().default(true),
  }),
});

const team = defineCollection({
  schema: z.object({
    name: z.string(),
    role: z.string(),
    bio: z.string(),
    image: z.string(),
    order: z.number().optional(),
  }),
});

const pages = defineCollection({
  schema: z.object({
    title: z.string(),
    slug: z.string().unique(),
    published: z.boolean().default(true),
  }),
});

export const collections = { caseStudies, testimonials, team, pages };
```

**Key features:**
- TypeScript validation ensures content shape at build time
- Optional fields (duration, image, etc.) allow flexible content
- `published` flag lets drafts exist without displaying
- Build fails if content doesn't match schema (catch errors early)

---

## 3. Content Files Format

### Example: Case Study (`case-studies/siemens.md`)

```markdown
---
title: "Siemens — Large Enterprise Facilitation"
slug: siemens
service: "Talk"
company: "Siemens AG"
duration: "Single day workshop (May 2023)"
outcome: "Clear decisions with named owners, aligned team direction, repeat customer"
quote: "After the workshop, we finally had clarity on what we were actually trying to do. And we knew who was responsible for what."
image: "/images/siemens-logo.png"
published: true
---

## Problem
Large team alignment across divisions. Multiple stakeholders with competing priorities. Needed structured facilitation to surface real bottlenecks and drive decisions with clear ownership.

## The Engagement
- **Service:** Talk (Facilitation)
- **Investment:** €2,800 + expenses
- **Follow-up:** Multiple additional facilitation sessions booked

## What Happened
Team meeting structured as full facilitation workshop. Issues surfaced that weren't apparent in regular meetings. Participants left with clarity, assigned owners for next steps.

## Key Results
✓ Clear decisions with named owners  
✓ Aligned team direction  
✓ Follow-up sessions booked (indicates satisfaction)
```

### Example: Team Member (`team/christian.md`)

```markdown
---
name: "Christian Dähn"
role: "Founder & Strategy Lead"
bio: "Christian leads workshops and strategy engagements, helping organizations align before building."
image: "/images/christian.jpg"
order: 1
---

Christian has facilitated workshops for Fortune 500 companies and mid-market teams, specializing in organizational alignment and decision-making under uncertainty.
```

---

## 4. Astro Component Integration

### Example: Display Case Studies

**File:** `beta/src/components/CaseStudiesList.astro`

```astro
---
import { getCollection } from 'astro:content';

const caseStudies = await getCollection('caseStudies', ({ data }) => data.published);
const sorted = caseStudies.sort((a, b) => 
  new Date(b.data.date).getTime() - new Date(a.data.date).getTime()
);
---

<div class="case-studies">
  {sorted.map(study => (
    <CaseStudyCard
      title={study.data.title}
      company={study.data.company}
      service={study.data.service}
      quote={study.data.quote}
      url={`/case-studies/${study.data.slug}`}
    />
  ))}
</div>
```

**File:** `beta/src/pages/case-studies/[slug].astro` (Dynamic route)

```astro
---
import { getCollection } from 'astro:content';
import CaseStudyLayout from '../../layouts/CaseStudyLayout.astro';

export async function getStaticPaths() {
  const caseStudies = await getCollection('caseStudies');
  return caseStudies.map(study => ({
    params: { slug: study.data.slug },
    props: { study },
  }));
}

const { study } = Astro.props;
const { Content } = await study.render();
---

<CaseStudyLayout {...study.data}>
  <Content />
</CaseStudyLayout>
```

**Result:** Each case study Markdown file automatically becomes a static HTML page at `/case-studies/siemens`, `/case-studies/leaguesphere`, etc.

---

## 5. Editing Workflow

### Option A: GitHub Web UI (Simplest)
1. Christian/Sebastian navigates to `beta/src/content/case-studies/siemens.md`
2. Clicks edit (pencil icon)
3. Makes changes in GitHub's editor
4. Clicks "Commit changes"
5. Selects "Commit directly to `main` branch"
6. GitHub Actions automatically triggers
7. Changes live in ~5-10 minutes

**No local git knowledge required.**

### Option B: Local Git (For bulk editing)
1. Clone repo: `git clone git@github.com:bumbleflies/bumbleflies.github.io.git`
2. Create branch: `git checkout -b content/add-case-studies`
3. Edit Markdown files locally in VS Code or any editor
4. Commit: `git commit -m "feat: add case study for LeagueSphere"`
5. Push: `git push origin content/add-case-studies`
6. Create PR on GitHub
7. You review + merge
8. GitHub Actions rebuilds

**Enables reviews if desired; also allows multiple edits before commit.**

### Approval Strategy
- **No review needed:** Christian/Sebastian commit directly to `main`. Changes go live immediately.
- **With review:** Create branch, push, submit PR. You approve before merge.

**Recommendation:** Start with direct commits (simpler). Move to PR reviews if needed later.

---

## 6. Build & Deployment

### GitHub Actions CI/CD (Existing)
Your current `.github/workflows/` already handles:
1. Detect push to `main`
2. Run `astro build` (which reads `/content` files)
3. Validate content against schemas (build fails if invalid)
4. Build Docker image
5. Push to `ghcr.io/bumbleflies/web:beta`

**No changes needed.** The build process already supports content collections.

### Local Development
Developers can test locally:
```bash
cd beta
npm install
npm run dev
# Astro dev server auto-reloads when content files change
```

### Deployment to servyy-test
Your existing process continues:
```bash
ssh servyy-test.lxd "cd /home/cda/servyy-container/bumbleflies && docker compose pull && docker compose up -d"
```

---

## 7. Initial State (MVP)

**Phase 1 — Collections Defined, Empty:**
- `beta/src/content/config.ts` written (schema + validation)
- Folder structure created (`case-studies/`, `testimonials/`, `team/`)
- Components created to render collections (even if empty)
- Deployed and tested locally
- Changes live on `main`

**Phase 2 — Populate Content (After):**
- Christian/Sebastian adds case studies, testimonials, team bios
- Edit via GitHub UI or local git
- Changes auto-rebuild and deploy

**Initial timeline:** ~1-2 days for Phase 1, then ongoing content migration.

---

## 8. Key Decisions & Rationale

| Decision | Why |
|----------|-----|
| **Markdown files (not DecapCMS)** | Single source of truth (Git), no backend to maintain, leverages Astro's native capabilities |
| **GitHub UI editing allowed** | Non-technical editors (Christian/Sebastian) can edit without touching terminal |
| **Direct commits to `main`** | Fast iteration; can move to PR reviews later if approval needed |
| **Astro collections for schema** | Type-safe, validated at build time, catches errors early |
| **Existing CI/CD unchanged** | Minimal disruption; builds already support content files |

---

## 9. Success Criteria

- [ ] Content collections schema defined and committed
- [ ] Folder structure created in repo
- [ ] Components built to render all collections (even with placeholder data)
- [ ] Local build passes (no validation errors)
- [ ] GitHub Actions build passes when pushed to `main`
- [ ] Deployed to servyy-test successfully
- [ ] Christian/Sebastian can edit a test case study via GitHub UI and see changes go live

---

## 10. Technical Constraints & Assumptions

- GitHub Actions CI/CD works as described (currently true)
- Docker Compose deployment continues to work
- Astro version ≥ 4.0 (supports content collections)
- Christian/Sebastian have GitHub access
- No real-time CMS UI needed (async edits + rebuilds acceptable)

---

## 11. Future Enhancements (Out of Scope)

- Scheduled content publishing (scheduled deploys)
- Rich text editor for content (Markdown works for now)
- Draft previews without full rebuild
- Content versioning/history (Git handles this)
- Localization (German/English content paths)

These can be added later without changing the core architecture.

---

## Conclusion

This design leverages Astro's native content collections system to keep content in Git. No separate CMS infrastructure needed. Christian/Sebastian can edit via GitHub UI or local git. Changes auto-deploy via existing CI/CD. Simple, maintainable, and aligned with your current infrastructure.

**Next step:** Implementation planning — define specific components, pages, and exact file structure to build Phase 1.
