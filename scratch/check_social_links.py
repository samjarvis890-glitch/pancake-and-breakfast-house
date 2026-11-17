from pathlib import Path
import re

text = Path('index.html').read_text(encoding='utf-8')
pos = text.find('class="footer-social-links"')
print(text[pos:pos+600])
