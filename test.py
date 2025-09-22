# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(matrix)):
#     transpose = []
#     for j in range(len(matrix[0])):
#         transpose.append(matrix[j][i])
#     print(transpose)


# # Slicing in lists
# l1 = [1, 2, 3, 4, 5]
# print(l1[1:4])  # [2, 3, 4]
# print(l1[::-1])  # [5, 4, 3, 2, 1]
# print(l1[::2])  # [1, 3, 5]
# print(l1[-3:-1])  # [3, 4]
# print(l1[:3])  # [1, 2, 3]
# print(l1[3:])  # [4, 5]
# print(l1[-1:-2:-1]) # [5]

# a = input("Enter a string: ")
# split_string = a.split()
# print(split_string)
# for i in range(len(split_string)):
#     if split_string[i] == split_string[i][::-1]:
#         print(f"{split_string[i]} is a Palindrome")
#     else:
#         print(f"{split_string[i]} is Not a palindrome")

# a = '''krish patel'''
# print(a.title())

# print("apple" < "banana")

# s = "krish is smart and ceo of a company , but he is good at his work"
# print(s.replace("is", "was", len(s.split("is")) - 1))

# a = "krish"
# b = "patel"
# print(a,b)  # pkrahtishel

# c,d = 0,1
# print(c,d)  # 0 1

# a = "krishkri"
# print(a.count('kris'))

# l = [1,1,2,2,3,3,45,6]


# d = {}
# n = int(input("Enter number of elements: "))

# for i in range(n):
#     d[i] = i*i
# print(d)

# d = {}
# new_d = {}
# for i in range(int(input("enter number of elements: "))):
#     name = input("Enter name: ")
#     marks = []
#     for j in range(3):
#         marks.append(input("Enter marks: "))
#     d[name] = marks
# print(d)
# for key, value in d.items():
#     total = sum(int(mark) for mark in value)
#     new_d[key] = total

# print(new_d)

# s = {1, 2, 3, 4, 5}
# print(s)
# print(type(s))

# Write a python program that generates a set of prime numbers and another set of odd numbers. Demonstrate the result of union, intersection, difference, and symmetric difference operations on these sets
# n = 20
# prime = set()
# odd = set()
# for i in range(2, n + 1):
#     is_prime = True
#     for j in range(2, int(i**0.5) + 1):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         prime.add(i)
#     if i % 2 != 0:
#         odd.add(i)

# print("Prime numbers:", prime)
# print("Odd numbers:", odd)

# # Union
# print("Union:", prime | odd)

# # Intersection
# print("Intersection:", prime & odd)

# # Difference
# print("Difference (Prime - Odd):", prime - odd)
# print("Difference (Odd - Prime):", odd - prime)

# # Symmetric Difference
# print("Symmetric Difference:", prime ^ odd)


# Develop Python program to take a list of non-empty tuples and create a list that is sorted in ascending order by the last member in each tuple

# t = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(t) - 1):
#     for j in range(i + 1, len(t)):
#         if t[i][-1] > t[j][-1]:
#             t[i], t[j] = t[j], t[i]
# print(t)

# s = {1, 2, 3, 4, 5}
# print(2 in s)  # True

# set :- membership - yes
# list :- membership - yes
# dict :- membership - yes (keys)
# tuple :- membership - yes
#string :- membership - yes



# s = {1, 2, 3}
# print(min(s))  # 1
# print(max(s))  # 3
# print(sum(s))  # 6
# print(len(s))  # 3
# print(sorted(s))  

# t = 1,2
# print(type(t))  # <class 'tuple'>

# t1 = (1,)
# print(type(t1))  # <class 'tuple'>

# what is enumerate in tuples

# t = (1, 2, 3, 4, 5)
# for index , value in enumerate(t, start=5):
#     print(index, value)

# s = "krish" 
# print(s.format())

# d = {"name": "krish", "age": 20}
# print(d.pop("name")) 
# print(d.popitem())
# print(d)
# print(d.clear())

# d = {"name": "krish", "age": 20}
# print(str(d).capitalize())

# d = {}
# for i in range(int(input("Enter number of elements: "))):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     d[key] = value
# print(d)

# d1 = {"name": "krish", "age": 20, "city": "ahmedabad"}
# for key, value in d1.items():
#     print(f"{key} : {value}")

# d = {"krish":[10,20,30,40],"patel":[20,30,40,50],"hello":[30,40,50,60]}
# new = {}
# for key,value in d.items():
#     new[key] = sum(value)
# print(new)
# for key, value in new.items():
#     if value == max(new.values()):
#         print(key, value)

# d1={"s1":80 , "s2":45 , "s3":76 , "s4":52 , "s5":82}

# for value in d1.values():
#     if value == max(d1.values()):
#         print("max:-", value)
#     if value == min(d1.values()):
#         print("min:-", value)

d = {"krish": [10, 20, 30, 40], "patel": [20, 30, 40, 50], "hello": [30, 40, 50, 60] , "hi": [100,200,300]}
print(d.popitem())