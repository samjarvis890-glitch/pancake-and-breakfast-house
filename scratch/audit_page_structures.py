import re
from pathlib import Path

html_files = ['index.html', 'home-2.html', 'menu.html', 'about.html', 'group-bookings.html', 'contact.html']

for hf in html_files:
    text = Path(hf).read_text(encoding='utf-8')
    print(f"\n============================== {hf} ==============================")
    
    # 1. Check section headers
    # Find all h1, h2, h3 and section header divs
    headers = re.findall(r'<div[^>]*class=["\'][^"\']*(?:section-header|home2-header|menu-header|about-header)[^"\']*["\'][^>]*>', text)
    print(f"Section header containers: {len(headers)}")
    
    # Check all h2 tags
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', text, re.DOTALL)
    print(f"H2 headings ({len(h2s)}):")
    for h in h2s:
        clean_h = re.sub(r'<[^>]+>', '', h).strip()
        print(f"  - {clean_h[:60]}")
        
    # Check forms
    forms = re.findall(r'<form[^>]*id=["\']([^"\']+)["\']', text)
    if forms:
        print(f"Forms: {forms}")
        
    # Check buttons
    btns = re.findall(r'<a[^>]*class=["\'][^"\']*btn-[^"\']*["\']|<button[^>]*class=["\'][^"\']*btn-[^"\']*["\']', text)
    print(f"Buttons with btn-* class: {len(btns)}")
