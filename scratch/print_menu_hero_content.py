with open('menu.html', encoding='utf-8') as f:
    text = f.read()

pos = text.find('class="menu-hero-content"')
print(text[pos:pos+1500])
