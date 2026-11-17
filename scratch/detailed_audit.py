import re
from pathlib import Path
from html.parser import HTMLParser

html_files = sorted(list(Path('.').glob('*.html')))
css_files = sorted(list(Path('assets/css').glob('*.css')))

print("=== CHECKING CSS FILES FOR DARK MODE RULES ===")
for c in css_files:
    if 'bootstrap' in c.name or 'tailwind' in c.name or 'fonts' in c.name:
        continue
    content = c.read_text(encoding='utf-8')
    dark_count = len(re.findall(r'\[data-theme=["\']?dark["\']?\]', content))
    print(f"{c.name}: {dark_count} dark mode rules found, size={len(content)} chars")

print("\n=== CHECKING HTML FILES FOR INLINE STYLES AND CLASSES ===")
for f in html_files:
    content = f.read_text(encoding='utf-8')
    bg_whites = len(re.findall(r'class=["\'][^"\']*\bbg-white\b[^"\']*["\']', content))
    text_darks = len(re.findall(r'class=["\'][^"\']*\btext-dark\b[^"\']*["\']', content))
    text_blacks = len(re.findall(r'class=["\'][^"\']*\btext-black\b[^"\']*["\']', content))
    bg_lights = len(re.findall(r'class=["\'][^"\']*\bbg-light\b[^"\']*["\']', content))
    
    inline_styles = re.findall(r'style=["\']([^"\']+)["\']', content)
    suspicious_inline = [s for s in inline_styles if any(k in s for k in ['color:', 'background:', 'background-color:'])]
    
    inputs = re.findall(r'<(input|select|textarea)\b([^>]*)>', content, re.IGNORECASE)
    
    print(f"\n--- {f.name} ---")
    print(f"  bg-white: {bg_whites}, text-dark: {text_darks}, text-black: {text_blacks}, bg-light: {bg_lights}")
    print(f"  Suspicious inline color/bg styles: {len(suspicious_inline)}")
    if suspicious_inline:
        for s in suspicious_inline[:3]:
            print(f"    - {s}")
    print(f"  Form controls: {len(inputs)}")
