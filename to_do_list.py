inventory = []

while True:
    print("-" * 30)
    print("INVENTORY MANAGEMENT")
    print("-" * 30)

    choice = str(input("Add, Remove, View or Exit? [A/R/V/E]: ")).strip().upper()[0]

    if choice == "A":
        item = input("What do you want to add? ")
        inventory.append(item)
        print(f"[{item}] added successfully!")

    elif choice == "R":
        item = input("What do you want to remove? ")
        if item in inventory:
            inventory.remove(item)
            print(f"[{item}] removed from inventory.")
        else:
            print("Error: Item not found in inventory!")

    elif choice == "V":
        print("\n--- CURRENT INVENTORY ---")
        if not inventory:
            print("The list is empty.")
        else:
            for index, item in enumerate(inventory):
                print(f"{index}: {item}")
    
    elif choice == "E":
        print("Closing system... Goodbye!")
        break
    
    else:
        print("Invalid option! Try again.")