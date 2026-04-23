from random import randint

print("Roll the dice, you get two dice per round.")

dice1 = randint(1, 6)
dice2 = randint(1, 6)
player_total = dice1 + dice2

while True:
    response = input("Roll the dice? (y/n) ")
    
    if response.lower() == 'y':
        print(f"You rolled: {dice1} and {dice2}")
        print(f"Player dice total: {player_total}")
        
        computer_dice1 = randint(1, 6)
        computer_dice2 = randint(1, 6)
        computer_total = computer_dice1 + computer_dice2
        
        print(f"Computer rolled the dice and got: {computer_total}")
        print(f"Computer dice total: {computer_total}")
        
        if player_total > computer_total:
            print("Congratulations, you won!")
        elif computer_total > player_total:
            print("Computer won. Try again!")
    
    elif response.lower() == 'n':
        print("Game ended.")
        break