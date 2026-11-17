import re
from pathlib import Path

for css_path in Path('assets/css').glob('*.css'):
    if any(x in css_path.name for x in ['bootstrap', 'tailwind', 'fonts']):
        continue
    content = css_path.read_text(encoding='utf-8')
    print(f"\n==================== {css_path.name} ====================")
    
    # Extract dark theme rules
    dark_matches = re.findall(r'(\[data-theme=["\']?dark["\']?\][^{]*\{[^}]*\})', content)
    print(f"Total dark rules: {len(dark_matches)}")
    for dm in dark_matches:
        print("  " + dm.strip().replace('\n', ' '))
