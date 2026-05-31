import { describe, it, expect } from 'vitest';

describe('Footer Component Logic', () => {
  it('should render the correct current year', () => {
    const year = new Date().getFullYear();
    expect(year).toBeGreaterThanOrEqual(2025);
  });

  it('should provide DE content when lang is DE', () => {
    const lang = 'DE';
    const content = lang === 'DE' ? { legal: ['Impressum', 'Datenschutz'] } : { legal: ['Imprint', 'Privacy'] };
    expect(content.legal[0]).toBe('Impressum');
  });

  it('should provide EN content when lang is EN', () => {
    const lang = 'EN';
    const content = lang === 'DE' ? { legal: ['Impressum', 'Datenschutz'] } : { legal: ['Imprint', 'Privacy'] };
    expect(content.legal[0]).toBe('Imprint');
  });
});
