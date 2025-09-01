# match :- match is used to match a value against a set of patterns and execute code based on the first matching pattern.
# It is similar to switch-case statements in other languages.

print('1 for addition \n2 for subtraction \n3 for multiplication \n4 for division \n5 for modulus \n6 for exponentiation \n7 for floor division')
choice = int(input('Enter your choice: '))
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
match(choice):
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
    case _:
        print("Invalid choice")