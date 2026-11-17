with open('assets/css/home-2.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.home2-hero-cta[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
