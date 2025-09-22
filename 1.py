from cv2 import reduce


# l = [10,20,30,40,50,"qww"]
# print(20 in l)
# print(20 not in l)
# print(l[0] is l[-1])
# print(l[0] is not l[-1])

# x = int(input("Enter a number: "))
# print(x)

# print(chr(66))

# s = "hello"
# print(list(s))

# x,y,z = 10,20,30
# print(x,y,z)

# x = 10,20,30    
# print(x)
# print(type(x))
# x = 5
# print(x*'*')

# x = bytearray("hello", "utf-8")
# print(x)
# print(type(x))

# x = None
# x = 10
# print(x)

# print(10%3,sep=' ')
# print(10//3,sep=' ')

# name = 10
# print(name)
# name = "university"
# print(name)

# s = "hello world"
# print(s[::-3])
# print(s.capitalize())

# s1 = "madam"
# if s1 == s1[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")


# print(s1.replace('a', '3' , 1))

# print(s1.lower())

# s = "hello world welcome to python programming"
# print(s[-5:-2:2])


# d = dict(name="john", age=25)
# print(d.pop('age', 'not found'))
# print(d)
# print(d.popitem())
# print(d)
# d.update({'age':30})
# print(d)

# d1 = d.copy()
# print(d1)
# d1.clear()
# print(d1)

# d = { 'name': 'Alice', 'age': 30, 'city': 'New York' }
# del d
# print(d)
# # print(d)

# x = (10, 20, 30)
# print(x)
# print(y)
# print(z)
# print(type(x))

# x1 = x + (40,)
# print(x1)

# s = "heloo hello"
# print(s.replace('o', 'a', 1))



# for i in range(2,2):
#     print(i)







# #1
# l = [10,20,30,40,50,10,20]
# nl = []
# for i in range(0,len(l)):
#     if l[i] not in nl :
#         nl.append(l[i])
# print(nl)

# print(list(set(l)))

# #2

# tl = [(1,20),(1,2),(1,1)]

# for i in range(len(tl)):
#     for j in range(i+1, len(tl)):
#         if tl[i][-1] > tl[j][-1]:
#             temp = tl[i]
#             tl[i] = tl[j]
#             tl[j] = temp
# print(tl)


# #3
# D1={"s1":80 , "s2":45 , "s3":76 , "s4":52 , "s5":82}
# print("Maximum " ,max(D1.get(k) for k in D1))
# print("Minimum " ,min(D1.get(k) for k in D1))

# #4
# s = "madam"
# if s == s[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome") 

# #5
# d = {'alice':[10,20,30,40] ,'bob':[50,60,70,80]}
# nd = {}
# for key , value in d.items():
#     nd[key] = sum(value)
# print(nd)
# print(max(max(d[key]) for key in d))


# #6 
# d = {}

# for i in range(1,10):
#     d[i] = i*i
# print(d)


# #7
# odd = set()
# prime = set()
# for num in range(1, 11):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             prime.add(num)

# for i in range(1,11,2):
#     odd.add(i)


# print("Odd numbers:", odd)
# print("Prime numbers:", prime)

# print(odd.union(prime))
# print(odd.intersection(prime))
# print(odd.difference(prime))
# print(prime.difference(odd))
# print(odd.symmetric_difference(prime))

# #8
# n = input("Enter a number: ")

# a, b = 0, 1
# print(a,b, end=' ')
# for i in range(2, int(n)):
#     c = a + b
#     print(c, end=' ')
#     a = b
#     b = c

# x, y = 10, 20
# print('krish' * 4)
# print(x, y)

# print(bytes(5))
# my_bytes = b"Python"
# print(my_bytes[0])  # Output: 80 (ASCII value of 'P')

# print(ord('A'))  # Output: 65
# print(chr(65))  # Output: 'A'
# data = b"abcdefg"
# view = memoryview(data)
# print(view[1:4].tobytes())  # Output: b'bcd'


# x= 11
# if not x == 5 :
#     print("true")
# else:
#     print("false")

# print(101 ^ 102)
# s = "krishna 007"
# print(s.split("n"))
# print(sum(ord(c) for c in s))


# l = [10,20,30,40,50]
# print(l[-1])
# l[0] = 100 
# print(l)


# pi = 3.14159265
# print(f"Pi rounded to 2 decimals: {pi:.2f}")   # 3.14
# print("Pi rounded to 3 decimals: {:.3f}".format(pi))  # 3.142



# name = "krishna"
# print("my name is %s " %name)

# print(list((10,20,30,40,50)))

# d = {1: 'a', 2: 'b', 3: 'c'}
# d[4]= 'd' 
# print(d.get(11, 'not found'))
# print(d.pop(1))
# print(d)

# l = [10,20,10,10,30,40,50,20]
# print(list(set(l)))




# student = {
#     's1' : {'name': 'Alice', 'age': 20, 'marks': [85, 90, 78]},
#     's2' : {'name': 'Bob', 'age': 22, 'marks': [88, 76, 95]},
#     's3' : {'name': 'Charlie', 'age': 23, 'marks': [92, 89, 84]}
# }
# for key, value in student.items():
#     for k , v in value.items():
#         if k == 'marks':
#             print(value['name'] ,max(v))

# s = "hello world welcome to python programming"
# print(sorted(s.split()))


# t  = (10,)
# print(t)

# l = [(1, 2, 3),(4,5,6)]
# x , y , z = list(zip(*l))
# print(x)
# print(y)
# print(z)

# s = "krish"
# print(s.lstrip('ki'))

# set = {1,2,3,4,5}

# l = list(set)
# l[0] = 10
# set = set(l)
# print(set)

i = 1
while i in range(1,10):
    print(i)
    i += 1