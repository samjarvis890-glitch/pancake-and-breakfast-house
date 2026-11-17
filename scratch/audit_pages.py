import re
from pathlib import Path

html_files = list(Path('.').glob('*.html'))
print(f"Found {len(html_files)} HTML files:")
for f in html_files:
    content = f.read_text(encoding='utf-8')
    css_links = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', content)
    print(f"\n--- {f.name} ---")
    for link in css_links:
        href = re.search(r'href=["\']([^"\']+)["\']', link)
        if href:
            print(f"  CSS: {href.group(1)}")
