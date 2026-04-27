inventory = (
    "Pencil", 1.75,
    "Eraser", 2.00,
    "Notebook", 15.90,
    "Pencil Case", 25.00,
    "Protractor", 4.20,
    "Compass", 9.99,
    "Backpack", 120.00,
    "Pens", 22.30,
    "Book", 34.90)

print("-" * 40)
print(f"{'PRICE LIST':^40}")
print("-" * 40)

for pos in range(0, len(inventory)):
    if pos % 2 == 0:
        print(f"{inventory[pos]:.<30}", end="")
    else:
        print(f"US${inventory[pos]:>7.2f}")

print("-" * 40)