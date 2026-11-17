with open('home-2.html', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('<!-- SECTION 01: HERO')
print(text[pos:pos+1500])
