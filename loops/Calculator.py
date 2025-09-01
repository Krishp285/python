while True:
    a = int(input("enter a value of no1 :-"))
    b = int(input("enter a value of no2 :-"))

    while True:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Modulus")
        print("6. Exponentiation" )
        print("7. Floor Division")
        print("8. add new Number")
        print("9. Exit")
        choice = int(input("Enter your choice (1-9): "))

        match choice:
            case 1:
                print("Addition:", a + b)
            case 2:
                print("Subtraction:", a - b)
            case 3:
                print("Multiplication:", a * b)
            case 4:
                print("Division:", a / b)
            case 5:
                print("Modulus:", a % b)
            case 6:
                print("Exponentiation:", a ** b)
            case 7:
                print("Floor Division:", a // b)
            case 8:
                print("Adding new numbers...")
                break
            case 9:
                exit()
            case _:
                print("Invalid choice")
