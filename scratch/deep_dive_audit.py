import re
from pathlib import Path

html_files = ['index.html', 'home-2.html', 'menu.html', 'about.html', 'group-bookings.html', 'contact.html']

print("==================================================")
print("AUDITING HTML FILES FOR ALIGNMENT & CONTRAST ISSUES")
print("==================================================")

for filename in html_files:
    content = Path(filename).read_text(encoding='utf-8')
    print(f"\n--- {filename} ---")
    
    # Check Section headers alignment
    # Check if any section headers have un-centered text or strange inline styles
    section_headers = re.findall(r'<div[^>]*class=["\'][^"\']*(?:section-header|home2-header|menu-header|about-header)[^"\']*["\'][^>]*>([\s\S]*?)</div>', content)
    print(f"Section headers count: {len(section_headers)}")
    for sh in section_headers:
        eyebrow = re.search(r'<span[^>]*class=["\'][^"\']*(?:eyebrow)[^"\']*["\'][^>]*>(.*?)</span>', sh)
        title = re.search(r'<h[1-6][^>]*>(.*?)</h[1-6]>', sh)
        desc = re.search(r'<p[^>]*class=["\'][^"\']*(?:desc|subtitle)[^"\']*["\'][^>]*>(.*?)</p>', sh)
        title_str = re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else 'No title'
        eyebrow_str = re.sub(r'<[^>]+>', '', eyebrow.group(1)).strip() if eyebrow else 'No eyebrow'
        print(f"  Header: [{eyebrow_str}] -> '{title_str}'")

    # Check images for alt text and loading
    images = re.findall(r'<img\b([^>]*)>', content)
    images_without_alt = [img for img in images if 'alt=' not in img]
    print(f"Images count: {len(images)}, missing alt: {len(images_without_alt)}")
    
    # Check for hardcoded color styles that might break dark mode
    hardcoded_styles = re.findall(r'style=["\'][^"\']*(?:color:\s*(?:#[0-9a-fA-F]{3,6}|rgb|black|white)|background(?:-color)?:\s*(?:#[0-9a-fA-F]{3,6}|rgb|black|white))[^"\']*["\']', content)
    print(f"Hardcoded color styles: {len(hardcoded_styles)}")
    if hardcoded_styles:
        for hs in hardcoded_styles[:5]:
            print(f"    Style: {hs}")
