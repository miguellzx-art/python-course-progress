numbers = list()
even_numbers = list()
odd_numbers = list()

while True:
    numbers.append(int(input("Enter a number: ")))
    response = str(input("Would you like to continue? [Y/N] "))
    if response in "Nn":
        break

for index, value in enumerate(numbers):
    if value % 2 == 0:
        even_numbers.append(value)
    elif value % 2 == 1:
        odd_numbers.append(value)

print("-=" * 30)
print(f"The complete list is {numbers}")
print(f"The list of even numbers is {even_numbers}")
print(f"The list of odd numbers is {odd_numbers}")