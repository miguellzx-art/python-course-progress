try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        years_left = 18 - age
        print(f"You are not old enough to enlist yet. You still have {years_left} years left to enlist.")
    elif age == 18:
        print("You are exactly the right age to enlist. Look for the nearest military enlistment office.")
    else:
        print("You are past the enlistment age. Please go to the nearest military office to regularize your situation.")
except ValueError:
    print("Please enter a valid age.")