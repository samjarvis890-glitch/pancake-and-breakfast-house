from pathlib import Path
import re

text = Path('index.html').read_text(encoding='utf-8')
matches = re.findall(r'<a[^>]+href=["\']#["\'][^>]*>([\s\S]*?)</a>', text)
print(f"Found {len(matches)} matches for href='#' in index.html:")
for m in matches:
    print("  ->", m.strip()[:100].replace('\n', ' '))
