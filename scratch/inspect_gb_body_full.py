with open('group-bookings.html', encoding='utf-8') as f:
    text = f.read()

pos1 = text.find('<!-- SECTION 01: RESERVATION BOOKING FORM')
pos2 = text.find('</main>')
print(text[pos1:pos2])
