with open('assets/css/main.css', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f"main.css total lines: {len(lines)}")
print("=== TOP 40 LINES ===")
for l in lines[:40]:
    print(l)
print("\n=== LAST 40 LINES ===")
for l in lines[-40:]:
    print(l)
