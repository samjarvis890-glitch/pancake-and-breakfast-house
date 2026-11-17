with open('assets/js/main.js', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function markActiveNav[\s\S]*?\}', text)
if m:
    print(m.group(0))
