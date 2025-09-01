"""
hotel menu : 

1.breakfast :  2 item  
2.lunch  : 2 item  
3.dinner :  2 item  
"""

print("Welcome to the Hotel Menu")
print("1. Breakfast")
print("2. Lunch")
print("3. Dinner")
print("4. Exit")    
choice = int(input("Please select an option (1-4): "))
match choice:
    case 1:
        print("You selected Breakfast")
        print("1. idli sambhar")
        print("2. poha")
        sub_choice = int(input("Please select an item (1-2): "))
        match sub_choice:
            case 1:
                print("You selected idli sambhar")
            case 2:
                print("You selected poha")
            case _:
                print("Invalid choice for breakfast")
    case 2:
        print("You selected Lunch")
        print("1. dal rice")
        print("2. roti sabzi")
        sub_choice = int(input("Please select an item (1-2): "))
        match sub_choice:
            case 1:
                print("You selected dal rice")
            case 2:
                print("You selected roti sabzi")
            case _:
                print("Invalid choice for lunch")
    case 3:
        print("You selected Dinner")
        print("1. paneer butter masala and naan")
        print("2. biryani")
        sub_choice = int(input("Please select an item (1-2): "))
        match sub_choice:
            case 1:
                print("You selected paneer butter masala and naan")
            case 2:
                print("You selected biryani")
            case _:
                print("Invalid choice for dinner")
    case 4:
        print("Exit")
    case _:
        print("Invalid choice")