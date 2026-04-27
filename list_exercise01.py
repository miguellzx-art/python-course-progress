values = []


for i in range(0, 5):
    values.append(int(input(f"Enter a value for position {i}: ")))

highest = max(values)
lowest = min(values)

print("-" * 30)
print(f"You entered the values: {values}")
print(f"The highest value was {highest} at positions: ", end="")

for i, v in enumerate(values):
    if v == highest:
        print(f"{i}... ", end="")

print(f"\nThe lowest value was {lowest} at positions: ", end="")
for i, v in enumerate(values):
    if v == lowest:
        print(f"{i}... ", end="")