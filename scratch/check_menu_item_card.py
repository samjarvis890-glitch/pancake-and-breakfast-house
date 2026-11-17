with open('assets/css/menu.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.menu-item-card[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
matches2 = re.findall(r'(\.menu-item-category-badge[^{]*\{[^}]*\})', text)
for m in matches2:
    print(m)
