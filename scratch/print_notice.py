with open('contact.html', encoding='utf-8') as f:
    text = f.read()

import re
notice = re.search(r'id=["\']contactNotice["\'][\s\S]*?</div>\s*</div>', text)
if notice:
    print(notice.group(0))
