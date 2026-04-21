from random import randint
items = ("Rock", "Paper", "Scissors")
computer = randint(0, 2)
print(f"Your options:\n0 - {items[0]}\n1 - {items[1]}\n2 - {items[2]}")
player = int(input("What is your play? "))
print(f"The computer played {items[computer]}")
print(f"The player played {items[player]}")
if computer == 0:
    if player == 0:
        print("Draw!")
    elif player == 1:
        print("Player wins!")
    elif player == 2:
        print("Computer wins!")
    else:
        print("Invalid play!")
elif computer == 1:
    if player == 0:
        print("Computer wins!")
    elif player == 1:
        print("Draw!")
    elif player == 2:
        print("Player wins!")
    else:
        print("Invalid play!")
elif computer == 2:
    if player == 0:
        print("Player wins!")
    elif player == 1:
        print("Computer wins!")
    elif player == 2:
        print("Draw!")
    else:
        print("Invalid play!")