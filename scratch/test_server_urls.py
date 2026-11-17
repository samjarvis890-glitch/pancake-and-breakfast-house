import urllib.request

base_url = "http://127.0.0.1:5500/"
pages = ['index.html', 'home-2.html', 'menu.html', 'about.html', 'group-bookings.html', 'contact.html']

for page in pages:
    url = base_url + page
    try:
        req = urllib.request.urlopen(url, timeout=5)
        status = req.getcode()
        length = len(req.read())
        print(f"HTTP {status} OK: {url} ({length} bytes)")
    except Exception as e:
        print(f"HTTP ERROR on {url}: {e}")
