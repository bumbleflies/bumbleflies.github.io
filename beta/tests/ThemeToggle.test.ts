import { describe, it, expect, vi, beforeEach } from 'vitest';

describe('ThemeToggle Logic', () => {
  beforeEach(() => {
    // Mock localStorage and documentElement
    const storage: Record<string, string> = {};
    global.localStorage = {
      getItem: (key: string) => storage[key] || null,
      setItem: (key: string, value: string) => { storage[key] = value; },
      removeItem: (key: string) => { delete storage[key]; },
      clear: () => { Object.keys(storage).forEach(k => delete storage[k]); },
      length: 0,
      key: (index: number) => null,
    } as any;

    document.documentElement.removeAttribute('data-theme');
  });

  it('should toggle theme from light to dark', () => {
    const element = document.documentElement;
    
    // Simulate initial state (light)
    expect(element.getAttribute('data-theme')).toBeNull();

    // Toggle logic (simplified version of the script in component)
    const isDark = element.getAttribute('data-theme') === 'dark';
    if (isDark) {
      element.removeAttribute('data-theme');
      localStorage.setItem('theme', 'light');
    } else {
      element.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    }

    expect(element.getAttribute('data-theme')).toBe('dark');
    expect(localStorage.getItem('theme')).toBe('dark');
  });

  it('should toggle theme from dark to light', () => {
    const element = document.documentElement;
    element.setAttribute('data-theme', 'dark');
    
    // Toggle logic
    const isDark = element.getAttribute('data-theme') === 'dark';
    if (isDark) {
      element.removeAttribute('data-theme');
      localStorage.setItem('theme', 'light');
    } else {
      element.setAttribute('data-theme', 'dark');
      localStorage.setItem('theme', 'dark');
    }

    expect(element.getAttribute('data-theme')).toBeNull();
    expect(localStorage.getItem('theme')).toBe('light');
  });
});
