with open('assets/js/main.js', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('function applyTheme')
print(text[pos:pos+1200])
