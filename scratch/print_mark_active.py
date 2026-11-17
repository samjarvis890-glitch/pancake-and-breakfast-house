with open('assets/js/main.js', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('function markActiveNav')
end = text.find('initTheme()', pos)
print(text[pos:end])
