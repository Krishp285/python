# Program to find the largest of three numbers using if-else statements

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2 ):
    if (num1 >=num3):
        largest = num1
    else:
        largest = num3
else:
    if (num2 >= num3):
        largest = num2
    else:
        largest = num3

print("The largest number is:", largest)

# Program to find the largest of three numbers using max function

largest = max(num1, num2, num3)
print("The largest number using max function is:", largest)

# Program to find the largest of three numbers using a single line expression
largest = num1 if (num1 >= num2 and num1 >= num3) else (num2 if num2 >= num3 else num3)
print("The largest number using single line expression is:", largest)

# Program to find the largest of three numbers using ternery operator (?:)
# python does not have a built-in ternary operator like C/C++, but we can simulate it using a conditional expression.
