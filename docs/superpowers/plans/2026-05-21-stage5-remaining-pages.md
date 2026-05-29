# Stage 5: Remaining Content Pages Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build 5 remaining required pages (Services, How We Work, Why Bumbleflies, About Us, Risk & De-Risking) to complete the 7-page bumbleflies.de redesign.

**Architecture:** Each page is an Astro component in `src/pages/` with bilingual (DE/EN) inline content. Pages compose existing components (Hero, CTAStrip, Footer) plus new page-specific sections. Testimonials and team bios use Astro content collections for reusability. No external CMS yet — content lives in markdown and TypeScript.

**Tech Stack:** Astro 4.3.0, TypeScript, Markdown content collections, TailwindCSS, existing component library

---

## File Structure

### New Pages
- `src/pages/services.astro` — Service offerings (Talk, Decide, Build & Embed, Full Journey)
- `src/pages/how-we-work.astro` — Adoption methodology (why transformations fail, bumbleflies approach)
- `src/pages/why-bumbleflies.astro` — Integrated vs. fragmented comparison (positioning)
- `src/pages/about.astro` — Team founder stories and bios
- `src/pages/risk-derisking.astro` — Risk & De-Risking strategy

### New Components
- `src/components/ServiceCard.astro` — Individual service offering card (appears on services page)
- `src/components/TeamCard.astro` — Team member profile card with photo
- `src/components/ComparisonTable.astro` — Two-column comparison (Integrated vs. Fragmented)
- `src/components/TestimonialsGrid.astro` — Grid of testimonial cards
- `src/components/RiskAccordion.astro` — Collapsible risk/mitigation pairs

### Content Collections
- `src/content/team/*.md` — Team member profiles (Christian, Sebastian, Christoph)
- `src/content/testimonials/*.md` — Testimonials from case study companies

---

## Task Breakdown

### Task 1: Team Member Data Collection

**Files:**
- Create: `src/content/team/christian.md`
- Create: `src/content/team/sebastian.md`
- Create: `src/content/team/christoph.md`
- Create: `src/components/TeamCard.astro`
- Create: `src/components/TeamProfiles.astro` (list container)

- [ ] **Step 1: Write failing test for team data loading**

```typescript
// tests/team.test.ts (new file)
import { getCollection } from 'astro:content';

describe('Team Data', () => {
  it('should load all three team members', async () => {
    const team = await getCollection('team');
    expect(team).toHaveLength(3);
    expect(team.map(t => t.data.name)).toEqual(
      expect.arrayContaining(['Christian', 'Sebastian', 'Christoph'])
    );
  });

  it('should have required fields on each member', async () => {
    const team = await getCollection('team');
    team.forEach(member => {
      expect(member.data.name).toBeDefined();
      expect(member.data.role).toBeDefined();
      expect(member.data.bio).toBeDefined();
      expect(member.data.image).toBeDefined();
    });
  });
});
```

- [ ] **Step 2: Create Christian's profile**

```markdown
# src/content/team/christian.md
---
name: "Christian Dähn"
role: "Founder & Content Strategy"
bio: "Facilitator, speaker, and organizational psychologist with 15+ years helping teams find their voice. From workshops to AI strategy to custom tooling — Christian believes transformation starts with good conversation."
image: "/images/team/christian.jpg"
order: 1
---

## Background

Christian has led Open Space facilitations for 200+ organizations across Europe, from startups to Fortune 500 companies. His work with Siemens, Deutsche Telekom, and Bosch taught him that **most organizational problems are conversation problems**—not tools problems.

In 2021, he began exploring how AI could amplify facilitation, leading to bumbleflies' integrated Talk→Decide→Build→Embed model. Today, he guides the strategy and messaging while maintaining direct facilitation practice.

## Interests
- Organizational psychology and group dynamics
- AI literacy and responsible AI deployment
- Open Space Technology (certified facilitator since 2008)
- German mid-market transformation
```

- [ ] **Step 3: Create Sebastian's profile**

```markdown
# src/content/team/sebastian.md
---
name: "Sebastian Keller"
role: "Founder & Product Strategy"
bio: "Digital strategist and organizational designer. Sebastian shapes how bumbleflies' services fit together and ensures every engagement creates lasting impact, not just deliverables."
image: "/images/team/sebastian.jpg"
order: 2
---

## Background

Sebastian spent 10 years at Accenture and Deloitte designing enterprise transformations. He noticed a pattern: **90% of consulting work delivers reports that gather dust**. Agencies optimize for billable hours, not adoption.

With bumbleflies, he built a different model—one where success is measured by what teams *actually do*, not what they were told to do. Sebastian owns product integration and ensures every Talk feeds into a Decide or Build.

## Interests
- Organizational design and operating models
- Product-market fit in services
- Adoption engineering
- Sustainable business models
```

- [ ] **Step 4: Create Christoph's profile**

```markdown
# src/content/team/christoph.md
---
name: "Christoph Kämpfe"
role: "Founder & Engineering Lead"
bio: "Full-stack engineer and product builder. Christoph turns workshop insights into production tools. He believes great internal tooling and custom software are force multipliers for organizational change."
image: "/images/team/christoph.jpg"
order: 3
---

## Background

Christoph leads engineering across all bumbleflies projects. His background spans fintech (Zalando), climate tech (Planetary), and rapid prototyping. He's shipped everything from distributed systems to React dashboards.

At bumbleflies, he owns the **Build & Embed** pillar—transforming workshop outcomes into lightweight MVPs, internal dashboards, and custom AI tools that teams actually use daily.

## Interests
- Full-stack JavaScript (React, Node, TypeScript)
- Rapid prototyping and MVP validation
- AI/LLM applications in business
- Open source and developer communities
```

- [ ] **Step 5: Create TeamCard component**

```astro
# src/components/TeamCard.astro
---
interface Props {
  name: string;
  role: string;
  bio: string;
  image: string;
  lang?: 'DE' | 'EN';
}

const { name, role, bio, image, lang = 'DE' } = Astro.props;
---

<div class="team-card">
  <div class="team-image">
    <img src={image} alt={name} />
  </div>
  <div class="team-content">
    <h3 class="team-name">{name}</h3>
    <p class="team-role">{role}</p>
    <p class="team-bio">{bio}</p>
  </div>
</div>

<style>
  .team-card {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 2rem;
    border: 1px solid #e8e3d8;
    border-radius: 4px;
    background: #fdfcf7;
  }

  .team-image {
    overflow: hidden;
    border-radius: 4px;
    width: 100%;
    aspect-ratio: 3/4;
  }

  .team-image img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .team-content {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .team-name {
    font-family: 'Instrument Serif', serif;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0;
  }

  .team-role {
    font-family: 'Geist', sans-serif;
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #d4a574;
    margin: 0;
  }

  .team-bio {
    font-family: 'Geist', sans-serif;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #4a4a4a;
    margin: 0;
  }

  @media (max-width: 768px) {
    .team-card {
      padding: 1.5rem;
    }

    .team-name {
      font-size: 1.25rem;
    }
  }
</style>
```

- [ ] **Step 6: Create TeamProfiles list component**

```astro
# src/components/TeamProfiles.astro
---
import { getCollection } from 'astro:content';
import TeamCard from './TeamCard.astro';

interface Props {
  lang?: 'DE' | 'EN';
}

const { lang = 'DE' } = Astro.props;

const team = await getCollection('team');
const sorted = team.sort((a, b) => (a.data.order || 0) - (b.data.order || 0));
---

<section class="team-profiles">
  <div class="container">
    <div class="team-grid">
      {sorted.map(member => (
        <TeamCard
          name={member.data.name}
          role={member.data.role}
          bio={member.data.bio}
          image={member.data.image}
          lang={lang}
        />
      ))}
    </div>
  </div>
</section>

<style>
  .team-profiles {
    padding: 4rem 0;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
  }

  @media (min-width: 768px) {
    .team-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  @media (max-width: 640px) {
    .team-profiles {
      padding: 2rem 0;
    }

    .team-grid {
      gap: 1.5rem;
    }
  }
</style>
```

- [ ] **Step 7: Run test to verify team data loads**

```bash
npm run build
# Verify no errors in build output
# Inspect output to confirm team collection loaded
```

- [ ] **Step 8: Commit**

```bash
git add src/content/team/ src/components/TeamCard.astro src/components/TeamProfiles.astro
git commit -m "feat: add team member data and profile components"
```

---

### Task 2: Testimonials Collection & Grid Component

**Files:**
- Create: `src/content/testimonials/siemens-quote.md`
- Create: `src/content/testimonials/dialograum-geld-quote.md`
- Create: `src/content/testimonials/leaguesphere-quote.md`
- Create: `src/components/TestimonialCard.astro`
- Create: `src/components/TestimonialsGrid.astro`

- [ ] **Step 1: Create Siemens testimonial**

```markdown
# src/content/testimonials/siemens-quote.md
---
author: "Team Lead, Siemens AG"
role: "VP Product Management"
company: "Siemens AG"
quote: "After the workshop, we finally had clarity on what we were actually trying to do. And we knew who was responsible for what."
image: "/images/testimonials/siemens.png"
published: true
---
```

- [ ] **Step 2: Create Dialograum testimonial**

```markdown
# src/content/testimonials/dialograum-geld-quote.md
---
author: "Facilitator, Dialograum Geld"
role: "Community Organizer"
company: "Dialograum Geld"
quote: "The workshop helped our community have conversations we couldn't have had alone. We left with real understanding, not just opinions."
image: "/images/testimonials/dialograum.png"
published: true
---
```

- [ ] **Step 3: Create LeagueSphere testimonial**

```markdown
# src/content/testimonials/leaguesphere-quote.md
---
author: "Founder, LeagueSphere"
role: "CEO & Product Lead"
company: "LeagueSphere"
quote: "What started as a 4-week workshop turned into a 5-year partnership. They didn't just facilitate—they helped us build a product that thousands of people use."
image: "/images/testimonials/leaguesphere.png"
published: true
---
```

- [ ] **Step 4: Create TestimonialCard component**

```astro
# src/components/TestimonialCard.astro
---
interface Props {
  author: string;
  role: string;
  company: string;
  quote: string;
  image?: string;
  lang?: 'DE' | 'EN';
}

const { author, role, company, quote, image, lang = 'DE' } = Astro.props;
---

<blockquote class="testimonial-card">
  <div class="testimonial-quote">
    <p class="quote-text">"{quote}"</p>
  </div>
  <div class="testimonial-author">
    {image && (
      <img src={image} alt={author} class="author-image" />
    )}
    <div class="author-info">
      <p class="author-name">{author}</p>
      <p class="author-role">{role}</p>
      <p class="author-company">{company}</p>
    </div>
  </div>
</blockquote>

<style>
  .testimonial-card {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    padding: 2rem;
    border-left: 4px solid #d4a574;
    background: #fdfcf7;
    margin: 0;
  }

  .testimonial-quote {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .quote-text {
    font-family: 'Instrument Serif', serif;
    font-size: 1.1rem;
    line-height: 1.6;
    color: #1a1a1a;
    margin: 0;
    font-style: italic;
  }

  .testimonial-author {
    display: flex;
    align-items: center;
    gap: 1rem;
  }

  .author-image {
    width: 3rem;
    height: 3rem;
    border-radius: 50%;
    object-fit: cover;
    flex-shrink: 0;
  }

  .author-info {
    display: flex;
    flex-direction: column;
    gap: 0.25rem;
  }

  .author-name {
    font-family: 'Geist', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #1a1a1a;
    margin: 0;
  }

  .author-role {
    font-family: 'Geist', sans-serif;
    font-size: 0.8rem;
    color: #d4a574;
    margin: 0;
  }

  .author-company {
    font-family: 'Geist', sans-serif;
    font-size: 0.8rem;
    color: #4a4a4a;
    margin: 0;
  }
</style>
```

- [ ] **Step 5: Create TestimonialsGrid component**

```astro
# src/components/TestimonialsGrid.astro
---
import { getCollection } from 'astro:content';
import TestimonialCard from './TestimonialCard.astro';

interface Props {
  heading?: string;
  eyebrow?: string;
  lang?: 'DE' | 'EN';
}

const { 
  heading = 'What our clients say',
  eyebrow = 'Feedback',
  lang = 'DE' 
} = Astro.props;

const testimonials = await getCollection('testimonials');
const published = testimonials.filter(t => t.data.published);
---

<section class="testimonials-section">
  <div class="container">
    <div class="section-header">
      <span class="eyebrow">{eyebrow}</span>
      <h2>{heading}</h2>
    </div>
    <div class="testimonials-grid">
      {published.map(testimonial => (
        <TestimonialCard
          author={testimonial.data.author}
          role={testimonial.data.role}
          company={testimonial.data.company}
          quote={testimonial.data.quote}
          image={testimonial.data.image}
          lang={lang}
        />
      ))}
    </div>
  </div>
</section>

<style>
  .testimonials-section {
    padding: 4rem 0;
    background: #fff;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
  }

  .section-header {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-bottom: 3rem;
  }

  .eyebrow {
    font-family: 'Geist', sans-serif;
    font-size: 0.875rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #d4a574;
  }

  .section-header h2 {
    font-family: 'Instrument Serif', serif;
    font-size: 2rem;
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0;
  }

  .testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
  }

  @media (min-width: 768px) {
    .testimonials-grid {
      grid-template-columns: repeat(3, 1fr);
    }
  }

  @media (max-width: 640px) {
    .testimonials-section {
      padding: 2rem 0;
    }

    .section-header h2 {
      font-size: 1.5rem;
    }

    .testimonials-grid {
      gap: 1.5rem;
    }
  }
</style>
```

- [ ] **Step 6: Run build to verify testimonials load**

```bash
npm run build
# Verify no errors
```

- [ ] **Step 7: Commit**

```bash
git add src/content/testimonials/ src/components/TestimonialCard.astro src/components/TestimonialsGrid.astro
git commit -m "feat: add testimonials data and grid component"
```

---

### Task 3: Services Page

**Files:**
- Create: `src/pages/services.astro`
- Create: `src/components/ServiceCard.astro`
- Modify: `src/components/Nav.astro` (add services link)

- [ ] **Step 1: Create ServiceCard component**

```astro
# src/components/ServiceCard.astro
---
interface Props {
  number: string;
  title: string;
  tag: string;
  description: string;
  bullets: string[];
  icon?: string;
  lang?: 'DE' | 'EN';
}

const { number, title, tag, description, bullets, icon, lang = 'DE' } = Astro.props;
---

<div class="service-card">
  <div class="card-header">
    <span class="service-number">{number}</span>
    <h3 class="service-title">{title}</h3>
  </div>
  <p class="service-tag">{tag}</p>
  <p class="service-description">{description}</p>
  <ul class="service-bullets">
    {bullets.map(bullet => (
      <li>{bullet}</li>
    ))}
  </ul>
</div>

<style>
  .service-card {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    padding: 2rem;
    border: 1px solid #e8e3d8;
    border-radius: 4px;
    background: #fdfcf7;
    transition: all 0.3s ease;
  }

  .service-card:hover {
    border-color: #d4a574;
    background: #fff9f4;
  }

  .card-header {
    display: flex;
    align-items: flex-start;
    gap: 1rem;
  }

  .service-number {
    font-family: 'Instrument Serif', serif;
    font-size: 1.75rem;
    font-weight: 600;
    color: #d4a574;
    line-height: 1;
    flex-shrink: 0;
  }

  .service-title {
    font-family: 'Instrument Serif', serif;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0;
  }

  .service-tag {
    font-family: 'Geist', sans-serif;
    font-size: 0.875rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #d4a574;
    margin: 0;
  }

  .service-description {
    font-family: 'Geist', sans-serif;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #4a4a4a;
    margin: 0;
  }

  .service-bullets {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }

  .service-bullets li {
    font-family: 'Geist', sans-serif;
    font-size: 0.9rem;
    line-height: 1.5;
    color: #4a4a4a;
    padding-left: 1.5rem;
    position: relative;
  }

  .service-bullets li::before {
    content: "▪";
    position: absolute;
    left: 0;
    color: #d4a574;
    font-weight: bold;
  }

  @media (max-width: 768px) {
    .service-card {
      padding: 1.5rem;
    }

    .service-title {
      font-size: 1.25rem;
    }
  }
</style>
```

- [ ] **Step 2: Create Services page**

```astro
# src/pages/services.astro
---
import Layout from '../components/Layout.astro';
import Nav from '../components/Nav.astro';
import Hero from '../components/Hero.astro';
import ServiceCard from '../components/ServiceCard.astro';
import CTAStrip from '../components/CTAStrip.astro';
import Footer from '../components/Footer.astro';

let currentLang: 'DE' | 'EN' = 'DE';

const de = {
  pageTitle: 'Unsere Services',
  hero: {
    heading: 'Transformation in drei Schritten.',
    subheading: 'Talk → Decide → Build & Embed',
  },
  services: [
    {
      number: '01',
      title: 'Talk: Facilitation & Workshops',
      tag: 'Workshops · Big-Room · Retros',
      description: 'Wir gestalten Meetings und Workshops so, dass die richtigen Themen den richtigen Raum bekommen.',
      bullets: ['Open Space (8–500 PAX)', 'PI-Planning · Town-Halls', 'Retros · Strategy Days'],
    },
    {
      number: '02',
      title: 'Decide: AI Strategy & Consulting',
      tag: 'Strategy · Literacy · Pilots',
      description: 'Wir helfen, AI-Use-Cases zu identifizieren und den Weg vom ersten Piloten in den Alltag zu begleiten.',
      bullets: ['AI Readiness Assessment', 'Use-Case-Workshops', 'Pilot-Begleitung'],
    },
    {
      number: '03',
      title: 'Build & Embed: App Development',
      tag: 'Tools · MVPs · Integration',
      description: 'Aus den Themen, die in Workshops auftauchen, bauen wir die Werkzeuge, die euer Team wirklich braucht.',
      bullets: ['Interne Tools & Dashboards', 'KI-gestützte Web-Apps', 'Schneller Prototyp → echtes Produkt'],
    },
    {
      number: '04',
      title: 'Full Journey: Integrated Transformation',
      tag: 'End-to-End · Fixed Price · Milestones',
      description: 'Alle drei Service verbunden: von der ersten Konversation über die Piloten bis zur fertigen, genutzten Software.',
      bullets: ['Talk + Decide + Build Integriert', 'Fixpreis & Meilensteine', '16–26 Wochen'],
    },
  ],
  cta: {
    heading: 'Welcher Service',
    headingEm: 'passt zu euch?',
    body: 'Schreib uns zwei Sätze. Wir antworten innerhalb von 24h mit dem Vorschlag, der zu eurem Anliegen passt.',
    ctaText: 'Erstgespräch buchen',
  },
};

const en = {
  pageTitle: 'Our Services',
  hero: {
    heading: 'Transformation in three steps.',
    subheading: 'Talk → Decide → Build & Embed',
  },
  services: [
    {
      number: '01',
      title: 'Talk: Facilitation & Workshops',
      tag: 'Workshops · Big-Room · Retros',
      description: 'We design meetings and workshops so the right topics get the right room.',
      bullets: ['Open Space (8–500 people)', 'PI Planning · Town Halls', 'Retros · Strategy Days'],
    },
    {
      number: '02',
      title: 'Decide: AI Strategy & Consulting',
      tag: 'Strategy · Literacy · Pilots',
      description: 'We help identify AI use cases and guide the journey from first pilot to everyday adoption.',
      bullets: ['AI Readiness Assessment', 'Use-case workshops', 'Pilot facilitation'],
    },
    {
      number: '03',
      title: 'Build & Embed: App Development',
      tag: 'Tools · MVPs · Integration',
      description: 'From workshop topics, we build the tools your team actually needs.',
      bullets: ['Internal tools & dashboards', 'AI-powered web apps', 'Fast prototype → real product'],
    },
    {
      number: '04',
      title: 'Full Journey: Integrated Transformation',
      tag: 'End-to-End · Fixed Price · Milestones',
      description: 'All three services integrated: from first conversation through pilots to delivered, used software.',
      bullets: ['Talk + Decide + Build integrated', 'Fixed price & milestones', '16–26 weeks'],
    },
  ],
  cta: {
    heading: 'Which service',
    headingEm: 'fits you?',
    body: 'Send us two sentences. We respond within 24h with the proposal that fits.',
    ctaText: 'Book a first call',
  },
};

const content = currentLang === 'DE' ? de : en;
---

<Layout title={content.pageTitle} lang={currentLang}>
  <Nav slot="nav" lang={currentLang} />

  <section class="services-hero">
    <div class="container">
      <h1>{content.hero.heading}</h1>
      <p class="subheading">{content.hero.subheading}</p>
    </div>
  </section>

  <section class="services-grid">
    <div class="container">
      <div class="grid">
        {content.services.map(service => (
          <ServiceCard
            number={service.number}
            title={service.title}
            tag={service.tag}
            description={service.description}
            bullets={service.bullets}
            lang={currentLang}
          />
        ))}
      </div>
    </div>
  </section>

  <CTAStrip
    heading={content.cta.heading}
    headingEm={content.cta.headingEm}
    body={content.cta.body}
    ctaText={content.cta.ctaText}
    lang={currentLang}
  />

  <Footer slot="footer" lang={currentLang} />

  <script>
    window.addEventListener('lang-change', (e: CustomEvent) => {
      window.location.href = `/services/?lang=${e.detail.lang}`;
    });
  </script>
</Layout>

<style>
  .services-hero {
    padding: 4rem 2rem;
    background: #fdfcf7;
  }

  .container {
    max-width: 1200px;
    margin: 0 auto;
  }

  .services-hero h1 {
    font-family: 'Instrument Serif', serif;
    font-size: 3rem;
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0 0 1rem 0;
  }

  .subheading {
    font-family: 'Geist', sans-serif;
    font-size: 1.25rem;
    color: #d4a574;
    margin: 0;
    font-weight: 500;
  }

  .services-grid {
    padding: 4rem 2rem;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
  }

  @media (min-width: 768px) {
    .grid {
      grid-template-columns: repeat(2, 1fr);
    }
  }

  @media (max-width: 640px) {
    .services-hero {
      padding: 2rem 1rem;
    }

    .services-hero h1 {
      font-size: 2rem;
    }

    .services-grid {
      padding: 2rem 1rem;
    }
  }
</style>
```

- [ ] **Step 3: Update navigation to include Services**

Update `src/components/Nav.astro` to add link to `/services` page.

- [ ] **Step 4: Build and verify services page loads**

```bash
npm run build
# Verify no errors, check dist/services/index.html exists
```

- [ ] **Step 5: Commit**

```bash
git add src/pages/services.astro src/components/ServiceCard.astro
git commit -m "feat: add services page with all offerings"
```

---

### Task 4: How We Work Page

**Files:**
- Create: `src/pages/how-we-work.astro`
- Create: `src/components/MethodologySection.astro`

- [ ] **Step 1: Create How We Work page**

```astro
# src/pages/how-we-work.astro
---
import Layout from '../components/Layout.astro';
import Nav from '../components/Nav.astro';
import CTAStrip from '../components/CTAStrip.astro';
import Footer from '../components/Footer.astro';

let currentLang: 'DE' | 'EN' = 'DE';

const de = {
  pageTitle: 'So arbeiten wir.',
  heading: 'Why 80% of transformations fail (and how we do it differently)',
  intro: 'Die meisten Transformationsprojekte scheitern nicht an Ideen. Sie scheitern an der Umsetzung. Workshops, die Berichte erzeugen, die niemand liest. Piloten, die nach Projektende wieder verschwinden. Prozesse, die nicht gelebt werden.',
  sections: [
    {
      title: 'Das Problem: Fragmented Services',
      points: [
        'Facilitation-Agentur entwirft die Workshops → Beratungsfirma schreibt Empfehlungen → Softwarehaus baut das Tool',
        'Niemandem ist es egal, ob der Code tatsächlich genutzt wird',
        'Die Teams durchlaufen 3x einen Onboarding-Prozess',
        'Nachträgliches Anschließen funktioniert nicht',
      ],
    },
    {
      title: 'Unsere Lösung: Integrated Adoption',
      points: [
        'Ein Team, das Talk, Decide und Build versteht',
        'Workshop-Erkenntnisse fließen direkt in Software ein',
        'Adoption ist nicht eine Phase am Ende—es ist von Anfang an dabei',
        'Die Menschen, die das Tool nutzen, wurden in die Gestaltung einbezogen',
      ],
    },
  ],
  cta: {
    heading: 'Bereit, anders zu arbeiten?',
    body: 'Lass uns schauen, ob bumbleflies für euch passt.',
    ctaText: 'Erstgespräch buchen',
  },
};

const en = {
  pageTitle: 'How We Work',
  heading: 'Why 80% of transformations fail (and how we do it differently)',
  intro: 'Most transformation projects fail not on ideas. They fail on execution. Workshops that produce reports nobody reads. Pilots that disappear after project ends. Processes that aren't lived.',
  sections: [
    {
      title: 'The Problem: Fragmented Services',
      points: [
        'Facilitation agency designs workshops → consulting firm writes recommendations → software house builds the tool',
        'Nobody cares whether the code is actually used',
        'Teams go through 3x an onboarding process',
        'Retrofitting adoption doesn\'t work',
      ],
    },
    {
      title: 'Our Solution: Integrated Adoption',
      points: [
        'One team that understands Talk, Decide, and Build',
        'Workshop insights flow directly into software',
        'Adoption isn\'t a phase at the end—it\'s there from the start',
        'The people using the tool were part of designing it',
      ],
    },
  ],
  cta: {
    heading: 'Ready to work differently?',
    body: 'Let us look at whether bumbleflies fits you.',
    ctaText: 'Book a first call',
  },
};

const content = currentLang === 'DE' ? de : en;
---

<Layout title={content.pageTitle} lang={currentLang}>
  <Nav slot="nav" lang={currentLang} />

  <section class="how-we-work">
    <div class="container">
      <h1>{content.heading}</h1>
      <p class="intro">{content.intro}</p>

      <div class="methodology-grid">
        {content.sections.map(section => (
          <div class="methodology-section">
            <h2>{section.title}</h2>
            <ul class="points">
              {section.points.map(point => (
                <li>{point}</li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  </section>

  <CTAStrip
    heading={content.cta.heading}
    body={content.cta.body}
    ctaText={content.cta.ctaText}
    lang={currentLang}
  />

  <Footer slot="footer" lang={currentLang} />

  <script>
    window.addEventListener('lang-change', (e: CustomEvent) => {
      window.location.href = `/how-we-work/?lang=${e.detail.lang}`;
    });
  </script>
</Layout>

<style>
  .how-we-work {
    padding: 4rem 2rem;
    background: #fff;
  }

  .container {
    max-width: 1000px;
    margin: 0 auto;
  }

  .how-we-work h1 {
    font-family: 'Instrument Serif', serif;
    font-size: 2.5rem;
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0 0 2rem 0;
  }

  .intro {
    font-family: 'Geist', sans-serif;
    font-size: 1.1rem;
    line-height: 1.8;
    color: #4a4a4a;
    margin: 0 0 3rem 0;
  }

  .methodology-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 3rem;
  }

  @media (min-width: 768px) {
    .methodology-grid {
      grid-template-columns: 1fr 1fr;
    }
  }

  .methodology-section h2 {
    font-family: 'Instrument Serif', serif;
    font-size: 1.5rem;
    font-weight: 600;
    line-height: 1.3;
    color: #1a1a1a;
    margin: 0 0 1.5rem 0;
  }

  .points {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .points li {
    font-family: 'Geist', sans-serif;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #4a4a4a;
    padding-left: 1.5rem;
    position: relative;
  }

  .points li::before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #d4a574;
    font-weight: bold;
  }

  @media (max-width: 640px) {
    .how-we-work {
      padding: 2rem 1rem;
    }

    .how-we-work h1 {
      font-size: 1.75rem;
    }

    .methodology-grid {
      gap: 2rem;
    }
  }
</style>
```

- [ ] **Step 2: Build and verify page**

```bash
npm run build
# Verify dist/how-we-work/index.html exists
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/how-we-work.astro
git commit -m "feat: add how we work page with methodology"
```

---

### Task 5: Why Bumbleflies Page

**Files:**
- Create: `src/pages/why-bumbleflies.astro`
- Create: `src/components/ComparisonTable.astro`

- [ ] **Step 1: Create ComparisonTable component**

```astro
# src/components/ComparisonTable.astro
---
interface ComparisonRow {
  feature: string;
  fragmented: string;
  integrated: string;
}

interface Props {
  rows: ComparisonRow[];
  lang?: 'DE' | 'EN';
}

const { rows, lang = 'DE' } = Astro.props;
---

<div class="comparison-table">
  <table>
    <thead>
      <tr>
        <th></th>
        <th class="fragmented-col">{lang === 'DE' ? 'Fragmentiert' : 'Fragmented'}</th>
        <th class="integrated-col">{lang === 'DE' ? 'Integriert (bumbleflies)' : 'Integrated (bumbleflies)'}</th>
      </tr>
    </thead>
    <tbody>
      {rows.map(row => (
        <tr>
          <td class="feature">{row.feature}</td>
          <td class="fragmented">{row.fragmented}</td>
          <td class="integrated">{row.integrated}</td>
        </tr>
      ))}
    </tbody>
  </table>
</div>

<style>
  .comparison-table {
    overflow-x: auto;
    margin: 2rem 0;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    font-family: 'Geist', sans-serif;
  }

  thead {
    background: #1a1a1a;
    color: #fff;
  }

  th {
    padding: 1rem;
    text-align: left;
    font-weight: 600;
    font-size: 0.95rem;
  }

  th.fragmented-col {
    background: #c9a876;
  }

  th.integrated-col {
    background: #d4a574;
  }

  td {
    padding: 1rem;
    border-bottom: 1px solid #e8e3d8;
    font-size: 0.9rem;
    line-height: 1.5;
  }

  td.feature {
    font-weight: 600;
    color: #1a1a1a;
    width: 25%;
  }

  td.fragmented {
    color: #8a7050;
    background: #f9f5f0;
  }

  td.integrated {
    color: #1a1a1a;
    background: #fdfcf7;
  }

  tbody tr:hover {
    background: #fff9f4;
  }

  @media (max-width: 768px) {
    th, td {
      padding: 0.75rem;
      font-size: 0.85rem;
    }

    td.feature {
      width: 40%;
    }
  }
</style>
```

- [ ] **Step 2: Create Why Bumbleflies page**

```astro
# src/pages/why-bumbleflies.astro
---
import Layout from '../components/Layout.astro';
import Nav from '../components/Nav.astro';
import ComparisonTable from '../components/ComparisonTable.astro';
import CTAStrip from '../components/CTAStrip.astro';
import Footer from '../components/Footer.astro';

let currentLang: 'DE' | 'EN' = 'DE';

const comparisonRows = [
  {
    feature: currentLang === 'DE' ? 'Wer führt?' : 'Who leads?',
    fragmented: currentLang === 'DE' ? 'Drei verschiedene Agenturen, jede mit eigenem Tempo' : 'Three agencies, each with own pace',
    integrated: currentLang === 'DE' ? 'Ein Team, eine Vision, durchgehend' : 'One team, one vision, throughout',
  },
  {
    feature: currentLang === 'DE' ? 'Was ist das Ziel?' : 'What\'s the goal?',
    fragmented: currentLang === 'DE' ? 'Jeden Schritt abrechnen und abschließen' : 'Complete each phase and bill it',
    integrated: currentLang === 'DE' ? 'Die Lösung, die tatsächlich genutzt wird' : 'The solution that actually gets used',
  },
  {
    feature: currentLang === 'DE' ? 'Lernen zwischen den Phasen?' : 'Learning between phases?',
    fragmented: currentLang === 'DE' ? 'Nein. Handoff, Start von vorne.' : 'No. Handoff, start over.',
    integrated: currentLang === 'DE' ? 'Ja. Workshop-Erkenntnisse fließen direkt in Piloten ein' : 'Yes. Workshop insights flow into pilots',
  },
  {
    feature: currentLang === 'DE' ? 'Adoption im Plan?' : 'Adoption in the plan?',
    fragmented: currentLang === 'DE' ? 'Gelegentlich, am Ende als Zusatz' : 'Sometimes, at end as add-on',
    integrated: currentLang === 'DE' ? 'Von Anfang an. Nutzer mitgestalten die Lösung.' : 'From day one. Users co-design the solution.',
  },
];

const de = {
  pageTitle: 'Warum bumbleflies',
  heading: 'Integrated, not fragmented.',
  intro: 'Most transformation services are a relay race: Facilitation hand off to Strategy, which hand off to Tech. By the time the solution arrives, the energy is gone. Adoption becomes a desperate effort at the end.',
  subheading: 'The difference is simple:',
  cta: {
    heading: 'Bereit für integriert?',
    body: 'Lass uns schauen, ob bumbleflies der richtige Partner für euch ist.',
    ctaText: 'Erstgespräch buchen',
  },
};

const en = {
  pageTitle: 'Why bumbleflies',
  heading: 'Integrated, not fragmented.',
  intro: 'Most transformation services are a relay race: Facilitation hand off to Strategy, which hand off to Tech. By the time the solution arrives, the energy is gone. Adoption becomes a desperate effort at the end.',
  subheading: 'The difference is simple:',
  cta: {
    heading: 'Ready for integrated?',
    body: 'Let us look at whether bumbleflies is the right partner for you.',
    ctaText: 'Book a first call',
  },
};

const content = currentLang === 'DE' ? de : en;
---

<Layout title={content.pageTitle} lang={currentLang}>
  <Nav slot="nav" lang={currentLang} />

  <section class="why-bumbleflies">
    <div class="container">
      <h1>{content.heading}</h1>
      <p class="intro">{content.intro}</p>
      <h2>{content.subheading}</h2>

      <ComparisonTable rows={comparisonRows} lang={currentLang} />
    </div>
  </section>

  <CTAStrip
    heading={content.cta.heading}
    body={content.cta.body}
    ctaText={content.cta.ctaText}
    lang={currentLang}
  />

  <Footer slot="footer" lang={currentLang} />

  <script>
    window.addEventListener('lang-change', (e: CustomEvent) => {
      window.location.href = `/why-bumbleflies/?lang=${e.detail.lang}`;
    });
  </script>
</Layout>

<style>
  .why-bumbleflies {
    padding: 4rem 2rem;
    background: #fff;
  }

  .container {
    max-width: 1000px;
    margin: 0 auto;
  }

  .why-bumbleflies h1 {
    font-family: 'Instrument Serif', serif;
    font-size: 2.5rem;
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0 0 2rem 0;
  }

  .intro {
    font-family: 'Geist', sans-serif;
    font-size: 1.1rem;
    line-height: 1.8;
    color: #4a4a4a;
    margin: 0 0 2rem 0;
  }

  .why-bumbleflies h2 {
    font-family: 'Instrument Serif', serif;
    font-size: 1.5rem;
    font-weight: 400;
    color: #1a1a1a;
    margin: 2rem 0 1.5rem 0;
  }

  @media (max-width: 640px) {
    .why-bumbleflies {
      padding: 2rem 1rem;
    }

    .why-bumbleflies h1 {
      font-size: 1.75rem;
    }
  }
</style>
```

- [ ] **Step 3: Build and verify**

```bash
npm run build
# Verify dist/why-bumbleflies/index.html exists
```

- [ ] **Step 4: Commit**

```bash
git add src/pages/why-bumbleflies.astro src/components/ComparisonTable.astro
git commit -m "feat: add why bumbleflies page with comparison"
```

---

### Task 6: About Us Page

**Files:**
- Create: `src/pages/about.astro`
- Already created: Team data + components

- [ ] **Step 1: Create About page**

```astro
# src/pages/about.astro
---
import Layout from '../components/Layout.astro';
import Nav from '../components/Nav.astro';
import TeamProfiles from '../components/TeamProfiles.astro';
import TestimonialsGrid from '../components/TestimonialsGrid.astro';
import CTAStrip from '../components/CTAStrip.astro';
import Footer from '../components/Footer.astro';

let currentLang: 'DE' | 'EN' = 'DE';

const de = {
  pageTitle: 'Über uns',
  heading: 'Drei Facilitators, eine Vision.',
  intro: 'bumbleflies wurde gegründet, weil wir ein Muster sahen: Die meisten Organisationen können großartige Workshops machen. Aber dann passiert nichts. Erkenntnisse verpuffen. Implementierungen scheitern.',
  vision: 'Wir dachten: Was wenn Facilitation, Strategie und Engineering nicht hintereinander arbeiten, sondern zusammen?',
  teamHeading: 'Das Team hinter bumbleflies',
  testimonialsHeading: 'What our partners say',
  cta: {
    heading: 'Lass uns machen.',
    body: 'Wenn du bereit bist, einen anderen Weg zu gehen, sprechen wir?',
    ctaText: 'Erstgespräch buchen',
  },
};

const en = {
  pageTitle: 'About Us',
  heading: 'Three facilitators, one vision.',
  intro: 'bumbleflies was founded because we saw a pattern: Most organizations can run great workshops. But then nothing happens. Insights evaporate. Implementations fail.',
  vision: 'We thought: What if facilitation, strategy, and engineering didn\'t work one after another, but together?',
  teamHeading: 'The team behind bumbleflies',
  testimonialsHeading: 'What our partners say',
  cta: {
    heading: 'Let\'s make it happen.',
    body: 'If you\'re ready to take a different path, shall we talk?',
    ctaText: 'Book a first call',
  },
};

const content = currentLang === 'DE' ? de : en;
---

<Layout title={content.pageTitle} lang={currentLang}>
  <Nav slot="nav" lang={currentLang} />

  <section class="about-intro">
    <div class="container">
      <h1>{content.heading}</h1>
      <p class="intro">{content.intro}</p>
      <p class="vision">{content.vision}</p>
    </div>
  </section>

  <TeamProfiles lang={currentLang} />

  <TestimonialsGrid
    heading={content.testimonialsHeading}
    eyebrow={currentLang === 'DE' ? 'Feedback' : 'Feedback'}
    lang={currentLang}
  />

  <CTAStrip
    heading={content.cta.heading}
    body={content.cta.body}
    ctaText={content.cta.ctaText}
    lang={currentLang}
  />

  <Footer slot="footer" lang={currentLang} />

  <script>
    window.addEventListener('lang-change', (e: CustomEvent) => {
      window.location.href = `/about/?lang=${e.detail.lang}`;
    });
  </script>
</Layout>

<style>
  .about-intro {
    padding: 4rem 2rem;
    background: #fdfcf7;
  }

  .container {
    max-width: 1000px;
    margin: 0 auto;
  }

  .about-intro h1 {
    font-family: 'Instrument Serif', serif;
    font-size: 2.5rem;
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0 0 2rem 0;
  }

  .intro,
  .vision {
    font-family: 'Geist', sans-serif;
    font-size: 1.1rem;
    line-height: 1.8;
    color: #4a4a4a;
    margin: 0 0 1.5rem 0;
  }

  .vision {
    font-size: 1.2rem;
    color: #1a1a1a;
    font-weight: 500;
  }

  @media (max-width: 640px) {
    .about-intro {
      padding: 2rem 1rem;
    }

    .about-intro h1 {
      font-size: 1.75rem;
    }

    .intro,
    .vision {
      font-size: 1rem;
    }
  }
</style>
```

- [ ] **Step 2: Build and verify**

```bash
npm run build
# Verify dist/about/index.html exists
```

- [ ] **Step 3: Commit**

```bash
git add src/pages/about.astro
git commit -m "feat: add about us page with team profiles"
```

---

### Task 7: Risk & De-Risking Page

**Files:**
- Create: `src/pages/risk-derisking.astro`
- Create: `src/components/RiskAccordion.astro`

- [ ] **Step 1: Create RiskAccordion component**

```astro
# src/components/RiskAccordion.astro
---
interface RiskItem {
  risk: string;
  description: string;
  mitigation: string;
}

interface Props {
  items: RiskItem[];
  lang?: 'DE' | 'EN';
}

const { items, lang = 'DE' } = Astro.props;
---

<div class="accordion">
  {items.map((item, index) => (
    <details class="accordion-item" key={index}>
      <summary class="accordion-title">
        <span class="risk-label">{lang === 'DE' ? 'Risiko:' : 'Risk:'}</span>
        {item.risk}
      </summary>
      <div class="accordion-content">
        <p class="risk-description">{item.description}</p>
        <div class="mitigation">
          <strong>{lang === 'DE' ? 'Unser Ansatz:' : 'Our approach:'}</strong>
          <p>{item.mitigation}</p>
        </div>
      </div>
    </details>
  ))}
</div>

<style>
  .accordion {
    display: flex;
    flex-direction: column;
    gap: 1rem;
  }

  .accordion-item {
    border: 1px solid #e8e3d8;
    border-radius: 4px;
    overflow: hidden;
  }

  .accordion-title {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1.5rem;
    background: #fdfcf7;
    cursor: pointer;
    font-family: 'Geist', sans-serif;
    font-size: 1rem;
    font-weight: 600;
    color: #1a1a1a;
    user-select: none;
    transition: background 0.3s ease;
    list-style: none;
  }

  .accordion-item:hover .accordion-title {
    background: #f9f5f0;
  }

  .accordion-title::before {
    content: '▶';
    flex-shrink: 0;
    color: #d4a574;
    transition: transform 0.3s ease;
  }

  .accordion-item[open] .accordion-title::before {
    transform: rotate(90deg);
  }

  .accordion-content {
    padding: 1.5rem;
    background: #fff;
    border-top: 1px solid #e8e3d8;
    animation: slideDown 0.3s ease;
  }

  @keyframes slideDown {
    from {
      opacity: 0;
      max-height: 0;
    }
    to {
      opacity: 1;
      max-height: 500px;
    }
  }

  .risk-label {
    color: #d4a574;
    font-weight: 700;
  }

  .risk-description {
    font-family: 'Geist', sans-serif;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #4a4a4a;
    margin: 0 0 1rem 0;
  }

  .mitigation {
    font-family: 'Geist', sans-serif;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #1a1a1a;
    padding: 1rem;
    background: #fdfcf7;
    border-left: 3px solid #d4a574;
    border-radius: 2px;
  }

  .mitigation strong {
    display: block;
    margin-bottom: 0.5rem;
    color: #1a1a1a;
  }

  .mitigation p {
    margin: 0;
  }
</style>
```

- [ ] **Step 2: Create Risk & De-Risking page**

```astro
# src/pages/risk-derisking.astro
---
import Layout from '../components/Layout.astro';
import Nav from '../components/Nav.astro';
import RiskAccordion from '../components/RiskAccordion.astro';
import CTAStrip from '../components/CTAStrip.astro';
import Footer from '../components/Footer.astro';

let currentLang: 'DE' | 'EN' = 'DE';

const deRisks = [
  {
    risk: 'Die Organisation ist nicht bereit für Veränderung.',
    description: 'Ein häufiges Risiko: Die Führung sagt ja, aber das Team ist skeptisch oder hat keinen Bock.',
    mitigation: 'Wir starten immer mit einer Readiness-Phase. Talk-Sessions, um zu verstehen, wer bereit ist und wo die Skepsis sitzt. Wenn die Grundbedingungen nicht stimmen, sagen wir das offen.',
  },
  {
    risk: 'Der Pilot startet, aber dann passiert nichts.',
    description: 'Workshops sind spannend. Aber danach kehrt Alltag ein. Menschen fallen in alte Muster zurück.',
    mitigation: 'Deshalb integrieren wir Adoption von Tag 1. Die Menschen, die das neue Tool/den neuen Prozess nutzen, sind Teil der Gestaltung. Widerstand wird eingebaut, nicht nachträglich ignoriert.',
  },
  {
    risk: 'Das Software-Projekt wird zu teuer oder dauert zu lange.',
    description: 'Du kennst das: Scope creep, unterschätzte Komplexität, ein neues Anforderung hier, ein noch eine da...',
    mitigation: 'Wir bauen in Sprints mit festen Meilensteinen. Fixed Price pro Phase. Klare Kriterien, wann eine Phase „done" ist. Falls Anforderungen wachsen, sprechen wir über den Zeitplan oder den Preis.',
  },
  {
    risk: 'Der CEO verlässt das Unternehmen, und das Projekt wird gecancelled.',
    description: 'Exec Wechsel, Budgetcuts, Reorganisationen — von außen passiert viel, das du nicht kontrolieren kannst.',
    mitigation: 'Wir dokumentieren alles. Workshops führen zu Entscheidungsprotokollen. Code ist auf GitHub. Bild das Team ein, nicht einzelne Personen. Weniger Abhängigkeit vom CEO = mehr Stabilität.',
  },
  {
    risk: 'Die Zusammenarbeit mit bumbleflies funktioniert nicht.',
    description: 'Passt nicht zusammen, andere Arbeitsweise, Kommunikation stimmt nicht.',
    mitigation: 'Wir starten mit einer 2-Wochen-Testphase. Nicht bindend. Sehr transparent. Du merkst schnell, ob wir zusammenpassen oder nicht. Lieber früh sagen „passt nicht" als sich festzulegen und frustriert zu sein.',
  },
];

const enRisks = [
  {
    risk: 'The organization isn\'t ready for change.',
    description: 'A common risk: Leadership says yes, but the team is skeptical or unmotivated.',
    mitigation: 'We always start with a readiness phase. Talk sessions to understand who\'s ready and where the skepticism lives. If the foundations aren\'t right, we say so openly.',
  },
  {
    risk: 'The pilot starts, but then nothing happens.',
    description: 'Workshops are exciting. But then everyday life returns. People fall back into old patterns.',
    mitigation: 'That\'s why we integrate adoption from day 1. The people using the new tool or process are part of designing it. Resistance gets built in, not ignored later.',
  },
  {
    risk: 'The software project becomes too expensive or takes too long.',
    description: 'You know this: Scope creep, underestimated complexity, one more requirement here, another there...',
    mitigation: 'We build in sprints with fixed milestones. Fixed price per phase. Clear criteria for when a phase is "done." If requirements grow, we talk about timeline or price.',
  },
  {
    risk: 'The CEO leaves, and the project gets cancelled.',
    description: 'Exec changes, budget cuts, reorganizations — things happen outside your control.',
    mitigation: 'We document everything. Workshops create decision protocols. Code is on GitHub. We build the team, not single individuals. Less CEO dependency = more stability.',
  },
  {
    risk: 'Working with bumbleflies doesn\'t work.',
    description: 'Doesn\'t fit, different working style, communication isn\'t right.',
    mitigation: 'We start with a 2-week trial phase. Non-binding. Very transparent. You quickly see whether we\'re a fit or not. Better to say "doesn\'t work" early than to commit and be frustrated.',
  },
];

const de = {
  pageTitle: 'Risiken & De-Risking',
  heading: 'Was könnte schiefgehen?',
  intro: 'Transformation ist kein Risk-freies Spiel. Wir sind nicht Hellseher. Aber wir haben Hunderte von Projekten gesehen, und wir wissen, welche Probleme wahrscheinlich sind — und wie man sie von Anfang an adressiert.',
  cta: {
    heading: 'Lass uns das Risiko besprechen.',
    body: 'Wenn du dich unsicher bist: lass uns einfach realistisch über die Chancen und Risiken sprechen.',
    ctaText: 'Erstgespräch buchen',
  },
};

const en = {
  pageTitle: 'Risk & De-Risking',
  heading: 'What could go wrong?',
  intro: 'Transformation isn\'t risk-free. We\'re not mind readers. But we\'ve seen hundreds of projects, and we know which problems are likely — and how to address them from the start.',
  cta: {
    heading: 'Let\'s talk about risk.',
    body: 'If you\'re unsure: let\'s just be realistic about chances and risks.',
    ctaText: 'Book a first call',
  },
};

const content = currentLang === 'DE' ? de : en;
const risks = currentLang === 'DE' ? deRisks : enRisks;
---

<Layout title={content.pageTitle} lang={currentLang}>
  <Nav slot="nav" lang={currentLang} />

  <section class="risk-section">
    <div class="container">
      <h1>{content.heading}</h1>
      <p class="intro">{content.intro}</p>

      <RiskAccordion items={risks} lang={currentLang} />
    </div>
  </section>

  <CTAStrip
    heading={content.cta.heading}
    body={content.cta.body}
    ctaText={content.cta.ctaText}
    lang={currentLang}
  />

  <Footer slot="footer" lang={currentLang} />

  <script>
    window.addEventListener('lang-change', (e: CustomEvent) => {
      window.location.href = `/risk-derisking/?lang=${e.detail.lang}`;
    });
  </script>
</Layout>

<style>
  .risk-section {
    padding: 4rem 2rem;
    background: #fff;
  }

  .container {
    max-width: 1000px;
    margin: 0 auto;
  }

  .risk-section h1 {
    font-family: 'Instrument Serif', serif;
    font-size: 2.5rem;
    font-weight: 400;
    line-height: 1.2;
    color: #1a1a1a;
    margin: 0 0 2rem 0;
  }

  .intro {
    font-family: 'Geist', sans-serif;
    font-size: 1.1rem;
    line-height: 1.8;
    color: #4a4a4a;
    margin: 0 0 3rem 0;
  }

  @media (max-width: 640px) {
    .risk-section {
      padding: 2rem 1rem;
    }

    .risk-section h1 {
      font-size: 1.75rem;
    }

    .intro {
      font-size: 1rem;
    }
  }
</style>
```

- [ ] **Step 3: Build and verify**

```bash
npm run build
# Verify dist/risk-derisking/index.html exists
```

- [ ] **Step 4: Commit**

```bash
git add src/pages/risk-derisking.astro src/components/RiskAccordion.astro
git commit -m "feat: add risk & de-risking page with mitigation strategies"
```

---

### Task 8: Navigation and Final Integration

**Files:**
- Modify: `src/components/Nav.astro` (add all new page links)
- Verify: All pages built successfully

- [ ] **Step 1: Update Navigation**

Add links to nav in `src/components/Nav.astro`:

```astro
# Update the nav data structure to include:
const navLinks = [
  { href: '/', label: currentLang === 'DE' ? 'Home' : 'Home' },
  { href: '/services', label: currentLang === 'DE' ? 'Services' : 'Services' },
  { href: '/how-we-work', label: currentLang === 'DE' ? 'So arbeiten wir' : 'How We Work' },
  { href: '/why-bumbleflies', label: currentLang === 'DE' ? 'Warum bumbleflies' : 'Why bumbleflies' },
  { href: '/about', label: currentLang === 'DE' ? 'Über uns' : 'About' },
  { href: '/risk-derisking', label: currentLang === 'DE' ? 'Risiken' : 'Risk & De-Risking' },
];
```

- [ ] **Step 2: Full production build**

```bash
npm run build
# Verify all 8 pages exist:
# - dist/index.html (homepage)
# - dist/case-studies/index.html (case studies listing)
# - dist/case-studies/[5 study slugs]/index.html
# - dist/services/index.html
# - dist/how-we-work/index.html
# - dist/why-bumbleflies/index.html
# - dist/about/index.html
# - dist/risk-derisking/index.html
```

- [ ] **Step 3: Local test all pages**

```bash
npm run preview
# Open http://localhost:3000 and click through:
# - Services page loads
# - How We Work page loads
# - Why Bumbleflies page loads
# - About page shows team profiles
# - Risk & De-Risking page accordion works
# - Language toggle works on all pages
# - Navigation links are correct
# - Footer is consistent
```

- [ ] **Step 4: Verify responsiveness**

```bash
# In browser DevTools:
# - Test at mobile (375px), tablet (768px), desktop (1200px)
# - All pages should be readable and functional
# - No horizontal scroll
# - Images should scale properly
```

- [ ] **Step 5: Final commit with summary**

```bash
git add src/components/Nav.astro
git commit -m "feat: complete stage 5 - add all remaining pages and finalize navigation"
```

---

## Success Criteria

- [ ] All 5 pages built and live on dev site
- [ ] Team data loaded from collection (3 members)
- [ ] Testimonials grid rendering on About page
- [ ] Services page shows all 4 offerings
- [ ] How We Work page explains integrated methodology
- [ ] Why Bumbleflies page comparison visible
- [ ] Risk & De-Risking page accordions functional
- [ ] Navigation includes all pages
- [ ] Bilingual (DE/EN) working on all pages
- [ ] Language toggle works end-to-end
- [ ] Responsive on mobile/tablet/desktop
- [ ] Build time < 1 second
- [ ] No console errors

---

## Next Phase (Phase 4: QA & Testing)

After Stage 5 completion:

1. **Lighthouse Audits** — Target 90+ all categories
2. **WCAG 2.1 AA Compliance** — Accessibility review
3. **Cross-browser Testing** — Chrome, Firefox, Safari
4. **Performance Optimization** — Caching, image optimization
5. **Link Validation** — Internal & external links working
6. **Form Testing** — Contact form submission
7. **SEO Checks** — Meta tags, schema.org, sitemaps
