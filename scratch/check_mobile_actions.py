import re
from pathlib import Path

html_files = sorted(list(Path('.').glob('*.html')))
for hf in html_files:
    text = hf.read_text(encoding='utf-8')
    m = re.search(r'<div class="navbar-actions-mobile"[^>]*>([\s\S]*?)</div>\s*</div>\s*</header>', text)
    if m:
        content = m.group(1).strip()
        has_dark = 'themeToggleBtnMobile' in content or 'theme' in content.lower()
        has_rtl = 'rtlToggleBtnMobile' in content or 'rtl' in content.lower()
        has_hamb = 'hamburgerBtn' in content or 'hamburger' in content.lower()
        print(f"{hf.name}: Dark={has_dark}, RTL={has_rtl}, Hamb={has_hamb}")
    else:
        print(f"{hf.name}: NO navbar-actions-mobile found!")
