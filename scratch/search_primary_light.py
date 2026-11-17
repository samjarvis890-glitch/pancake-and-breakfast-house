from pathlib import Path
import re

for css in Path('assets/css').glob('*.css'):
    text = css.read_text(encoding='utf-8')
    matches = re.findall(r'--color-primary-light', text)
    if matches:
        print(f"{css.name}: {len(matches)} occurrences")
