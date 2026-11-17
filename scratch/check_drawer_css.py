with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.drawer-toggle[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
matches2 = re.findall(r'(\.mobile-drawer-toggles[^{]*\{[^}]*\})', text)
for m in matches2:
    print(m)
