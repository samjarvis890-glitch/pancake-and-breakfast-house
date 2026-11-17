with open('assets/css/menu.css', encoding='utf-8') as f:
    text = f.read()

import re
items = ['menu-card', 'menu-diet-pill', 'menu-price-tag', 'menu-beyond-card', 'menu-split-card', 'menu-note-card']
for item in items:
    matches = re.findall(rf'(\.{item}[^{{]*\{{[^}}]*\}})', text)
    print(f"=== {item} ===")
    for m in matches[:2]:
        print(" ", m.replace('\n', ' '))
