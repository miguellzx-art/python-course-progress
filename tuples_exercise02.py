from random import randint

numbers = (randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5))

print("Generated numbers: ", end="")

for n in numbers:
    print(f"{n} ", end="")

print(f"\nHigh: {max(numbers)}")
print(f"Low: {min(numbers)}")