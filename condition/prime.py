# Program to check whether a number is prime

no = int(input("Enter a number: "))
if no > 1:
    for i in range(2, int(no**0.5) + 1):
        if no % i == 0:
            print(no, "is not a prime number")
            break
    else:
        print(no, "is a prime number")
else:
    print(no, "is not a prime number")
    