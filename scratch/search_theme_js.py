with open('assets/js/main.js', encoding='utf-8') as f:
    text = f.read()

import re
print("Theme occurrences in main.js:")
for m in re.finditer(r'.{0,40}theme.{0,60}', text, re.IGNORECASE):
    print(m.group(0).strip())
