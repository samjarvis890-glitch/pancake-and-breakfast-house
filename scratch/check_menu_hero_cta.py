with open('assets/css/menu.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.menu-hero-cta[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
