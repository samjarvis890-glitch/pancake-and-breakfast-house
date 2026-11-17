with open('assets/js/main.js', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('function initTheme')
end = text.find('function initDirection', pos)
print(text[pos:end])
