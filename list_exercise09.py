numbers = []

print("Enter 5 numbers:\n")

for i in range(5):
    while True:
        try:
            num = float(input(f"Enter the {i+1}º number: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input! Please enter only numbers.")

inverted_numbers = numbers[::-1]

print("\n" + "="*40)
print("Original list :", numbers)
print("Inverted list :", inverted_numbers)
print("="*40)