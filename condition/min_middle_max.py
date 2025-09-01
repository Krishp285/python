a = int(input("enter a number 1:"))
b = int(input("enter a number 2:"))
c = int(input("enter a number 3:"))

if a > b and a > c:
    print("max is:", a)
    if b < c:
        print("min is:", b)
        print("middle is:", c)
    else:
        print("min is:", c)
        print("middle is:", b)
elif b > a and b > c:
    print("max is:", b)
    if a < c:
        print("min is:", a)
        print("middle is:", c)
    else:
        print("min is:", c)
        print("middle is:", a)
else:
    print("max is:", c)
    if a < b:
        print("min is:", a)
        print("middle is:", b)
    else:
        print("min is:", b)
        print("middle is:", a)