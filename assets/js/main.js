/**
 * PANCAKE & BREAKFAST HOUSE — GLOBAL JAVASCRIPT (main.js)
 * Shared across Home, Menu, Group Bookings, and Contact
 */

(function () {
  'use strict';

  // Storage keys
  const THEME_KEY = 'pb_theme';
  const DIR_KEY = 'pb_dir';

  // DOM Elements
  const htmlEl = document.documentElement;
  const header = document.querySelector('.site-header');
  const drawer = document.getElementById('mobileDrawer');
  const drawerBackdrop = document.getElementById('drawerBackdrop');
  const hamburgerBtn = document.getElementById('hamburgerBtn');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const backToTopBtn = document.getElementById('backToTopBtn');
  const newsletterForm = document.getElementById('footerNewsletterForm');
  const newsletterInput = document.getElementById('newsletterEmail');
  const newsletterMsg = document.getElementById('newsletterMsg');

  /* ==========================================================================
     THEME (LIGHT / DARK) SYSTEM
     ========================================================================== */
  function getPreferredTheme() {
    const saved = localStorage.getItem(THEME_KEY);
    if (saved) return saved;
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark'
      : 'light';
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      htmlEl.setAttribute('data-theme', 'dark');
      document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
        btn.setAttribute('aria-label', 'Switch to light mode');
        btn.setAttribute('title', 'Switch to light mode');
        const icon = btn.querySelector('.theme-icon-use');
        if (icon) {
          icon.innerHTML = `
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          `;
        }
      });
    } else {
      htmlEl.removeAttribute('data-theme');
      document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
        btn.setAttribute('aria-label', 'Switch to dark mode');
        btn.setAttribute('title', 'Switch to dark mode');
        const icon = btn.querySelector('.theme-icon-use');
        if (icon) {
          icon.innerHTML = `
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          `;
        }
      });
    }
  }

  function toggleTheme() {
    const current = htmlEl.getAttribute('data-theme') === 'dark' ? 'dark' : 'light';
    const next = current === 'dark' ? 'light' : 'dark';
    localStorage.setItem(THEME_KEY, next);
    applyTheme(next);
  }

  // Initial theme apply
  applyTheme(getPreferredTheme());

  /* ==========================================================================
     DIRECTION (LTR / RTL) SYSTEM
     ========================================================================== */
  function getPreferredDir() {
    return localStorage.getItem(DIR_KEY) || 'ltr';
  }

  function applyDir(dir) {
    htmlEl.setAttribute('dir', dir);
    document.querySelectorAll('.dir-toggle-btn').forEach(btn => {
      btn.setAttribute('aria-label', dir === 'rtl' ? 'Switch to Left to Right' : 'Switch to Right to Left');
      btn.setAttribute('title', dir === 'rtl' ? 'Switch to LTR' : 'Switch to RTL');
      const textSpan = btn.querySelector('.dir-label-text');
      if (textSpan) {
        textSpan.textContent = dir === 'rtl' ? 'LTR' : 'RTL';
      }
    });
  }

  function toggleDir() {
    const current = htmlEl.getAttribute('dir') || 'ltr';
    const next = current === 'rtl' ? 'ltr' : 'rtl';
    localStorage.setItem(DIR_KEY, next);
    applyDir(next);
  }

  // Initial direction apply
  applyDir(getPreferredDir());

  /* ==========================================================================
     DRAWER & HAMBURGER NAVIGATION
     ========================================================================== */
  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('is-active');
    if (drawerBackdrop) drawerBackdrop.classList.add('is-active');
    if (hamburgerBtn) hamburgerBtn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
    if (drawerCloseBtn) drawerCloseBtn.focus();
  }

  function closeDrawer() {
    if (!drawer) return;
    drawer.classList.remove('is-active');
    if (drawerBackdrop) drawerBackdrop.classList.remove('is-active');
    if (hamburgerBtn) {
      hamburgerBtn.setAttribute('aria-expanded', 'false');
      hamburgerBtn.focus();
    }
    document.body.style.overflow = '';
  }

  if (hamburgerBtn) {
    hamburgerBtn.addEventListener('click', function (e) {
      e.preventDefault();
      const isOpen = drawer && drawer.classList.contains('is-active');
      if (isOpen) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });
  }

  if (drawerCloseBtn) {
    drawerCloseBtn.addEventListener('click', function (e) {
      e.preventDefault();
      closeDrawer();
    });
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', closeDrawer);
  }

  // Close drawer on clicking navigation links (excluding dropdown toggle buttons)
  document.querySelectorAll('.mobile-drawer a').forEach(link => {
    link.addEventListener('click', () => {
      closeDrawer();
    });
  });

  /* ==========================================================================
     MOBILE ACCORDION DROPDOWNS
     ========================================================================== */
  const mobileDropdownBtns = document.querySelectorAll('.mobile-dropdown-btn');
  mobileDropdownBtns.forEach(btn => {
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      const parent = btn.closest('.mobile-dropdown-item');
      const submenu = parent ? parent.querySelector('.mobile-submenu') : null;
      if (!submenu) return;
      const isOpen = submenu.classList.contains('is-open');

      // Close all other open submenus (accordion behavior)
      mobileDropdownBtns.forEach(otherBtn => {
        if (otherBtn !== btn) {
          otherBtn.setAttribute('aria-expanded', 'false');
          const otherParent = otherBtn.closest('.mobile-dropdown-item');
          const otherSubmenu = otherParent ? otherParent.querySelector('.mobile-submenu') : null;
          if (otherSubmenu) {
            otherSubmenu.classList.remove('is-open');
          }
        }
      });

      if (isOpen) {
        submenu.classList.remove('is-open');
        btn.setAttribute('aria-expanded', 'false');
      } else {
        submenu.classList.add('is-open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });

  /* ==========================================================================
     DESKTOP DROPDOWNS (CLICK & HOVER SUPPORT)
     ========================================================================== */
  const desktopDropdowns = document.querySelectorAll('.nav-item-dropdown');
  desktopDropdowns.forEach(dropdown => {
    const toggleBtn = dropdown.querySelector('.dropdown-toggle');
    if (!toggleBtn) return;

    // Toggle on click
    toggleBtn.addEventListener('click', function (e) {
      if (window.innerWidth >= 1281) {
        e.preventDefault();
        e.stopPropagation();
        const isOpen = dropdown.classList.contains('is-open');

        // Close other desktop dropdowns
        desktopDropdowns.forEach(other => {
          if (other !== dropdown) {
            other.classList.remove('is-open');
            const otherBtn = other.querySelector('.dropdown-toggle');
            if (otherBtn) otherBtn.setAttribute('aria-expanded', 'false');
          }
        });

        if (isOpen) {
          dropdown.classList.remove('is-open');
          toggleBtn.setAttribute('aria-expanded', 'false');
        } else {
          dropdown.classList.add('is-open');
          toggleBtn.setAttribute('aria-expanded', 'true');
        }
      }
    });

    // On hover entry/exit, maintain proper aria-expanded
    dropdown.addEventListener('mouseenter', function () {
      if (window.innerWidth >= 1281) {
        toggleBtn.setAttribute('aria-expanded', 'true');
      }
    });
    dropdown.addEventListener('mouseleave', function () {
      if (window.innerWidth >= 1281 && !dropdown.classList.contains('is-open')) {
        toggleBtn.setAttribute('aria-expanded', 'false');
      }
    });
  });

  // Close desktop dropdowns on outside click
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.nav-item-dropdown')) {
      desktopDropdowns.forEach(dropdown => {
        dropdown.classList.remove('is-open');
        const toggleBtn = dropdown.querySelector('.dropdown-toggle');
        if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      desktopDropdowns.forEach(dropdown => {
        dropdown.classList.remove('is-open');
        const toggleBtn = dropdown.querySelector('.dropdown-toggle');
        if (toggleBtn) toggleBtn.setAttribute('aria-expanded', 'false');
      });
      if (drawer && drawer.classList.contains('is-active')) {
        closeDrawer();
      }
    }
  });

  // Attach Theme and RTL buttons
  document.querySelectorAll('.theme-toggle-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleTheme();
    });
  });

  document.querySelectorAll('.dir-toggle-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      toggleDir();
    });
  });

  /* ==========================================================================
     ACTIVE PAGE & SECTION INDICATOR
     ========================================================================== */
  function markActiveNav() {
    let currentPath = window.location.pathname.split('/').pop() || 'index.html';
    if (!currentPath || currentPath === '' || currentPath === '/') {
      currentPath = 'index.html';
    }

    // Reset all nav active states
    document.querySelectorAll('.navbar-nav-desktop .nav-link, .mobile-nav-link, .dropdown-item-custom, .mobile-sublink').forEach(el => {
      el.classList.remove('active');
      el.removeAttribute('aria-current');
    });

    // Check Home (Home 1 or Home 2)
    if (currentPath === 'index.html') {
      const homeBtn = document.getElementById('homeDropdown');
      const mobileHomeBtn = document.getElementById('mobileHomeDropdownBtn');
      if (homeBtn) homeBtn.classList.add('active');
      if (mobileHomeBtn) mobileHomeBtn.classList.add('active');

      document.querySelectorAll('a[href="index.html"].dropdown-item-custom, a[href="index.html"].mobile-sublink').forEach(a => {
        a.classList.add('active');
      });
    } else if (currentPath === 'home-2.html') {
      const homeBtn = document.getElementById('homeDropdown');
      const mobileHomeBtn = document.getElementById('mobileHomeDropdownBtn');
      if (homeBtn) homeBtn.classList.add('active');
      if (mobileHomeBtn) mobileHomeBtn.classList.add('active');

      document.querySelectorAll('a[href="home-2.html"].dropdown-item-custom, a[href="home-2.html"].mobile-sublink').forEach(a => {
        a.classList.add('active');
      });
    } else if (currentPath === 'menu.html') {
      document.querySelectorAll('a[href="menu.html"].nav-link, a[href="menu.html"].mobile-nav-link').forEach(a => {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      });
    } else if (currentPath === 'about.html') {
      document.querySelectorAll('a[href="about.html"].nav-link, a[href="about.html"].mobile-nav-link').forEach(a => {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      });
    } else if (currentPath === 'group-bookings.html') {
      document.querySelectorAll('a[href="group-bookings.html"].nav-link, a[href="group-bookings.html"].mobile-nav-link').forEach(a => {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      });
    } else if (currentPath === 'contact.html') {
      document.querySelectorAll('a[href="contact.html"].nav-link, a[href="contact.html"].mobile-nav-link').forEach(a => {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      });
    }
  }

  markActiveNav();
  window.addEventListener('hashchange', markActiveNav);

  /* ==========================================================================
     BACK TO TOP
     ========================================================================== */
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  /* ==========================================================================
     NEWSLETTER FORM (DEMO VALIDATION)
     ========================================================================== */
  if (newsletterForm && newsletterInput && newsletterMsg) {
    newsletterForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const val = newsletterInput.value.trim();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

      if (!val || !emailRegex.test(val)) {
        newsletterMsg.textContent = 'Please enter a valid email address.';
        newsletterMsg.className = 'newsletter-message is-visible is-error';
        newsletterInput.focus();
        return;
      }

      newsletterMsg.textContent = 'Thank you for your interest! (Demo mode: no actual emails collected).';
      newsletterMsg.className = 'newsletter-message is-visible is-success';
      newsletterInput.value = '';

      setTimeout(() => {
        newsletterMsg.className = 'newsletter-message';
      }, 6000);
    });
  }

})();
