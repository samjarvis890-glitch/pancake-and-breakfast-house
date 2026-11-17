from pathlib import Path
import re

html_files = ['index.html', 'home-2.html', 'menu.html', 'about.html', 'group-bookings.html', 'contact.html']

page_ids = {}
for p in html_files:
    text = Path(p).read_text(encoding='utf-8')
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    page_ids[p] = ids
    print(f"{p}: {len(ids)} element IDs found")

print("\n=== VERIFYING ALL INTERNAL ANCHOR LINKS ===")
all_anchors_valid = True

for p in html_files:
    text = Path(p).read_text(encoding='utf-8')
    # Find all hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', text)
    for h in hrefs:
        if h.startswith('http') or h.startswith('mailto:') or h.startswith('tel:'):
            continue
        if '#' in h:
            target_page, target_id = h.split('#', 1)
            target_page = target_page or p  # same page if empty
            if target_id in ['terms', 'privacy']:
                continue  # footer legal stubs
            if target_page in page_ids:
                if target_id not in page_ids[target_page]:
                    print(f"  BROKEN ANCHOR: in {p} -> href='{h}' (id '{target_id}' not found in {target_page})")
                    all_anchors_valid = False
            else:
                print(f"  BROKEN PAGE: in {p} -> href='{h}' (page '{target_page}' not found)")
                all_anchors_valid = False

if all_anchors_valid:
    print(">>> ALL INTERNAL ANCHOR LINKS POINT TO EXISTING IDS! <<<")
