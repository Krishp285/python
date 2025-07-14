# Program to demonstrate all  operators

# 1) Arithmetic Operators

a = 10
b = 5
print("Addition:", a + b)          # 15
print("Subtraction:", a - b)       # 5
print("Multiplication:", a * b)    # 50
print("Division:", a / b)          # 2.0
print("Floor Division:", a // b)    # 2
print("Modulus:", a % b)           # 0
print("Exponentiation:", a ** b)   # 100000

# 2) Comparison Operators

print("Equal:", a == b)            # False
print("Not Equal:", a != b)        # True
print("Greater than:", a > b)      # True
print("Less than:", a < b)         # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)     # False

# 3) Assignment Operators

a = 10
b = 5
a += b  # a = a + b
print("After += :", a)  # 15
b -= 2  # b = b - 2
print("After -= :", b)  # 3
a *= 2  # a = a * 2
print("After *= :", a)  # 30
b /= 2  # b = b / 2
print("After /= :", b)  # 1.5
a //= 3  # a = a // 3
print("After //= :", a)  # 10
b %= 1  # b = b % 1
print("After %= :", b)  # 0.5
a **= 2  # a = a ** 2
print("After **= :", a)  # 100



# 4) Logical Operators

print("Logical AND:", a > 5 and b < 5)  # False
print("Logical OR:", a > 5 or b < 5)   # True
print("Logical NOT:", not (a > 5))      # False

# 5) Bitwise Operators

print("Bitwise AND:", a & b)            # 0
print("Bitwise OR:", a | b)             # 3
print("Bitwise XOR:", a ^ b)            # 3
print("Bitwise NOT:", ~a)               # -101
print("Bitwise Left Shift:", a << 1)    # 200
print("Bitwise Right Shift:", a >> 1)   # 50


# 6) Identity Operators

print("Identity is:", a is b)          # False
print("Identity is not:", a is not b)  # True

# 7) Membership Operators

list1 = [1, 2, 3, 4, 5]

print("Membership in list:", 3 in list1)  # True
print("Membership not in list:", 6 not in list1)  # True


# 8) unary Operators

a = 10
print("Unary plus:", +a)  # 10
print("Unary minus:", -a)  # -10

# 9) Ternary Operator

x = 5
y = 10
result = "x is greater" if x > y else "y is greater"
print("Ternary result:", result)  # "y is greater"

# 10) Membership Operators
list2 = [1, 2, 3, 4, 5]
print("Membership in list2:", 3 in list2)  # True
print("Membership not in list2:", 6 not in list2)  # True
print("Membership in string:", 'a' in "apple")  # True


# 11) Type Casting
a = 10
b = 5.5
print("Integer to float:", float(a))  # 10.0
print("Float to integer:", int(b))  # 5
print("String to integer:", int("123"))  # 123
print("String to float:", float("123.45"))  # 123.45


