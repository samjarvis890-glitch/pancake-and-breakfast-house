with open('assets/css/contact.css', encoding='utf-8') as f:
    text = f.read()

import re
print("contact.css media queries:")
for m in re.finditer(r'@media[^{]*\{', text):
    print(" ", m.group(0))
