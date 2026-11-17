with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
print('Inline scripts in group-bookings.html:', len(scripts))
for i, s in enumerate(scripts):
    if s.strip():
        print(f"Script {i+1}:", s.strip()[:300])

src_scripts = re.findall(r'<script[^>]*src=["\']([^"\']+)["\']', text)
print('External scripts in group-bookings.html:', src_scripts)
