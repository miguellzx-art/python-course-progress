num = int(input("Type a number: ")), int(input("Type a number: ")), int(input("Type a number: ")), int(input("Type a number: "))
print(f"you typed the number {num}")
print(f"The value 9 appears {num.count(9)} times.")
if 3 in num:
    print(f"The value 3 appears in the {num.index(3)} position.")
else:
    print("The value 3 do not appears in the tuple")
for n in num:
    if n % 2 == 0:
        print(f"The even numbers are {n}")