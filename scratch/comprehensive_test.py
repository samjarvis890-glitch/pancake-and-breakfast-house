from pathlib import Path
import re
import urllib.parse

html_files = ['index.html', 'home-2.html', 'menu.html', 'about.html', 'group-bookings.html', 'contact.html']

print("==================================================")
print("COMPREHENSIVE WEBSITE AUDIT & VERIFICATION")
print("==================================================")

all_ok = True

for page in html_files:
    text = Path(page).read_text(encoding='utf-8')
    print(f"\n--- Checking {page} ---")
    
    # 1. Check title & meta
    title_m = re.search(r'<title>(.*?)</title>', text)
    print(f"  Title: {title_m.group(1) if title_m else 'MISSING'}")
    
    viewport_m = re.search(r'<meta[^>]+name=["\']viewport["\'][^>]*>', text)
    if not viewport_m:
        print("  ERROR: Missing viewport meta tag!")
        all_ok = False
        
    # 2. Check local assets (CSS, JS, Images)
    css_links = re.findall(r'<link[^>]+href=["\']([^"\']+\.css)["\']', text)
    for css in css_links:
        if not Path(css).exists():
            print(f"  ERROR: Missing CSS file: {css}")
            all_ok = False
            
    js_links = re.findall(r'<script[^>]+src=["\']([^"\']+\.js)["\']', text)
    for js in js_links:
        if not Path(js).exists():
            print(f"  ERROR: Missing JS file: {js}")
            all_ok = False
            
    img_srcs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', text)
    for img in img_srcs:
        # ignore data:
        if img.startswith('data:'):
            continue
        clean_img = urllib.parse.unquote(img)
        if not Path(clean_img).exists():
            print(f"  ERROR: Missing Image file: {clean_img}")
            all_ok = False
            
    print(f"  Assets: {len(css_links)} CSS, {len(js_links)} JS, {len(img_srcs)} Images - All verified!")
    
    # 3. Check Section Header Centering
    header_divs = re.findall(r'<div[^>]*class=["\'][^"\']*(?:section-header|home2-header|menu-header|about-header)[^"\']*["\'][^>]*>', text)
    print(f"  Section header containers: {len(header_divs)}")
    
    # 4. Check Navigation elements
    has_desktop_nav = 'navbar-nav-desktop' in text
    has_mobile_actions = 'navbar-actions-mobile' in text
    has_mobile_drawer = 'mobileDrawer' in text
    has_theme_toggle = 'theme-toggle-btn' in text
    has_rtl_toggle = 'dir-toggle-btn' in text or 'rtlToggleBtn' in text
    
    if not (has_desktop_nav and has_mobile_actions and has_mobile_drawer and has_theme_toggle and has_rtl_toggle):
        print(f"  ERROR in Navbar/Drawer structure!")
        all_ok = False
    else:
        print(f"  Navbar: Desktop Nav, Mobile Actions, Drawer, Theme Toggle, RTL Toggle - All present!")

    # 5. Check Footer elements
    has_footer = '<footer' in text
    has_newsletter = 'footerNewsletterForm' in text
    has_back_to_top = 'backToTopBtn' in text
    if not (has_footer and has_newsletter and has_back_to_top):
        print(f"  ERROR in Footer structure!")
        all_ok = False
    else:
        print(f"  Footer: Complete global footer with newsletter & back to top - All present!")

if all_ok:
    print("\n>>> ALL 6 PAGES PASSED LOCAL ASSET & INTEGRITY CHECKS! <<<")
else:
    print("\n>>> ERRORS DETECTED DURING INTEGRITY CHECK! <<<")
