from time import sleep

countdown = int(input("Enter the countdown you want: "))
for c in range(countdown, -1, -1):
    print(c)
    sleep(1)