with open('assets/css/home-2.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'(\.(?:home2-taste-section|home2-taste-card|home2-inside-section|home2-moments-section|home2-moment-card|home2-slow-section)[^{]*\{[^}]*\})', text)
for m in matches:
    print(m)
