# lambda :- anonymous function :- function without a name 
# syntax :- lambda arguments : expression   
f = lambda a, b: a + b
print(f(2, 3)) # 5

# filter :- filter(function, iterable)
# filter out the elements from iterable for which function returns True
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, l))
print(even) # [2, 4, 6, 8, 10]

# map :- map(function, iterable)
# apply function to all the elements in iterable

squared = list(map(lambda x: x ** 2, l))
print(squared) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# reduce :- reduce(function, iterable)
# apply function to all the elements in iterable and reduce it to a single value
from functools import reduce

sum = reduce(lambda x, y: x + y, l)
print(sum) # 55

# how answer is 55
# step 1 :- x = 1, y = 2 => 1 + 2 = 3
# step 2 :- x = 3, y = 3 => 3 + 3 = 6
# step 3 :- x = 6, y = 4 => 6 + 4 = 10
# step 4 :- x = 10, y = 5 => 10 + 5 = 15
# step 5 :- x = 15, y = 6 => 15 + 6 = 21
# step 6 :- x = 21, y = 7 => 21 + 7 = 28
# step 7 :- x = 28, y = 8 => 28 + 8 = 36
# step 8 :- x = 36, y = 9 => 36 + 9 = 45
# step 9 :- x = 45, y = 10 => 45 + 10 = 55  

# l = ['apple', 'banana', 'cherry', 'date']

# ans = list(filter(lambda x : x[0] in ('a','e','i','o','u'), l))
# print(ans) # ['apple']