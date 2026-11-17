with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

new_main_content = """    <!-- SECTION 01: RESERVATION BOOKING FORM (#booking) -->
    <section class="pb-section" id="booking" style="background-color: var(--color-bg-card);">
      <div class="container-narrow">
        <div class="section-header">
          <span class="section-eyebrow">Online Reservation</span>
          <h2 class="section-title">Reserve Your Table</h2>
          <p class="section-desc">Fill out your details below and our morning concierge will confirm your reservation promptly.</p>
        </div>

        <div class="booking-form-card">
          <form id="tableBookingForm" novalidate>
            <div class="booking-form-grid">
              <div>
                <label for="bookName" class="form-label">Full Name <span class="required-star">*</span></label>
                <input type="text" id="bookName" class="form-control-pb" required placeholder="e.g. Eleanor Vance" autocomplete="name">
              </div>
              <div>
                <label for="bookEmail" class="form-label">Email Address <span class="required-star">*</span></label>
                <input type="email" id="bookEmail" class="form-control-pb" required placeholder="e.g. eleanor@example.com" autocomplete="email">
              </div>
            </div>

            <div class="booking-form-grid">
              <div>
                <label for="bookPhone" class="form-label">Phone Number <span class="required-star">*</span></label>
                <input type="tel" id="bookPhone" class="form-control-pb" required placeholder="(555) 000-0000" autocomplete="tel">
              </div>
              <div>
                <label for="bookGuests" class="form-label">Party Size / Guests <span class="required-star">*</span></label>
                <select id="bookGuests" class="form-control-pb" required>
                  <option value="2">Table for 2 Guests</option>
                  <option value="4" selected>Table for 3 to 4 Guests</option>
                  <option value="6">Table for 5 to 6 Guests</option>
                  <option value="8">Table for 7 to 8 Guests</option>
                  <option value="12">Group Table: 9 to 12 Guests</option>
                  <option value="20">Large Party: 13 to 20 Guests</option>
                  <option value="40">Private Mezzanine: 21 to 40 Guests</option>
                </select>
              </div>
            </div>

            <div class="booking-form-grid">
              <div>
                <label for="bookDate" class="form-label">Preferred Date <span class="required-star">*</span></label>
                <input type="date" id="bookDate" class="form-control-pb" required>
              </div>
              <div>
                <label for="bookTime" class="form-label">Time Slot <span class="required-star">*</span></label>
                <select id="bookTime" class="form-control-pb" required>
                  <option value="07:30">7:30 AM (Early Bird)</option>
                  <option value="08:30">8:30 AM (Sunrise Rush)</option>
                  <option value="09:30">9:30 AM (Peak Morning)</option>
                  <option value="10:30" selected>10:30 AM (Brunch Hour)</option>
                  <option value="11:30">11:30 AM (Late Morning)</option>
                  <option value="12:30">12:30 PM (Midday Table)</option>
                  <option value="13:30">1:30 PM (Afternoon Wind-down)</option>
                </select>
              </div>
            </div>

            <div style="margin-bottom: 1.5rem;">
              <label for="bookOccasion" class="form-label">Occasion / Reason</label>
              <select id="bookOccasion" class="form-control-pb">
                <option value="casual" selected>Casual Morning Catch-up</option>
                <option value="birthday">Birthday Celebration</option>
                <option value="family">Family Gathering</option>
                <option value="anniversary">Anniversary or Milestone</option>
                <option value="corporate">Team Breakfast / Meeting</option>
                <option value="other">Other Special Moment</option>
              </select>
            </div>

            <div style="margin-bottom: 2rem;">
              <label for="bookNotes" class="form-label">Dietary Preferences or Special Requests</label>
              <textarea id="bookNotes" class="form-control-pb" rows="3" placeholder="e.g. 2 guests require gluten-free pancakes, high chair needed for toddler, birthday candles requested."></textarea>
            </div>

            <button type="submit" class="btn-pb btn-pb-primary" style="width: 100%; justify-content: center; padding: 1rem 2rem;">
              <span>Confirm Table Reservation Request</span>
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" width="18" height="18"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </button>

            <div class="newsletter-message" id="bookingMsg" role="status" aria-live="polite"></div>
          </form>
        </div>
      </div>
    </section>

    <!-- SECTION 02: CELEBRATION MORNING PACKAGES (#packages) -->
    <section class="pb-section" id="packages">
      <div class="container-narrow">
        <div class="section-header">
          <span class="section-eyebrow">Curated For Groups</span>
          <h2 class="section-title">Celebration Morning Packages</h2>
          <p class="section-desc">Designed to make hosting effortless with family-style platters, continuous coffee and warm hospitality.</p>
        </div>

        <div class="booking-packages-grid">
          <!-- Package 1 -->
          <div class="booking-package-card">
            <span class="booking-package-tag">Family &amp; Kids</span>
            <h3 class="booking-package-title">The Pancake Party Stack</h3>
            <div class="booking-package-price">$24 <small>/ guest</small></div>
            <p class="booking-package-desc">
              Mini pancake flights with chocolate chips, wild berries and sprinkles, warm syrup carafes, fresh orange juice pitchers, and festive candles for the birthday star.
            </p>
            <ul class="booking-package-features">
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Unlimited mini buttermilk pancakes</span>
              </li>
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Fruit, Nutella and sprinkles bar</span>
              </li>
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Fresh squeezed orange juice</span>
              </li>
            </ul>
            <a href="#booking" class="btn-pb btn-pb-secondary booking-package-btn">Select This Package</a>
          </div>

          <!-- Package 2: Featured -->
          <div class="booking-package-card is-popular">
            <div class="booking-popular-badge">Most Popular Choice</div>
            <span class="booking-package-tag">Celebrations &amp; Birthdays</span>
            <h3 class="booking-package-title">The Grand Morning Feast</h3>
            <div class="booking-package-price">$32 <small>/ guest</small></div>
            <p class="booking-package-desc">
              Platters of fluffy golden buttermilk stacks, crisp Liege waffles, farm scrambles, applewood smoked bacon, avocado tartines, and bottomless specialty coffees.
            </p>
            <ul class="booking-package-features">
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Full sweet &amp; savoury breakfast spreads</span>
              </li>
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Continuous artisanal drip and tea</span>
              </li>
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Reserved prime seating for 2.5 hours</span>
              </li>
            </ul>
            <a href="#booking" class="btn-pb btn-pb-primary booking-package-btn">Select This Package</a>
          </div>

          <!-- Package 3 -->
          <div class="booking-package-card">
            <span class="booking-package-tag">Corporate &amp; Teams</span>
            <h3 class="booking-package-title">The Morning Executive</h3>
            <div class="booking-package-price">$28 <small>/ guest</small></div>
            <p class="booking-package-desc">
              Individual breakfast bowls, warm breakfast sandwiches on house brioche, fresh pastries, fruit cups, and handcrafted espresso drinks in our private mezzanine.
            </p>
            <ul class="booking-package-features">
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Quiet mezzanine space with fast Wi-Fi</span>
              </li>
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Individual gourmet plated options</span>
              </li>
              <li>
                <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M5 13l4 4L19 7"></path></svg>
                <span>Handcrafted espresso bar included</span>
              </li>
            </ul>
            <a href="#booking" class="btn-pb btn-pb-secondary booking-package-btn">Select This Package</a>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 03: FAQ -->
    <section class="pb-section" style="background-color: var(--color-bg-card);">
      <div class="container-narrow">
        <div class="section-header">
          <span class="section-eyebrow">Common Questions</span>
          <h2 class="section-title">Group Booking FAQs</h2>
          <p class="section-desc">Everything you need to know about celebrating your morning moments with us.</p>
        </div>

        <div class="booking-faq-list">
          <div class="booking-faq-item">
            <h3 class="booking-faq-q">How far in advance should we reserve?</h3>
            <p class="booking-faq-a">
              For weekend tables of 6 or more, we recommend booking 3 to 7 days ahead. For weekday mornings, 24 to 48 hours notice is usually plenty.
            </p>
          </div>

          <div class="booking-faq-item">
            <h3 class="booking-faq-q">Can you accommodate gluten-free or vegan diets?</h3>
            <p class="booking-faq-a">
              Yes! We have dedicated gluten-free pancake and waffle batter, almond/oat milks, and plant-based breakfast scrambles. Just note your preferences when booking.
            </p>
          </div>

          <div class="booking-faq-item">
            <h3 class="booking-faq-q">Can we bring our own birthday cake or decorations?</h3>
            <p class="booking-faq-a">
              You are very welcome to bring table decorations and balloons. You may also bring a birthday cake; we provide cake cutting, plates and candles with no cakeage fee!
            </p>
          </div>
        </div>
      </div>
    </section>
  """

pos1 = text.find('<!-- SECTION 01: RESERVATION BOOKING FORM')
pos2 = text.find('</main>')

updated_text = text[:pos1] + new_main_content + text[pos2:]

with open('group-bookings.html', 'w', encoding='utf-8') as f:
    f.write(updated_text)

print("group-bookings.html updated successfully!")
