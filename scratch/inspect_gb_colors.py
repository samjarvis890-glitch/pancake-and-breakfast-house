with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

import re

# check for any hardcoded colors like #fff, #2D211C, etc. that might be in inline styles
inline_colors = re.findall(r'style=["\'][^"\']*(?:color|background|border):[^"\']*["\']', text)
print(f"Inline styles with color/background/border: {len(inline_colors)}")
for ic in inline_colors[:15]:
    print("  ", ic)
