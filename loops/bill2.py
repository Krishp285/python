quantity = 0
bill = 0
while True:
    print("1. Fruits")
    print("2. Vegetables")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))

    match choice:
        case 1:
            while True:
                print("1 for Apples")
                print("2 for Bananas")
                print("3 for Oranges")
                print("4 to go back")
                fruit_choice = int(input("Enter your fruit choice (1-4): "))
                
                match fruit_choice:
                    case 1:
                        quantity = int(input("Enter the quantity of items: "))
                        bill += 100 * quantity
                        print("You selected Apples. Rs", 100 * quantity)
                    case 2:
                        quantity = int(input("Enter the quantity of items: "))
                        bill += 50 * quantity
                        print("You selected Bananas. Rs", 50 * quantity)
                    case 3:
                        quantity = int(input("Enter the quantity of items: "))
                        bill += 80 * quantity
                        print("You selected Oranges. Rs", 80 * quantity)
                    case 4:
                        break
                    case _:
                        print("Invalid fruit choice.")
        case 2:
            while True:
                print("1 for Carrots")
                print("2 for Broccoli")
                print("3 for Spinach")
                print("4 to go back")
                vegetable_choice = int(input("Enter your vegetable choice (1-4): "))
                
                match vegetable_choice:
                    case 1:
                        quantity = int(input("Enter the quantity of items: "))
                        bill += 40 * quantity
                        print("You selected Carrots. Rs", 40 * quantity)
                    case 2:
                        quantity = int(input("Enter the quantity of items: "))
                        bill += 60 * quantity
                        print("You selected Broccoli. Rs", 60 * quantity)
                    case 3:
                        quantity = int(input("Enter the quantity of items: "))
                        bill += 30 * quantity
                        print("You selected Spinach. Rs", 30 * quantity)
                    case 4:
                        break
                    case _:
                        print("Invalid vegetable choice.")
                        break
        case 3:
            print("The Bill is ", bill)
            break
        case _:
            print("Invalid choice.")
