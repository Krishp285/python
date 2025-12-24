# Write a Python program to check whether the given number is prime or not. 

number = int(input("Enter a number: "))
if number > 1:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
else:
    print(f"{number} is not a prime number")

# # Write a Python program to print Fibonacci series up to number given by user.

number = int(input("Enter a number: "))
a, b = 0, 1
for i in range(number):
    print(a, end=' ')
    a, b = b, a + b

# Write a Python program to check whether the given number is an Armstrong number or not 

number = int(input("Enter a number: "))
a = number
length = len(str(number))
print(length)
sum = 0
for i in range(1,length+1):
    digit = number % 10
    sum = sum + (digit**length)
    number = number // 10
if sum == a:
    print(f"{a} is an Armstrong number")
else:
    print(f"{a} is not an Armstrong number")

# # Write a Python program to print Prime numbers between 1 to 100 

for num in range(1, 101):
    if num > 1:   # 1 is not prime
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

 # Write a Python program to print following pattern: 1 01 101 0101 10101

for i in range(1, 6):
    for j in range(1, i + 1):
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()

# # Write a python program to enter a decimal number. Calculate and display the binary equivalent of this number. 

decimal = int(input("Enter a decimal number: "))
binary = bin(decimal).replace("0b", "") # replace is used to remove the '0b' prefix
print(f"Binary equivalent of {decimal} is {binary}")

# # Write a python program to implement factorial for given input. 

number = int(input("Enter a number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Factorial of {number} is {factorial}")

# Write a Python program to multiply two matrices 

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


# Write a Python program to find the transpose of the matrix, take input of matrix from user

matrix = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at ({i},{j}): "))
        row.append(element)
    matrix.append(row)

print("Input matrix:",matrix)

matrix = [[1,2],[4,5],[7,8]]
transpose = []
rows = len(matrix)
cols = len(matrix[0]) if rows > 0 else 0
for i in range(cols):
    new_row = []
    for j in range(rows):
        new_row.append(matrix[j][i])
    transpose.append(new_row)
print("Transpose of the matrix:", transpose)


# # # Write a Python program to multiply two N X N matrices

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[9,8,7],[6,5,4],[3,2,1]]
c = [[0,0,0],[0,0,0],[0,0,0]]
print(len(a))
print(len(b[0]))
print(len(b))
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]
print("Multiplication of the matrices:", c)

# Write a Python program to multiply two N X N matrices , take input of matrices from user

A = []
B = []
C = []
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at ({i},{j}): "))
        row.append(element)
    A.append(row)

print("Input matrix:",A)
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at ({i},{j}): "))
        row.append(element)
    B.append(row)
print("Input matrix:",B)

print(len(A))
print(len(B[0]))
print(len(B))
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
print("Multiplication of the matrices:", C)


# Write a Python function sumofsquare(M) that takes a non-empty list of integers and returns a list [even, odd] in which the first element is the sum of all even numbers and the second element is the sum of all odd numbers.

l = [1,2,3,4,5,6,7,8,9,10]
def sumofsquare(M):
    even_sum = 0
    odd_sum = 0
    for num in M:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return [even_sum, odd_sum]
print(sumofsquare(l))

# Explain nested if statements in Python with logical combinations. Write
# program to get temperature and humidity from the user. Display following
# messages in different situations:
# (1) If temperature>30 and humidity Message: “Hot and Dry”
# (2) If temperature is in between 20 to 30 and Humidity between 20% to
# 40% Message: “Good weather condition”
# (3) If temperature is between 20 to 30 and Humidity more than 80%
# Message: “Moisture present”.

temperature = float(input("Enter the temperature in Celsius: "))
humidity = float(input("Enter the humidity in percentage: "))

if temperature > 30 and humidity < 20:
    print("Hot and Dry")
elif 20 <= temperature <= 30 and 20 <= humidity <= 40:
    print("Good weather condition")
elif 20 <= temperature <= 30 and humidity > 80:
    print("Moisture present")

# Write a Python program to enumerate through a tuple and print index and value of each item

t = (1, 2, 3, 4, 5)

for i,j in enumerate(t , start=2):
    print(i,j)

# Consider the list st = [9, 8, 7, 6, 5, 4, and 3]. Write a Python program which performs the following operations without using built-in methods:
# Insert element 11 at beginning of the list
# Delete the element at index position 5
# Insert element 10 at end of the list
# Print all elements in reverse order

st = [9, 8, 7, 6, 5, 4, 3]
# Insert element 11 at beginning of the list
st = [11] + st
# Delete the element at index position 5
st = st[:5] + st[6:]
# Insert element 10 at end of the list
st = st + [10]
# Print all elements in reverse order
print(st[::-1])


# Write a program to compare two lists in Python.
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
if list1 == list2:
    print("The lists are equal.")
else:
    print("The lists are not equal.")


# Write a Python program to get and print the maximum and minimum values of a dictionary.
my_dict = {'a': 10, 'b': 20, 'c': 5, 'd': 15}
max_value = max(my_dict.values())
min_value = min(my_dict.values())
print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Write a Python Program to generate dictionary of numbers and their squares (i, i*i) from 1 to n.
n = int(input("Enter the value of n: "))
squares_dict = {}
for i in range(1,n+1):
    squares_dict[i] = i * i
print(squares_dict)


# Write a python program that has dictionary of names of students and a list of their marks in 4 subjects. Create another dictionary from this dictionary that has names of the students and their total marks. Find out the topper and his/her score.

students_marks = {
    'Alice': [85, 90, 78, 92],
    'Bob': [88, 76, 95, 89],
    'Charlie': [90, 91, 85, 87],
    'David': [70, 80, 75, 85]
}
total_marks = {}
for student, marks in students_marks.items():
    total_marks[student] = sum(marks)
print("Total Marks:", total_marks)
topper = max(total_marks, key=total_marks.get) # to get key with max value
print(f"Topper: {topper} with score {total_marks[topper]}") 

# another way to get max value

max_score = 0
topper_name = ""
for student, score in total_marks.items():
    if score > max_score:
        max_score = score
        topper_name = student

# Write a Python program to get the maximum value of a dictionary value.
d = {'a':1, 'b':2, 'c':3}
print(max(k for k in d.values()))
print(max(d.values())) # both are same


# Write a python program that generates a set of prime numbers and another set of odd numbers. Demonstrate the result of union, intersection, difference, and symmetric difference operations on these sets.

odd = set()
prime = set()
for num in range(1,51):
    if num >1:
        is_prime = True
        for i in range(2,num):
            if num%i == 0:
                is_prime = False
                break   
        if is_prime:
            prime.add(num)
for num in range(1,51,2):
    odd.add(num)
print("Prime Numbers:", prime)
print("Odd Numbers:", odd)
print("Union:", prime.union(odd)) # or prime | odd
print("Intersection:", prime.intersection(odd)) # or prime & odd
print("Difference (Prime - Odd):", prime.difference(odd))  # or prime - odd
print("Symmetric Difference:", prime.symmetric_difference(odd)) # or prime ^ odd

        

#Develop Python program to take a list of non-empty tuples and create a list that is sorted in ascending order by the last member in each tuple.

l = [(1,2),(3,1),(4,3)]
for i in range(len(l)):
    for j in range(i+1, len(l)):
        if l[i][-1] > l[j][-1]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
print(l)



# write a program to print fibonacci series using recursion

def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
num = int(input("Enter a number: "))
for i in range(num):
    print(fibonacci(i), end=' ')


#Write a Python program to copy the contents of one text file to another.

source_file = open("source.txt", "r")
destination_file = open("destination.txt", "w")
source_file_contents = source_file.read()
destination_file.write(source_file_contents)
source_file.close()
destination_file.close()

#Write a Python program that reads a text file and changes the file by capitalizing each character of file.
file = open("text1.txt", "r+")
content = file.read()
file.seek(0) 
file.write(content.upper())
file.close() 

# Write a Python program to count words, characters and spaces from text file.

file = open("text2.txt", "r")
word_count = 0
char_count = 0
space_count = 0
for line in file:
    char_count += len(line)
    word_count += len(line.split())
    space_count += line.count(' ')
file.close()
print(f"Words: {word_count}, Characters: {char_count}, Spaces: {space_count}")

#Create a Python program to read a text file and do following:
#Print no. of lines
#Print no. of unique words Store each word with its occurrence in dictionary
file = open("text3.txt", "r")
line_count = 0
word_dict = {}
for line in file:
    line_count += 1
    words = line.split()
    for word in words:
        word = word.lower()
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
file.close()
print(f"Number of lines: {line_count}")
print(f"Number of unique words: {len(word_dict)}")
print(f"Word occurrences: {word_dict}")

#WAP for considering the following instructions: (Create input.txt, write data, read content, write to output.txt, close files).
input_file = open("input.txt", "w")
input_file.write("This is a sample input file.\nIt contains multiple lines of text.\nThis is the third line.")
input_file.close()
input_file = open("input.txt", "r")
content = input_file.read()
input_file.close()
output_file = open("output.txt", "w")
output_file.write(content)
output_file.close()

#Write a python program to read and write data from a text file using pandas library.
import pandas as pd
data = pd.read_csv("data.txt")  # assuming data.txt is a CSV file
print(data)
data.to_csv("output_data.txt", index=False)  # writing to another CSV file

# write a program to reverse string using loop

s = "krish patel"
for i in range(len(s)-1,-1,-1):
    print(s[i], end='') 

# happy number 
number = int(input("Enter a number: "))
temp = number

for i in range(1, number):
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 2
        temp = temp // 10
    temp = sum
    if sum == 1:
        print(f"{number} is a happy number")
        break
    elif i == number - 1:
        print(f"{number} is not a happy number")


# ramanujan number
number = int(input("Enter a number: "))
found = False
for i in range(1, int(number**(1/3)) + 1):
    for j in range(i, int(number**(1/3)) + 1):
        for k in range(1, int(number**(1/3)) + 1):
            for l in range(k, int(number**(1/3)) + 1):
                if i**3 + j**3 == k**3 + l**3 == number and (i != k or j != l):
                    print(f"{number} can be expressed as the sum of two cubes in two different ways: {i}^3 + {j}^3 and {k}^3 + {l}^3")
                    found = True
if not found:
    print(f"{number} cannot be expressed as the sum of two cubes in two different ways.")
    
