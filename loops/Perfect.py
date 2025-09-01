a = int(input("Enter a start number: "))
b = int(input("Enter a end number: "))
for num in range(a, b + 1):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num, "Perfect number")
    else:
        print(num, "Not a perfect number")