import re
from pathlib import Path

pages = ['index.html', 'home-2.html', 'menu.html', 'about.html', 'group-bookings.html', 'contact.html']

print("=== CHECKING SECTION HEADERS IN ALL PAGES ===")
for p in pages:
    content = Path(p).read_text(encoding='utf-8')
    # Find all elements with classes ending in -header or containing section-header
    headers = re.findall(r'<div[^>]*class=["\']([^"\']*(?:section-header|home2-header|menu-header|about-header)[^"\']*)["\'][^>]*>', content)
    print(f"{p}: {len(headers)} section header containers found")
    for h in headers:
        # Check if text-center or similar is in class
        # (or handled via CSS)
        pass

print("\n=== CHECKING BUTTON GROUPS IN HERO & CTA ===")
for p in pages:
    content = Path(p).read_text(encoding='utf-8')
    btn_groups = re.findall(r'<div[^>]*class=["\'][^"\']*(?:btn-group|hero-actions|cta-buttons|actions)[^"\']*["\'][^>]*>', content)
    print(f"{p}: {btn_groups}")

print("\n=== CHECKING MODAL & LIGHTBOX IN ABOUT PAGE ===")
about_content = Path('about.html').read_text(encoding='utf-8')
lightbox = 'lightboxModal' in about_content
print(f"about.html has lightbox modal: {lightbox}")

print("\n=== CHECKING MENU SEARCH & FILTERS IN MENU PAGE ===")
menu_content = Path('menu.html').read_text(encoding='utf-8')
filters = re.findall(r'data-category=["\']([^"\']+)["\']', menu_content)
print(f"menu.html categories: {set(filters)}")

print("\n=== CHECKING GROUP BOOKINGS FORM & CARDS ===")
gb_content = Path('group-bookings.html').read_text(encoding='utf-8')
print(f"group-bookings.html form id: {'tableBookingForm' in gb_content}")

print("\n=== CHECKING CONTACT FORM & CARDS ===")
contact_content = Path('contact.html').read_text(encoding='utf-8')
print(f"contact.html form id: {'restaurantContactForm' in contact_content}")
