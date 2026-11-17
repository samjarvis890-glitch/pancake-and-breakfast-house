from pathlib import Path
import re

for css in ['home-2.css', 'menu.css', 'about.css', 'contact.css', 'home.css', 'main.css']:
    text = Path('assets/css/' + css).read_text(encoding='utf-8')
    rtl_matches = re.findall(r'\[dir="rtl"\][^{]*\{[^}]*\}', text)
    print(f"{css}: {len(rtl_matches)} RTL rules found")
    for rm in rtl_matches[:3]:
        print(" ", rm.replace('\n', ' '))
