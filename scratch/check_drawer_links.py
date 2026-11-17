import re
from pathlib import Path

html_files = sorted(list(Path('.').glob('*.html')))
for hf in html_files:
    text = hf.read_text(encoding='utf-8')
    m = re.search(r'<div class="mobile-drawer"[^>]*>([\s\S]*?)</div>\s*<!-- Main Content', text)
    if not m:
        m = re.search(r'<div class="mobile-drawer"[^>]*>([\s\S]*?)</div>\s*<main', text)
    if m:
        content = m.group(1).strip()
        links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', content)
        print(f"\n{hf.name} - Drawer links ({len(links)}):")
        for href, label in links:
            clean_lbl = re.sub(r'<[^>]+>', '', label).strip()
            print(f"  {clean_lbl:20} -> {href}")
    else:
        print(f"\n{hf.name} - NO drawer found!")
