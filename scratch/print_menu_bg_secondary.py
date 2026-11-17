with open('assets/css/menu.css', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('--color-bg-secondary')
print(text[pos-100:pos+100])
