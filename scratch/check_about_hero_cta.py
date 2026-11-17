with open('about.html', encoding='utf-8') as f:
    text = f.read()

pos = text.find('class="about-hero-cta"')
if pos != -1:
    print(text[pos-100:pos+500])
else:
    pos2 = text.find('class="about-hero')
    print(text[pos2:pos2+1000])
