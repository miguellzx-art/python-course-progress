positives = []
negatives = []
evens = []
odds = []

for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num >= 0:
        positives.append(num)
    else:
        negatives.append(num)
    if num % 2 == 0:
        evens.append(num)
    else:
        odds.append(num)

positives.sort() 
evens.sort()
negatives.sort(reverse=True)
odds.sort(reverse=True)
print("\n" + "="*30)
print(f"Positives (Ascending): {positives}")
print(f"Evens (Ascending):     {evens}")
print(f"Negatives (Descending): {negatives}")
print(f"Odds (Descending):      {odds}")
print("="*30)