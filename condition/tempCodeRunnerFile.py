number = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci series:")
while a <= number:
    print(a)
    a, b = b, a + b