import re
from pathlib import Path

css_files = [f for f in Path('assets/css').glob('*.css') if 'bootstrap' not in f.name and 'tailwind' not in f.name]

header_classes = ['section-header', 'home2-header', 'menu-header', 'about-header', 'section-eyebrow', 'home2-eyebrow', 'menu-eyebrow', 'about-eyebrow', 'section-title', 'section-desc']

for c in css_files:
    text = c.read_text(encoding='utf-8')
    for hc in header_classes:
        for m in re.finditer(rf'(\.{hc}\b[^{{]*\{{[^}}]*\}})', text):
            print(f"[{c.name}] {m.group(1).strip().replace(chr(10), ' ')}")
