from pathlib import Path

menu_text = Path('menu.html').read_text(encoding='utf-8')
menu_anchors = ['pancakes', 'waffles', 'breakfast-plates', 'eggs-toast', 'coffee-drinks', 'sweet-treats']
print("=== MENU ANCHORS ===")
for a in menu_anchors:
    found = f'id="{a}"' in menu_text or f"id='{a}'" in menu_text
    print(f"  #{a} -> {'FOUND' if found else 'MISSING!'}")

about_text = Path('about.html').read_text(encoding='utf-8')
about_anchors = ['our-story', 'our-restaurant', 'food-philosophy', 'gallery']
print("\n=== ABOUT ANCHORS ===")
for a in about_anchors:
    found = f'id="{a}"' in about_text or f"id='{a}'" in about_text
    print(f"  #{a} -> {'FOUND' if found else 'MISSING!'}")

gb_text = Path('group-bookings.html').read_text(encoding='utf-8')
gb_anchors = ['booking', 'packages']
print("\n=== GROUP BOOKINGS ANCHORS ===")
for a in gb_anchors:
    found = f'id="{a}"' in gb_text or f"id='{a}'" in gb_text
    print(f"  #{a} -> {'FOUND' if found else 'MISSING!'}")
