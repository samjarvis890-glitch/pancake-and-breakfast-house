/**
 * PANCAKE & BREAKFAST HOUSE — HOMEPAGE JAVASCRIPT (home.js)
 */

(function () {
  'use strict';

  // Homepage Specific Interactive Enhancements
  document.addEventListener('DOMContentLoaded', function () {
    // Gallery subtle keyboard / touch accessibility
    const galleryItems = document.querySelectorAll('.gallery-item');
    galleryItems.forEach(item => {
      item.setAttribute('tabindex', '0');
      item.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          const img = item.querySelector('img');
          if (img) {
            // Focus image smoothly
            img.style.transform = 'scale(1.05)';
            setTimeout(() => {
              img.style.transform = '';
            }, 600);
          }
        }
      });
    });

    // Subtle scroll reveal class for hero
    const heroVisual = document.querySelector('.hero-visual-container');
    if (heroVisual) {
      heroVisual.style.opacity = '1';
    }
  });
})();
