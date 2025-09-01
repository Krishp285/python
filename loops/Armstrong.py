a = int(input("Enter a number: "))
count = 0
sum = 0
length = len(str(a))

for i in range(1, length + 1):
    sum = sum + (a % 10) ** length
    

print("Armstrong number" if sum == a else "Not an Armstrong number")