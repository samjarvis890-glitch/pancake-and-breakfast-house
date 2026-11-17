with open('assets/css/about.css', encoding='utf-8') as f:
    text = f.read()

import re
print("about.css grids and columns:")
for m in re.finditer(r'(\.[a-zA-Z0-9_-]*(?:grid|row|cards|columns)[^{]*\{[^}]*\})', text):
    print(m.group(1))
