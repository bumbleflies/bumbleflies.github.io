/**
 * Transformation Journey - Scroll Controller
 * Handles scroll reveals, chapter transitions, and progress tracking
 */

(function() {
  'use strict';

  // Configuration
  const config = {
    revealThreshold: 0.15, // Show element when 15% is visible
    progressFillSelector: '#tj-progress-fill',
    chapterSelector: '.tj-chapter',
    revealSelector: '.tj-reveal',
    markerSelector: '.tj-progress__marker'
  };

  // State
  let progressFill;
  let chapters;
  let revealElements;
  let markers;
  let ticking = false;

  /**
   * Initialize the scroll controller
   */
  function init() {
    // Get elements
    progressFill = document.querySelector(config.progressFillSelector);
    chapters = Array.from(document.querySelectorAll(config.chapterSelector));
    revealElements = Array.from(document.querySelectorAll(config.revealSelector));
    markers = Array.from(document.querySelectorAll(config.markerSelector));

    if (!progressFill || chapters.length === 0) {
      console.log('Transformation Journey elements not found, skipping initialization');
      return;
    }

    // Set up Intersection Observer for reveals
    setupRevealObserver();

    // Set up scroll listener for progress bar
    window.addEventListener('scroll', onScroll);

    // Set up smooth scrolling for chapter markers
    setupMarkerClicks();

    // Initial state
    updateProgress();
    updateActiveChapter();
  }

  /**
   * Set up Intersection Observer for reveal animations
   */
  function setupRevealObserver() {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: config.revealThreshold
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          // Apply delay if specified
          const delay = entry.target.dataset.revealDelay || 0;
          setTimeout(() => {
            entry.target.classList.add('tj-revealed');
          }, parseInt(delay));

          // Unobserve after revealing (one-time animation)
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach(el => observer.observe(el));
  }

  /**
   * Handle scroll event (throttled with requestAnimationFrame)
   */
  function onScroll() {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        updateProgress();
        updateActiveChapter();
        ticking = false;
      });
      ticking = true;
    }
  }

  /**
   * Update progress bar fill based on scroll position
   */
  function updateProgress() {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight - windowHeight;
    const scrolled = window.pageYOffset;
    const progress = (scrolled / documentHeight) * 100;

    if (progressFill) {
      progressFill.style.height = `${Math.min(progress, 100)}%`;
    }
  }

  /**
   * Update active chapter marker based on scroll position
   */
  function updateActiveChapter() {
    const scrollPosition = window.pageYOffset + (window.innerHeight / 2);

    chapters.forEach((chapter, index) => {
      if (!chapter) return; // Skip if chapter element doesn't exist

      const chapterTop = chapter.offsetTop;
      const chapterBottom = chapterTop + chapter.offsetHeight;

      if (scrollPosition >= chapterTop && scrollPosition < chapterBottom) {
        // Update marker active state
        markers.forEach(m => m.classList.remove('active'));
        if (markers[index]) {
          markers[index].classList.add('active');
        }
      }
    });
  }

  /**
   * Set up smooth scrolling for chapter markers
   */
  function setupMarkerClicks() {
    markers.forEach(marker => {
      marker.addEventListener('click', (e) => {
        e.preventDefault();
        const targetId = marker.getAttribute('href');
        const targetElement = document.querySelector(targetId);

        if (targetElement) {
          const offset = 0; // No offset, full-screen chapters
          const targetPosition = targetElement.offsetTop - offset;

          window.scrollTo({
            top: targetPosition,
            behavior: 'smooth'
          });
        }
      });
    });
  }

  /**
   * Reduced motion support
   * If user prefers reduced motion, disable animations
   */
  function checkReducedMotion() {
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    if (prefersReducedMotion) {
      // Immediately reveal all elements
      revealElements.forEach(el => {
        el.classList.add('tj-revealed');
        el.style.transition = 'none';
      });
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
      checkReducedMotion();
      init();
    });
  } else {
    checkReducedMotion();
    init();
  }

})();
