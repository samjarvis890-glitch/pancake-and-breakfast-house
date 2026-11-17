with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

pos = text.find('RESPONSIVE NAVIGATION BREAKPOINTS')
print(text[pos-250:pos+100])
