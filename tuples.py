numbers_ext = (
    "zero", "one", "two", "three", "four", "five", 
    "six", "seven", "eight", "nine", "ten", 
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty")

while True:
    user_num = int(input("Enter a number between 0 and 20: "))
    
    if 0 <= user_num <= 20:
        break
    
    print("Try again. ", end="")

print(f"You typed the number {numbers_ext[user_num]}.")