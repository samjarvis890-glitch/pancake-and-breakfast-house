import re

with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

# Find all form controls and their labels
inputs = re.findall(r'<label[^>]*>(.*?)</label>[\s\S]*?<(input|select|textarea)[^>]*class=["\']([^"\']*)["\']', text)
print(f"Found {len(inputs)} form controls with labels in group-bookings.html:")
for lbl, tag, cls in inputs:
    lbl_clean = re.sub(r'<[^>]+>', '', lbl).strip()
    print(f"  [{tag}] {lbl_clean} -> class='{cls}'")

# Check CSS classes used in group-bookings.html
classes = set(re.findall(r'class=["\']([^"\']+)["\']', text))
all_classes = set()
for c in classes:
    for item in c.split():
        all_classes.add(item)
print(f"\nUnique classes in group-bookings.html: {len(all_classes)}")
