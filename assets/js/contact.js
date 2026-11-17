/**
 * PANCAKE & BREAKFAST HOUSE — CONTACT PAGE JAVASCRIPT (contact.js)
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    const contactForm = document.getElementById('restaurantContactForm');
    const noticeBox = document.getElementById('contactNotice');

    if (!contactForm) return;

    const fields = {
      name: document.getElementById('contactName'),
      email: document.getElementById('contactEmail'),
      phone: document.getElementById('contactPhone'),
      type: document.getElementById('contactType'),
      subject: document.getElementById('contactSubject'),
      message: document.getElementById('contactMessage'),
      privacy: document.getElementById('contactPrivacy')
    };

    // Remove validation errors on user input
    Object.values(fields).forEach(input => {
      if (!input) return;
      const eventType = input.type === 'checkbox' || input.tagName === 'SELECT' ? 'change' : 'input';
      input.addEventListener(eventType, function () {
        if (input.classList.contains('is-invalid')) {
          input.classList.remove('is-invalid');
        }
      });
    });

    // Form Submission
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      let isValid = true;
      let firstErrorField = null;

      // 1. Name validation
      if (!fields.name.value.trim() || fields.name.value.trim().length < 2) {
        fields.name.classList.add('is-invalid');
        isValid = false;
        if (!firstErrorField) firstErrorField = fields.name;
      } else {
        fields.name.classList.remove('is-invalid');
      }

      // 2. Email validation
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!fields.email.value.trim() || !emailRegex.test(fields.email.value.trim())) {
        fields.email.classList.add('is-invalid');
        isValid = false;
        if (!firstErrorField) firstErrorField = fields.email;
      } else {
        fields.email.classList.remove('is-invalid');
      }

      // 3. Enquiry Type validation
      if (!fields.type.value) {
        fields.type.classList.add('is-invalid');
        isValid = false;
        if (!firstErrorField) firstErrorField = fields.type;
      } else {
        fields.type.classList.remove('is-invalid');
      }

      // 4. Subject validation
      if (!fields.subject.value.trim() || fields.subject.value.trim().length < 3) {
        fields.subject.classList.add('is-invalid');
        isValid = false;
        if (!firstErrorField) firstErrorField = fields.subject;
      } else {
        fields.subject.classList.remove('is-invalid');
      }

      // 5. Message validation
      if (!fields.message.value.trim() || fields.message.value.trim().length < 8) {
        fields.message.classList.add('is-invalid');
        isValid = false;
        if (!firstErrorField) firstErrorField = fields.message;
      } else {
        fields.message.classList.remove('is-invalid');
      }

      // 6. Privacy Checkbox validation
      if (!fields.privacy.checked) {
        fields.privacy.classList.add('is-invalid');
        isValid = false;
        if (!firstErrorField) firstErrorField = fields.privacy;
      } else {
        fields.privacy.classList.remove('is-invalid');
      }

      if (!isValid) {
        if (firstErrorField) {
          firstErrorField.focus();
        }
        return;
      }

      // Show strict non-negotiable frontend demo notice
      if (noticeBox) {
        noticeBox.classList.add('is-active');
        noticeBox.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
      }

      // Reset form fields
      contactForm.reset();

      // Auto hide notice after 12 seconds
      setTimeout(function () {
        if (noticeBox) {
          noticeBox.classList.remove('is-active');
        }
      }, 12000);
    });

    // Handle "Get Directions" / "Open in Google Maps" placeholder click
    const directionsBtn = document.getElementById('getDirectionsBtn');
    const openMapsBtn = document.getElementById('openMapsBtn');

    function handleMapAction(e) {
      e.preventDefault();
      alert('Restaurant directions will be available once the exact physical restaurant address is confirmed.');
    }

    if (directionsBtn) directionsBtn.addEventListener('click', handleMapAction);
    if (openMapsBtn) openMapsBtn.addEventListener('click', handleMapAction);
  });
})();
