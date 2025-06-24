# Program to swap two numbers without using a third variable

a = int(input("enter the value of no1: "))   # 5
b = int(input("enter the value of no2: "))  # 10

a = a + b # a =15
b = a - b # b = 5
a = a - b # a = 10

print("After swapping: no1 =", a, "no2 =", b)  # no1 = 10, no2 = 5

# Program to swap two numbers using a third variable

temp = a  # temp = 5
a = b  # a = 10
b = temp  # b = 5
print("After swapping using third variable: no1 =", a, "no2 =", b)  # no1 = 5, no2 = 10