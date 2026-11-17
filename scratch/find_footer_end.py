with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('/* Footer Bottom Bar */')
pos2 = text.find('/* ==========================================================================\n   RESPONSIVE DESIGN', pos)
print(text[pos2-200:pos2+300])
