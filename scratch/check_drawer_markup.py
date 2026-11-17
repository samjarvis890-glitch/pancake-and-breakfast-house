with open('index.html', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('id="mobileDrawer"')
end_pos = text.find('<!-- Mobile Backdrop -->', pos)
print(text[pos:end_pos])
