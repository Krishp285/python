# 1. Ask user to give name and marks of 10 different students. Store them in dictionary."""
d ={}
for i in range(1):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    d[name] = marks

# 2. Sort the above dictionary in ascending order of Marks.

sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(sorted_d)
# 3. Make a Python program to count letters of the word: MISSISSIPPI. 
# Your program should store them in a dictionary as: {"M":1, "I":4, "S":4, "P":2}. Next, generalize this program for any word entered by user."""

word = input("Enter a word: ")
letter_count = {}
for char in word:
    if char in letter_count:
        letter_count[char] += 1
    else:
        letter_count[char] = 1
print(letter_count)

# 4.result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60], 'Computers': [93, 88, 79, 96, 70]}
# Expected Output: [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60], 'Computers': [93, 88, 79, 96, 70]}


# 5.list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
#  input string = 'bug'
#  output list = ['bug bun bug bun bug bug', 'buggy bug bug buggy', 'bunny bug', 'no bun']

list1 = ['no bun', 'bug bun bug bun bug bug', 'bunny bug', 'buggy bug bug buggy']
input_string = 'bug'
sorted_list = sorted(list1, key=lambda x: x.count(input_string), reverse=True)
print(sorted_list)
# 6.Write a Python program to drop empty items from a given dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

d = {'c1': 'Red', 'c2': 'Green', 'c3': None}
cleaned_dict = {k: v for k, v in d.items() if v is not None}
print(cleaned_dict)

# 7. Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190} 

d = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
filtered_dict = {k: v for k, v in d.items() if v > 170}
print(filtered_dict)
# 8. 
# Write a Python program to sort Counter by value.
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)] 

from collections import Counter
d = {'Math':81, 'Physics':83, 'Chemistry':87}
sorted_counter = sorted(d.items(), key=lambda item: item[1], reverse=True)
print(sorted_counter)

# 9. 
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

d = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for key, value in d:
    if key in result:
        result[key].append(value)
    else:
        result[key] = [value]
print(dict(result))
# 10. 
#  A Python Dictionary contains List as a value. Write a Python program to update the list values 
#  in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}

d = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
for key in d:
    d[key] = [x + 1 for x in d[key]]    
print(d)
