with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('.newsletter-message')
print(text[pos-50:pos+500])
