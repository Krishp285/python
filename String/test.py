s = 'kp'
for  i in s:
    print(i)

s1 = "hello world world"

# if i want all occurence of 'world' using find as there is no inbuild function to find all occurence
index = -1
while True:
    index = s1.find('world', index + 1)
    if index == -1:
        break
    print(f"'world' found at index: {index}")


s2 = "madam"
if s2 == s2[::-1]:
    print(f"{s2} is a palindrome")
else:
    print(f"{s2} is not a palindrome")

l = [1, 2, 3]
print(id(l))
l[0] = 10
print(id(l))


print("hello"+"krishna")

s = "Hello Python Python"
s = str(s.split())
print(s.find("Python" ,10))


l= ['apple', 'banana', 'cherry', 'date']
print(sorted(l,key=len,reverse=True))

l1 = l.copy()

list = [1,2,3,4,5]
print(list.sort(reverse=True))


d = {'a':1, 'b':2, 'c':3}
print(d.items())


student = {"name": "Krish", "age": 21, "city": "Ahmedabad"}
print(student)
student.update({"age": 22, "city": "Mumbai"})
student.update({"grade": "A"})
print(student)
del student["city"]
print(student)



john_wick_info= {
 "title": "John Wick",
 "release_year": 2014,
 "portrayed_by": "Keanu Reeves",
 "number_of_films": 4
 }
if "car" in john_wick_info.keys():
 print('Yes')
else:
 print('No')


a=("Spiderman", "John Wick", "batman", "Iron Man", "Wonder Woman", "Thor", "Black Widow", "Captain America", "Loki", "Superman", "Deadpool")
b=list(a)
b[1]="Aquaman"
a=tuple(b)
print(a)



t = ("x", "y", "z")
print(list(enumerate(t)))    


names = ["Krish", "Raj", "Neha"]
ages = [21, 22, 20]

zipped = zip(names, ages)
print(list(zipped))



student = {"name": "Krish", "age": 21, "city": "Ahmedabad"}

# Access using key
print(student["name"])   # Krish

# Access using get()
print(student.get("age"))           # 21
print(student.get("grade", "A+"))   # A+ (default value)
print(student)

for i in student.keys():
    print(i)

t = 1,2,3,4
print(type(t)) # <class 'tuple'>

t = (5, 10, 15)
print(sum(t))   # 30


d = {'a': 1, 'b': 2, 'c': 3}
print(d.fromkeys(['a'])) 

t = (1, 2, 3, 4, 5)
a, b, *c = t
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]


# XRANGE vs RANGE
# In Python 2, range() returns a list, while xrange() returns an xrange object which generates numbers on demand (lazy evaluation).
# In Python 3, range() behaves like xrange() from Python 2, providing memory efficiency by generating numbers on demand. There is no xrange() in Python 3.

for i in range(-5,5,1):
    print(i)


x = bytes(5)
print(x)  # Output: b'\x00\x00\x00\x00\x00


x = "madam"
p = ""
for i in range(len(x)-1, -1, -1):
    p += x[i]
if p == x:
    print(f"{x} is a palindrome")
else:
    print(f"{x} is not a palindrome")


# Given a list of strings, use a lambda function with filter() to return only the strings that start with a vowel (a, e, i, o, u).
strings = ["apple", "banana", "orange", "grape", "umbrella", "kiwi", "elephant"]
vowel_strings = list(filter(lambda s: s[0].lower() in 'aeiou', strings))
print(vowel_strings)


s = "krishna"
print(s.startswith('kri'))

y = "hello world"
d={}
for i in y:
    if i in 'aeiou':
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
        print(i)
    else:
        continue
print(d)



