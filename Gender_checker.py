gender = ""

while gender != "m" and gender != "f":
    gender = input("Enter your gender, 'm' for male and 'f' for female: ").strip().lower()
    
    if gender == "m":
        print("You are male.")
    elif gender == "f":
        print("You are female.")
    else:
        print("Invalid input. Please enter 'm' for male or 'f' for female.")