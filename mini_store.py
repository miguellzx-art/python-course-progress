total = tothousand = lower = count = 0
cheapest = ""

while True:
    product = input("Name of product: ")
    price = float(input("Price of product: US$"))
    count += 1
    total += price 
    
    if price > 1000:
        tothousand += 1
        
    if count == 1 or price < lower:
        lower = price 
        cheapest = product
    
    choice = " "
    while choice not in "YN":
        choice = input("Do you want to continue? (Y/N) ").strip().upper()[0]
    if choice == "N":
        break

print(f"{' GAME OVER ':=^30}")
print(f"The total amount spent is US${total:.2f}")
print(f"{tothousand} products cost more than US$1000")
print(f"The cheapest product is {cheapest} which costs US${lower:.2f}")