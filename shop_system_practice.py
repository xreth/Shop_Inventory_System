inventory = []

while True:
    question = input("Which command do you require? (1) Add inventory (2) View inventory (3) Search for item (4) Remove an item (5) Exit: ")

    if question == "1":
        print("Add inventory selected")
        inventory_add = input("Add inventory item: ")
        inventory.append(inventory_add)
        print("Item added:", inventory_add)
    if question == "2":
        print("view invenotry selected")
        print(inventory)
    if question == "3":
        print("search item selected")
        search = input("enter item name: ")
        if search == inventory:
            print("item found")
    if question == "4":
        print("remove an item selected")
        remove = input("which item would you like to remove: ")
        inventory.remove(remove)
    if question == "5":
        break
        
