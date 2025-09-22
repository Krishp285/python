# # Write a Python program to check whether the given number is prime or not. 


for num in range(1, 11):
    if num > 1:   # 1 is not prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)


# # Write a Python program to print Fibonacci series up to number given by user.

number = int(input("Enter a number: "))
i = 1
a, b = 0, 1
print("Fibonacci series:")
while i <= number:
    print(a,end=' ')
    a, b = b, a + b
    i += 1

# # Write a Python program to check whether the given number is an Armstrong number or not 

# number = int(input("Enter a number: "))
# a = number
# length = len(str(number))
# print(length)
# sum = 0
# for i in range(1,length+1):
#     digit = number % 10
#     sum = sum + (digit**length)
#     number = number // 10
# if sum == a:
#     print(f"{a} is an Armstrong number")
# else:
#     print(f"{a} is not an Armstrong number")

# # Write a Python program to print Prime numbers between 1 to 100 

# for num in range(1, 101):
#     if num > 1:   # 1 is not prime
#         is_prime = True
#         for i in range(2, num):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             print(num)

# # Write a Python program to print following pattern: 1 01 101 0101 10101

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         if (i + j) % 2 == 0:
#             print("1", end="")
#         else:
#             print("0", end="")
#     print()

# # Write a python program to enter a decimal number. Calculate and display the binary equivalent of this number. 

# decimal = int(input("Enter a decimal number: "))
# binary = bin(decimal).replace("0b", "") # replace is used to remove the '0b' prefix
# print(f"Binary equivalent of {decimal} is {binary}")

# # Write a python program to implement factorial for given input. 

# number = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print(f"Factorial of {number} is {factorial}")

# # Write a Python program to multiply two matrices 

def multiply_matrices(A, B):
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]   
print("Resultant matrix after multiplication:", multiply_matrices(A, B))


# Write a Python program to find the transpose of the matrix


# take input of matrix from user
# matrix = []
# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         element = int(input(f"Enter element at ({i},{j}): "))
#         row.append(element)
#     matrix.append(row)

# print("Input matrix:",matrix)




# matrix = [[1,2],[4,5],[7,8]]
# transpose = []
# rows = len(matrix)
# cols = len(matrix[0]) if rows > 0 else 0
# for i in range(cols):
#     new_row = []
#     for j in range(rows):
#         new_row.append(matrix[j][i])
#     transpose.append(new_row)
# print("Transpose of the matrix:", transpose)


# # # Write a Python program to multiply two N X N matrices


# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[9,8,7],[6,5,4],[3,2,1]]
# c = [[0,0,0],[0,0,0],[0,0,0]]
# print(len(a))
# print(len(b[0]))
# print(len(b))
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             c[i][j] += a[i][k] * b[k][j]
# print("Multiplication of the matrices:", c)

# # # Write a Python program to multiply two N X N matrices
# a = [[1,2,3],[4,5,6],[7,8,9]]
# b = [[9,8,7],[6,5,4],[3,2,1]]
# c = [[0,0,0],[0,0,0],[0,0,0]]
# print(len(a))
# print(len(b[0]))
# print(len(b))
# for i in range(len(a)):
#     for j in range(len(b[0])):
#         for k in range(len(b)):
#             c[i][j] += a[i][k] * b[k][j]
# print("Multiplication of the matrices:", c)
# # Write a Python function sumofsquare(M) that takes a non-empty list of integers and returns a list [even, odd] in which the first element is the sum of all even numbers and the second element is the sum of all odd numbers.

# l = [1,2,3,4,5,6,7,8,9,10]
# def sumofsquare(M):
#     even_sum = 0
#     odd_sum = 0
#     for num in M:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num
#     return [even_sum, odd_sum]
# print(sumofsquare(l))

# # Explain nested if statements in Python with logical combinations. Write
# # program to get temperature and humidity from the user. Display following
# # messages in different situations:
# # (1) If temperature>30 and humidity Message: “Hot and Dry”
# # (2) If temperature is in between 20 to 30 and Humidity between 20% to
# # 40% Message: “Good weather condition”
# # (3) If temperature is between 20 to 30 and Humidity more than 80%
# # Message: “Moisture present”.

# temperature = float(input("Enter the temperature in Celsius: "))
# humidity = float(input("Enter the humidity in percentage: "))

# if temperature > 30 and humidity < 20:
#     print("Hot and Dry")
# elif 20 <= temperature <= 30 and 20 <= humidity <= 40:
#     print("Good weather condition")
# elif 20 <= temperature <= 30 and humidity > 80:
#     print("Moisture present")


# t = (1, 2, 3, 4, 5)

# for i in enumerate(t , start=2):
#     print(i)

