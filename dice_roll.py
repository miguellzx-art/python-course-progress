from random import randint

while True:
    choice = input("\nRoll the dice? (y/n): ")
    
    if choice == 'y':
        player_d1, player_d2 = randint(1, 6), randint(1, 6)
        comp_d1, comp_d2 = randint(1, 6), randint(1, 6)
        
        p_total = player_d1 + player_d2
        c_total = comp_d1 + comp_d2
        
        print(f"You rolled {player_d1} + {player_d2} = {p_total}")
        print(f"Computer rolled {comp_d1} + {comp_d2} = {c_total}")
        
        if p_total > c_total:
            print("Result: Congratulations, you won!")
        elif c_total > p_total:
            print("Result: Computer won. Try again!")
        else:
            print("Result: It's a tie!")
            
    elif choice == 'n':
        print("Thanks for playing! See you next time.")
        break
    else:
        print("Invalid option. Please type 'y' or 'n'.")