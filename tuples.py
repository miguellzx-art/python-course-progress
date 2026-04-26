numbers_ext = (
    "zero", "one", "two", "three", "four", "five", 
    "six", "seven", "eight", "nine", "ten", 
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty"
)

while True:
    user_num = int(input("Enter a number between 0 and 20: "))
    
    if 0 <= user_num <= 20:
        print(f"You typed the number {numbers_ext[user_num]}.")
        
        choice = " "
        while choice not in "YN":
            choice = input("Do you want to continue? (Y/N) ").strip().upper()[0]
        
        if choice == "N":
            break
    else:
        print("Try again. ", end="")

print("--- PROGRAM ENDED ---")