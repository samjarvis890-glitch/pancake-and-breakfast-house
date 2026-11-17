with open('assets/css/contact.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'@media\s*\(\s*max-width:\s*575px\s*\)\s*\{([\s\S]*?\n\})', text)
for i, m in enumerate(matches):
    print(f"--- 575px block {i+1} ---")
    print(m)
