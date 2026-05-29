import { defineCollection, z } from 'astro:content';

const caseStudies = defineCollection({
  schema: z.object({
    title: z.string(),
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
    published: z.boolean().default(true),
    // Flexible fields for different page types
    eyebrow: z.string().optional(),
    heading: z.string().optional(),
    subheading: z.string().optional(),
    intro: z.string().optional(),
    // For homepage services/formats
    services: z.array(z.object({
      number: z.string(),
      title: z.string(),
      tag: z.string(),
      description: z.string(),
      bullets: z.array(z.string()),
      formats: z.array(z.object({
        kind: z.string(),
        label: z.string(),
      })),
    })).optional(),
    // For process/steps pages
    steps: z.array(z.object({
      number: z.string(),
      title: z.string(),
      description: z.string(),
    })).optional(),
    // For comparison/why pages
    comparisonRows: z.array(z.object({
      label: z.string(),
      fragmented: z.string(),
      integrated: z.string(),
    })).optional(),
    // For how-we-work pages
    problemTitle: z.string().optional(),
    problemBullets: z.array(z.string()).optional(),
    solutionTitle: z.string().optional(),
    solutionBullets: z.array(z.string()).optional(),
    // For CTAs
    ctaHeading: z.string().optional(),
    ctaHeading_em: z.string().optional(),
    ctaBody: z.string().optional(),
    ctaText: z.string().optional(),
    cta: z.object({
      text: z.string(),
      link: z.string(),
    }).optional(),
    // For quotes
    quote: z.string().optional(),
    quoteCite: z.string().optional(),
    // Legal page language indicator
    lang: z.string().optional(),
  }),
});

export const collections = { 'case-studies': caseStudies, testimonials, team, pages };
