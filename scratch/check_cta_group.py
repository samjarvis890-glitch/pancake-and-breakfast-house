with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.cta-group[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
