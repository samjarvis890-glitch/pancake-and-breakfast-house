with open('assets/css/menu.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'@media[^{]*\{([\s\S]*?\n\})', text)
for i, m in enumerate(matches):
    print(f"--- MQ block {i+1} ---")
    print(m[:300])
