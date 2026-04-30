matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(3):
    for col in range(3):
        matrix[row][col] = int(input(f"Enter a value to [{row} {col}]"))
print("-=" * 30)
for row in range(0, 3):
    for col in range(0, 3):
        print(f"[{matrix[row][col]:^5}]", end="")
    print()