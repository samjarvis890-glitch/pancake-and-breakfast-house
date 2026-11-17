with open('menu.html', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'class=["\']([^"\']*(?:item|card)[^"\']*)["\']', text)
print("Unique item/card classes in menu.html:", set(matches[:20]))
pos = text.find('class="menu-interactive-grid"')
print(text[pos:pos+1200])
