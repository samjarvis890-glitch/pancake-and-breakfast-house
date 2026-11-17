import re
from pathlib import Path

files = list(Path('.').glob('*.html')) + [f for f in Path('assets/css').glob('*.css') if 'bootstrap' not in f.name and 'tailwind' not in f.name]

for f in files:
    content = f.read_text(encoding='utf-8')
    # search for width: [0-9]+px or min-width: [0-9]+px
    widths = re.findall(r'(?:^|[;{\s])(min-width|width)\s*:\s*(\d+)px', content)
    dangerous = []
    for prop, val in widths:
        ival = int(val)
        if ival >= 320:
            dangerous.append((prop, ival))
    if dangerous:
        print(f"{f.name}: {len(dangerous)} potentially dangerous fixed/min widths:")
        for prop, val in dangerous[:10]:
            print(f"  {prop}: {val}px")
