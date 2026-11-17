from pathlib import Path
import re

main_text = Path('assets/css/main.css').read_text(encoding='utf-8')
defined_vars = set(re.findall(r'--([a-zA-Z0-9_-]+):', main_text))

print(f"Total CSS variables defined in main.css: {len(defined_vars)}")

for css in sorted(Path('assets/css').glob('*.css')):
    if any(x in css.name for x in ['bootstrap', 'tailwind', 'fonts']):
        continue
    text = css.read_text(encoding='utf-8')
    used_vars = set(re.findall(r'var\(--([a-zA-Z0-9_-]+)[,)]', text))
    missing = used_vars - defined_vars
    if missing:
        print(f"WARNING: {css.name} uses undefined variables: {missing}")
    else:
        print(f"OK: {css.name} (all {len(used_vars)} variables defined)")
