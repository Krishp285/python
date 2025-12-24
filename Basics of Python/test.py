#what is object identity in Python?
#Object identity in Python refers to the unique identifier assigned to each object in memory. You can check the identity of an object using the built-in `id()` function, which returns a unique integer representing the object's memory address during its lifetime. Two variables that reference the same object will have the same identity.
x,y = 3,3
print(x is y) 
print(x is not y)  
print(id(x), id(y)) # Outputs different ids for x and y because they are different objects  

a = [1, 2, 3]
b = a
print(a is b)  # Outputs: True because both a and b reference the same list object
print(a is not b)  # Outputs: False because both a and b reference the same list object


l = [1,2,3]
print(1 in l)  # Outputs: True because 1 is an element of the list l
print(4 in l)  # Outputs: False because 4 is not an element of the list l
print(4 not in l)  # Outputs: True because 4 is not an element of the list l

print("krish", end="123")
print("patel")
print("hello", "world", sep="---")