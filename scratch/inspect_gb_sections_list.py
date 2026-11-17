with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

import re
print("group-bookings.html main content:")
m = re.search(r'<main id="mainContent">([\s\S]*?)</main>', text)
if m:
    print(f"Main length: {len(m.group(1))} characters")
    sections = re.findall(r'<section[^>]*id=["\']?([^"\'\s>]+)?["\']?[^>]*>', m.group(1))
    print(f"Found sections: {sections}")
