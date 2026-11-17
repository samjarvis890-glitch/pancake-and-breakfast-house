import re

with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'@media\s*\(\s*max-width:\s*1280px\s*\)\s*\{([\s\S]*?\n\})', text)
if m:
    print(m.group(0)[:1500])
