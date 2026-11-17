/**
 * PANCAKE & BREAKFAST HOUSE — ABOUT JAVASCRIPT (about.js)
 * Interactions for "The Story Behind Every Good Morning"
 * Accessible Lightbox and Scroll Revelations
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    /* ==========================================================================
       GALLERY LIGHTBOX
       ========================================================================== */
    const galleryItems = document.querySelectorAll('.about-gallery-item');
    const lightbox = document.getElementById('aboutLightbox');
    const lightboxImg = document.getElementById('aboutLightboxImg');
    const lightboxCaption = document.getElementById('aboutLightboxCaption');
    const lightboxClose = document.getElementById('aboutLightboxClose');
    const lightboxPrev = document.getElementById('aboutLightboxPrev');
    const lightboxNext = document.getElementById('aboutLightboxNext');

    let currentIndex = 0;
    const galleryData = [];

    galleryItems.forEach((item, index) => {
      const img = item.querySelector('.about-gallery-img');
      const caption = item.querySelector('.about-gallery-caption')?.textContent || '';
      if (img) {
        galleryData.push({
          src: img.getAttribute('src'),
          alt: img.getAttribute('alt') || '',
          caption: caption
        });

        item.addEventListener('click', () => {
          openLightbox(index);
        });

        item.setAttribute('tabindex', '0');
        item.setAttribute('role', 'button');
        item.setAttribute('aria-label', `View ${caption} photo in full size`);
        item.addEventListener('keydown', (e) => {
          if (e.key === 'Enter' || e.key === ' ') {
            e.preventDefault();
            openLightbox(index);
          }
        });
      }
    });

    function updateLightbox(index) {
      if (!galleryData[index]) return;
      currentIndex = index;
      if (lightboxImg) {
        lightboxImg.src = galleryData[index].src;
        lightboxImg.alt = galleryData[index].alt;
      }
      if (lightboxCaption) {
        lightboxCaption.textContent = galleryData[index].caption;
      }
    }

    function openLightbox(index) {
      if (!lightbox) return;
      updateLightbox(index);
      lightbox.classList.add('active');
      document.body.style.overflow = 'hidden';
      if (lightboxClose) lightboxClose.focus();
    }

    function closeLightbox() {
      if (!lightbox) return;
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
      if (galleryItems[currentIndex]) {
        galleryItems[currentIndex].focus();
      }
    }

    function prevImage() {
      const newIndex = (currentIndex - 1 + galleryData.length) % galleryData.length;
      updateLightbox(newIndex);
    }

    function nextImage() {
      const newIndex = (currentIndex + 1) % galleryData.length;
      updateLightbox(newIndex);
    }

    if (lightboxClose) {
      lightboxClose.addEventListener('click', closeLightbox);
    }
    if (lightboxPrev) {
      lightboxPrev.addEventListener('click', prevImage);
    }
    if (lightboxNext) {
      lightboxNext.addEventListener('click', nextImage);
    }

    if (lightbox) {
      lightbox.addEventListener('click', (e) => {
        if (e.target === lightbox) {
          closeLightbox();
        }
      });
    }

    document.addEventListener('keydown', (e) => {
      if (!lightbox || !lightbox.classList.contains('active')) return;
      if (e.key === 'Escape') {
        closeLightbox();
      } else if (e.key === 'ArrowLeft') {
        prevImage();
      } else if (e.key === 'ArrowRight') {
        nextImage();
      }
    });

    /* ==========================================================================
       HASH NAVIGATION SMOOTH SCROLLING
       ========================================================================== */
    function handleHashScroll() {
      const hash = window.location.hash.replace('#', '');
      if (!hash) return;
      const targetEl = document.getElementById(hash);
      if (targetEl) {
        const headerHeight = document.querySelector('.site-header')?.offsetHeight || 88;
        const targetTop = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight - 16;
        window.scrollTo({
          top: targetTop,
          behavior: 'smooth'
        });
      }
    }

    if (window.location.hash) {
      setTimeout(handleHashScroll, 250);
    }
    window.addEventListener('hashchange', handleHashScroll);

    /* ==========================================================================
       INTERSECTION OBSERVER CARD REVEALS
       ========================================================================== */
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(function (entries, obs) {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('about-revealed');
            obs.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -40px 0px', threshold: 0.1 });

      document.querySelectorAll('.about-philosophy-card, .about-story-item, .about-gallery-item, .about-thumb-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(16px)';
        el.style.transition = 'opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
        observer.observe(el);
      });

      const style = document.createElement('style');
      style.innerHTML = `
        .about-revealed {
          opacity: 1 !important;
          transform: translateY(0) !important;
        }
      `;
      document.head.appendChild(style);
    }
  });
})();
