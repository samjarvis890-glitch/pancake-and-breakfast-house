/**
 * PANCAKE & BREAKFAST HOUSE — HOME 2 JAVASCRIPT (home-2.js)
 * Interactions for "The Cosy Morning Experience"
 */

(function () {
  'use strict';

  // Smooth appearance observation for cards & moments
  document.addEventListener('DOMContentLoaded', function () {
    const observerOptions = {
      root: null,
      rootMargin: '0px',
      threshold: 0.15
    };

    if ('IntersectionObserver' in window) {
      const revealObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('home2-revealed');
            observer.unobserve(entry.target);
          }
        });
      }, observerOptions);

      document.querySelectorAll('.home2-taste-card, .home2-moment-card, .home2-highlight-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s cubic-bezier(0.16, 1, 0.3, 1), transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
        revealObserver.observe(el);
      });

      // Add revealed transition class
      const style = document.createElement('style');
      style.innerHTML = `
        .home2-revealed {
          opacity: 1 !important;
          transform: translateY(0) !important;
        }
      `;
      document.head.appendChild(style);
    }
  });

})();
