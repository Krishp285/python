a = int(input("Enter a number: "))
sum = 0
mul = 1
for i in str(a):
        sum = sum +  int(i)
        mul = mul * int(i)
print("Twin numbers" if sum == mul else "Not twin numbers")

#Using nested loop

a = int(input("Enter a start number: "))
b = int(input("Enter a end number: "))
for i in range(a, b + 1):
    sum = 0
    mul = 1
    for j in str(i):
        sum = sum + int(j)
        mul = mul * int(j)
    print(i,":", 'Twin numbers' if sum == mul else 'Not twin numbers')