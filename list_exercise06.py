numbers = list()
evens = list()
odds = list()

for n in range(0, 7):
     num = int(input("Enter a number: "))
     numbers.append(num)
     if num % 2 == 0:
          evens.append(num)
     if num % 2 == 1:
          odds.append(num)

numbers.sort()
evens.sort()
odds.sort()

print(f"We have {odds} odd numbers.")
print(f"We have {evens} even numbers.")
print(f"In ascending order, it looks like this: \n{numbers}")