with open('assets/css/home-2.css', encoding='utf-8') as f:
    text = f.read()

import re
for m in re.finditer(r'([^{;}]*(?:#FFF4E6|#FFF9EF|#D1BFAE)[^{;}]*)', text):
    start = max(0, m.start() - 100)
    end = min(len(text), m.end() + 100)
    print("--- MATCH ---")
    print(text[start:end])
