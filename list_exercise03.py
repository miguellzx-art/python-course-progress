numbers = []

for c in range(0, 5):
    n = int(input("Enter a value: "))
    
    if c == 0 or n > numbers[-1]:
        numbers.append(n)
        print("Added to the end of the list...")
        
    else:
        pos = 0
        while pos < len(numbers):
            if n <= numbers[pos]:
                numbers.insert(pos, n)
                print(f"Added at position {pos}...")
                break
            pos += 1

print("-" * 30)
print(f"Final ordered list: {numbers}")