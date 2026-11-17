import re
from pathlib import Path

files = list(Path('.').glob('*.html')) + list(Path('assets/css').glob('*.css'))

for f in files:
    content = f.read_text(encoding='utf-8')
    matches = re.findall(r'minmax\s*\(\s*(\d+px)[^)]*\)', content)
    if matches:
        print(f"{f.name}:")
        for m in matches:
            px = int(re.sub(r'\D', '', m))
            if px > 250:
                print(f"  POTENTIAL MOBILE OVERFLOW: minmax({m}) -> {px}px")
            else:
                print(f"  Safe: minmax({m})")
