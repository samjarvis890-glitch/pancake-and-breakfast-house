with open('home-2.html', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<section[^>]*class=["\']([^"\']*)["\']', text)
print("Sections in home-2.html:", matches)
pos = text.find('<section')
print(text[pos:pos+1200])
