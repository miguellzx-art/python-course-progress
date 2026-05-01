matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_evens = max_value = sum_column = 0

for row in range(3):
    for col in range(3):
        matrix[row][col] = int(input(f"Enter a value for [{row}, {col}]: "))

print("-=" * 30)
for row in range(0, 3):
    for col in range(0, 3):
        print(f"[{matrix[row][col]:^5}]", end="")
        if matrix[row][col] % 2 == 0:
            sum_evens += matrix[row][col]
    print()

print("-=" * 30)
print(f"The sum of even values is {sum_evens}.")

for row in range(0, 3):
    sum_column += matrix[row][2]

print(f"The sum of the values in the third column is {sum_column}.")

for col in range(0, 3):
    if col == 0:
        max_value = matrix[1][col]
    elif matrix[1][col] > max_value:
        max_value = matrix[1][col]

print(f"The highest value in the second row is {max_value}.")