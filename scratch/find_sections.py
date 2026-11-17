with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'/\* ==+[\s\S]*?==+ \*/', text)
for m in matches[-10:]:
    print(m)
