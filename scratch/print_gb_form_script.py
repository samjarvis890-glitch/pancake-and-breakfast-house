with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', text, re.DOTALL)
for s in scripts:
    if 'tableBookingForm' in s:
        print(s)
