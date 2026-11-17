with open('assets/css/home-2.css', encoding='utf-8') as f:
    text = f.read()

import re
print("home-2.css grids and columns:")
for m in re.finditer(r'(\.[a-zA-Z0-9_-]*(?:grid|row|cards|columns)[^{]*\{[^}]*\})', text):
    print(m.group(1))
