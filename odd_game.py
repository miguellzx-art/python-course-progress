from random import randint 
v = 0
while True:
    player = int(input("Choose a number between 1 and 10: "))
    computer = randint(1, 10)
    total = player + computer
    type = input("Odd or Even? (O/E): ").upper()
    print(f"You choose {player}, computer rolled {computer}. Total is {total}")
    if type == "E":
        if total % 2 == 0:
            print("You win!")
            v += 1
        else:
            print("You lose!")
            break
    elif type == "O":
        if total % 2 == 1:
            print("You win!")
            v += 1
        else:
            print("You lose!")
            break
print(f"You won {v} times.")