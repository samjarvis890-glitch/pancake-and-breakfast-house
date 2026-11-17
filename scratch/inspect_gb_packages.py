import re

with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

packages = re.search(r'id=["\']packages["\'][\s\S]*?</section>', text)
if packages:
    print("=== PACKAGES SECTION ===")
    print(packages.group(0)[:2500])

faqs = re.search(r'Group Booking FAQs[\s\S]*?</section>', text)
if faqs:
    print("\n=== FAQS SECTION ===")
    print(faqs.group(0)[:2500])
