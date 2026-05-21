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
  }),
});

export const collections = { 'case-studies': caseStudies, testimonials, team, pages };
