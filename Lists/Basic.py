# List :- List is a collection of items in a particular order.
# List is created by placing all the items (elements) inside square brackets [ ], separated by commas.
# Example: my_list = [1, 2, 3, 4, 5]

# Properties of List

# 1. Ordered: Lists maintain the order of elements as they are added.
# 2. Mutable: Lists can be modified after creation (e.g., adding/removing elements).
# 3. Allow Duplicates: Lists can contain multiple instances of the same element.
# 4. Heterogeneous: Lists can contain elements of different data types (e.g., integers, strings, etc.).


# Functions(Methods) of list

# 1. append(): Adds an element to the end of the list.

l = [1,2]
l.append(3)
print(l) # [1, 2, 3]

# 2. extend(): Adds multiple elements to the end of the list.

l = [1, 2]
l.extend([3, 4, 5])
print(l) # [1, 2, 3, 4, 5]

# 3. insert(): Adds an element at a specific position in the list.
l = [1, 2, 3]
l.insert(4, 1)
print(l) # [1, 2, 3, 4, 1]

# 4. remove(): Removes the first occurrence of a specific element from the list.

l = [1,2,3,4,5]
l.remove(3)
print(l) # [1, 2, 4, 5]

# 5. pop(): Removes and returns an element at a specific position (default is the last element).

l = [1,4,3,2,0]
l.pop() 
print(l) # [1, 4, 3, 2]

l = [1,4,3,2,0]
l.pop(3)  # 3 is index
print(l) # [1, 4, 3, 2]


# 6. clear(): Removes all elements from the list.

l = [1,2,3,4,5]
l.clear()
print(l) # []


# 7. index(): Returns the index of the first occurrence of a specific element.
l = [1, 2, 3, 4, 5]
print(l.index(3,0,3)) # 2

# 8. count(): Returns the number of occurrences of a specific element.
print(l.count(2)) # 1

# 9. sort(): Sorts the elements of the list in ascending order.
l.sort()
print(l) # [1, 2, 4, 5]

# 10. reverse(): Reverses the order of the elements in the list.
l.reverse()
print(l) # [5, 4, 2, 1]
