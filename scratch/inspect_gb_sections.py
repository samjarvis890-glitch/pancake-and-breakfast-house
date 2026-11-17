import re

with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

# Let's inspect each section
sections = re.findall(r'(<section[\s\S]*?</section>)', text)
print(f"Total sections: {len(sections)}")
for i, s in enumerate(sections):
    tag = re.search(r'<section([^>]*)>', s)
    h2 = re.search(r'<h[12][^>]*>(.*?)</h[12]>', s)
    print(f"Section {i+1}: {tag.group(1) if tag else ''} | Title: {h2.group(1) if h2 else 'No title'}")
