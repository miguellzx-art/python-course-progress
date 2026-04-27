numbers = []

while True:
    n = int(input("Enter a value: "))
    
    if n not in numbers:
        numbers.append(n)
        print("Value added successfully!")
    else:
        print("Duplicate value! I will not add it.")
    
    choice = " "
    while choice not in "YN":
        choice = input("Do you want to continue? [Y/N] ").strip().upper()[0]
    
    if choice == "N":
        break

print("-" * 30)
numbers.sort()
print(f"You entered the unique values: {numbers}")