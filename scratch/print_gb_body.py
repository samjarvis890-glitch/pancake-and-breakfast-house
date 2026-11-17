with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

import re
pos_start = text.find('<!-- SECTION 01: RESERVATION BOOKING FORM')
pos_end = text.find('<!-- ==========================================================================\n       GLOBAL FOOTER', pos_start)
print(text[pos_start:pos_end])
