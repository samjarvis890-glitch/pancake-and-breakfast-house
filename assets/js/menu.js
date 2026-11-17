/**
 * PANCAKE & BREAKFAST HOUSE — MENU JAVASCRIPT (menu.js)
 * Interactive category filtering, search, and hash-based navigation
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    const filterBtns = document.querySelectorAll('.menu-filter-btn');
    const searchInput = document.getElementById('menuSearchInput');
    const searchClearBtn = document.getElementById('menuSearchClear');
    const interactiveGrid = document.getElementById('menuInteractiveGrid');
    const emptyState = document.getElementById('menuEmptyState');
    const emptyResetBtn = document.getElementById('menuEmptyResetBtn');
    const menuCards = document.querySelectorAll('.menu-filter-target');

    let currentCategory = 'all';
    let searchQuery = '';

    // Apply filtering logic
    function applyFilter() {
      let visibleCount = 0;
      const normalizedQuery = searchQuery.trim().toLowerCase();

      menuCards.forEach(card => {
        const itemCategory = card.getAttribute('data-category') || '';
        const itemName = (card.querySelector('.menu-item-title')?.textContent || '').toLowerCase();
        const itemDesc = (card.querySelector('.menu-item-desc')?.textContent || '').toLowerCase();

        const matchesCategory = currentCategory === 'all' || itemCategory === currentCategory;
        const matchesSearch = !normalizedQuery || itemName.includes(normalizedQuery) || itemDesc.includes(normalizedQuery);

        if (matchesCategory && matchesSearch) {
          card.style.display = '';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      // Show/hide empty state
      if (emptyState && interactiveGrid) {
        if (visibleCount === 0) {
          emptyState.style.display = 'block';
          interactiveGrid.style.display = 'none';
        } else {
          emptyState.style.display = 'none';
          interactiveGrid.style.display = '';
        }
      }
    }

    // Set active category button
    function setCategory(category) {
      currentCategory = category;
      filterBtns.forEach(btn => {
        if (btn.getAttribute('data-filter') === category) {
          btn.classList.add('active');
          btn.setAttribute('aria-pressed', 'true');
        } else {
          btn.classList.remove('active');
          btn.setAttribute('aria-pressed', 'false');
        }
      });
      applyFilter();
    }

    // Filter button click events
    filterBtns.forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const cat = this.getAttribute('data-filter');
        setCategory(cat);
      });
    });

    // Search input event
    if (searchInput) {
      searchInput.addEventListener('input', function () {
        searchQuery = this.value;
        if (searchClearBtn) {
          searchClearBtn.style.display = searchQuery.length > 0 ? 'inline-flex' : 'none';
        }
        applyFilter();
      });
    }

    // Clear search button
    if (searchClearBtn && searchInput) {
      searchClearBtn.addEventListener('click', function () {
        searchInput.value = '';
        searchQuery = '';
        searchClearBtn.style.display = 'none';
        searchInput.focus();
        applyFilter();
      });
    }

    // Empty state reset button
    if (emptyResetBtn) {
      emptyResetBtn.addEventListener('click', function () {
        if (searchInput) {
          searchInput.value = '';
          searchQuery = '';
        }
        if (searchClearBtn) {
          searchClearBtn.style.display = 'none';
        }
        setCategory('all');
      });
    }

    // Handle hash navigation (e.g., #pancakes, #waffles, #breakfast-plates, etc.)
    function handleHash() {
      const hash = window.location.hash.replace('#', '');
      if (!hash) return;

      const validCategories = [
        'pancakes',
        'waffles',
        'breakfast-plates',
        'eggs-toast',
        'bowls-light-bites',
        'coffee-drinks',
        'sweet-treats'
      ];

      if (validCategories.includes(hash)) {
        // Also update filter bar category for seamless user experience
        setCategory(hash);

        // Scroll to the specific section smoothly
        const targetEl = document.getElementById(hash);
        if (targetEl) {
          const headerHeight = document.querySelector('.site-header')?.offsetHeight || 88;
          const targetTop = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight - 16;
          window.scrollTo({
            top: targetTop,
            behavior: 'smooth'
          });
        }
      } else if (hash === 'menu-collection') {
        const targetEl = document.getElementById('menu-collection');
        if (targetEl) {
          const headerHeight = document.querySelector('.site-header')?.offsetHeight || 88;
          const targetTop = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight - 16;
          window.scrollTo({
            top: targetTop,
            behavior: 'smooth'
          });
        }
      }
    }

    // Check hash on load and on hashchange
    if (window.location.hash) {
      setTimeout(handleHash, 250);
    }
    window.addEventListener('hashchange', handleHash);

    // Subtle scroll reveal animations
    if ('IntersectionObserver' in window) {
      const cardObserver = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('menu-revealed');
            observer.unobserve(entry.target);
          }
        });
      }, { rootMargin: '0px 0px -50px 0px', threshold: 0.1 });

      document.querySelectorAll('.menu-item-card, .menu-beyond-card, .menu-split-card').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(16px)';
        el.style.transition = 'opacity 0.5s cubic-bezier(0.16, 1, 0.3, 1), transform 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
        cardObserver.observe(el);
      });

      const style = document.createElement('style');
      style.innerHTML = `
        .menu-revealed {
          opacity: 1 !important;
          transform: translateY(0) !important;
        }
      `;
      document.head.appendChild(style);
    }
  });
})();
