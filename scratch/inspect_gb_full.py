with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

import re
# check total lines and structure
lines = text.splitlines()
print(f"group-bookings.html has {len(lines)} lines")
print("Sections:")
for i, line in enumerate(lines):
    if '<section' in line or '</section>' in line:
        print(f"  Line {i+1}: {line.strip()[:100]}")
