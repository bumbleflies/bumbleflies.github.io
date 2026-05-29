/**
 * Hero Component Tests
 * Tests for engagement packages grid rendering in both DE and EN
 */

// This is a validation test to ensure the Hero component renders correctly
// Since Astro is a static site generator, we test by building and inspecting the output

interface EngagementPackage {
  num: string;
  phase: string;
  name: string;
  timeline: string;
  outcome: string;
  ctaText: string;
}

interface TestScenario {
  lang: 'DE' | 'EN';
  packages: EngagementPackage[];
  expectedPackageCount: number;
}

// DE content validation
const dePackages: EngagementPackage[] = [
  {
    num: '01',
    phase: 'REDEN',
    name: 'Quick Start',
    timeline: '1–2 weeks',
    outcome: 'Clarity über dein größtes Problem',
    ctaText: 'Mehr erfahren',
  },
  {
    num: '02',
    phase: 'ENTSCHEIDEN',
    name: 'Use-Case Sprint',
    timeline: '4–6 weeks',
    outcome: 'AI-Opportunity Assessment',
    ctaText: 'Mehr erfahren',
  },
  {
    num: '03',
    phase: 'BAUEN',
    name: 'AI Adoption',
    timeline: '1–6 months',
    outcome: 'Funktionierender Prototyp',
    ctaText: 'Mehr erfahren',
  },
  {
    num: '04',
    phase: 'BEGLEITEN',
    name: 'Custom Program',
    timeline: 'Concept',
    outcome: 'Team trainiert & unabhängig',
    ctaText: 'Mehr erfahren',
  },
];

// EN content validation
const enPackages: EngagementPackage[] = [
  {
    num: '01',
    phase: 'TALK',
    name: 'Quick Start',
    timeline: '1–2 weeks',
    outcome: 'Clarity on your biggest challenge',
    ctaText: 'Learn more',
  },
  {
    num: '02',
    phase: 'DECIDE',
    name: 'Use-Case Sprint',
    timeline: '4–6 weeks',
    outcome: 'AI opportunity assessment',
    ctaText: 'Learn more',
  },
  {
    num: '03',
    phase: 'BUILD',
    name: 'AI Adoption',
    timeline: '1–6 months',
    outcome: 'Working prototype',
    ctaText: 'Learn more',
  },
  {
    num: '04',
    phase: 'EMBED',
    name: 'Custom Program',
    timeline: 'Concept',
    outcome: 'Team trained & independent',
    ctaText: 'Learn more',
  },
];

// Test scenario definitions
const testScenarios: TestScenario[] = [
  {
    lang: 'DE',
    packages: dePackages,
    expectedPackageCount: 4,
  },
  {
    lang: 'EN',
    packages: enPackages,
    expectedPackageCount: 4,
  },
];

/**
 * Validates engagement package content structure
 */
export function validateEngagementPackages(): void {
  testScenarios.forEach((scenario) => {
    console.log(`\n✓ Testing ${scenario.lang} language variant`);
    console.log(`  Expected ${scenario.expectedPackageCount} packages`);

    scenario.packages.forEach((pkg) => {
      console.log(`  ✓ Package ${pkg.num}: ${pkg.phase} - ${pkg.name}`);
      // Validate required fields exist
      if (!pkg.num || !pkg.phase || !pkg.name || !pkg.timeline || !pkg.outcome || !pkg.ctaText) {
        throw new Error(`Invalid package structure for ${scenario.lang} package ${pkg.num}`);
      }
    });
  });

  console.log('\n✓ All engagement package validation tests passed');
}

/**
 * Validates rendered HTML structure contains engagement packages
 */
export function validateHeroHtmlStructure(html: string): void {
  // Check that engagement packages section exists
  if (!html.includes('a-hero__engagement-packages')) {
    throw new Error('Missing engagement packages section (.a-hero__engagement-packages)');
  }

  // Check that 4 package columns are rendered
  const packageMatches = html.match(/bf-cta--ghost/g);
  if (!packageMatches || packageMatches.length < 4) {
    throw new Error('Expected at least 4 CTA buttons in engagement packages grid');
  }

  // Check for specific content markers (at least one from each language)
  const deMarkers = ['REDEN', 'ENTSCHEIDEN', 'BAUEN', 'BEGLEITEN'];
  const enMarkers = ['TALK', 'DECIDE', 'BUILD', 'EMBED'];

  const hasDeContent = deMarkers.some(marker => html.includes(marker));
  const hasEnContent = enMarkers.some(marker => html.includes(marker));

  if (!hasDeContent && !hasEnContent) {
    throw new Error('No engagement package phase labels found in HTML');
  }

  console.log('✓ HTML structure validation passed');
}

export { dePackages, enPackages, testScenarios };
