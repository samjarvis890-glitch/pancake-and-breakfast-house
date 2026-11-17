with open('home-2.html', encoding='utf-8') as f:
    text = f.read()

pos = text.find('class="home2-hero-desc"')
print(text[pos:pos+1000])
