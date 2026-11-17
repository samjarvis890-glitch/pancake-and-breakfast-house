with open('assets/css/about.css', encoding='utf-8') as f:
    text = f.read()

import re
items = ['about-story-card', 'about-philosophy-card', 'about-pillar-item', 'about-quote-box', 'about-gallery-item', 'about-lightbox']
for item in items:
    matches = re.findall(rf'(\.{item}[^{{]*\{{[^}}]*\}})', text)
    print(f"=== {item} ===")
    for m in matches[:2]:
        print(" ", m.replace('\n', ' '))
