import math
a = int(input("Enter a number: "))
sum = 0
rev = a
for i in range(1, len(str(a)) + 1):
    temp = rev % 10
    sum += math.factorial(temp)
    rev = rev // 10
if sum == a:
    print("Strong number")
else:
    print("Not a strong number")
    

# using nested loop
sum = 0
rev = a
for i in range(1, len(str(a)) + 1):
    temp = rev % 10
    mul = 1
    for j in range(1, temp + 1):
        mul = mul * j 
    sum = sum + mul
    rev = rev // 10

print(sum)
if sum == a:
    print("Strong number")
else:
    print("Not a strong number")