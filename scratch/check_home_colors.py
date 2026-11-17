with open('assets/css/home.css', encoding='utf-8') as f:
    text = f.read()

import re
# check for hex colors not using variables
hex_colors = set(re.findall(r'#([0-9a-fA-F]{3,6})\b', text))
print("Hex colors in home.css:", hex_colors)
for hc in hex_colors:
    matches = re.findall(rf'([^{{;}}]*:\s*#[^{{;}}]*{hc}[^{{;}}]*)', text)
    print(f"  #{hc}: {matches[:2]}")
