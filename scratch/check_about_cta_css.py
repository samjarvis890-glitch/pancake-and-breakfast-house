with open('assets/css/about.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.about-hero-cta[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
