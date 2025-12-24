# task : 1 take list from user append all element in list and print odd and even element sum .
l = [1,2,3,4,5,6,7,8,9,10]
even_sum = 0
odd_sum = 0
for i in l:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Even Sum:", even_sum)
print("Odd Sum:", odd_sum)

# task  :2 take list from user append all element in list and print longest word in list
#          input : ["java", "python", "php","cpp","flutter"]
#          output :  flutter

l = ["java", "python", "php","cpp","flutter"]
longest_word = max(l, key=len)
print("Longest Word:", longest_word)
# task : 3 take list from user append all element in list and remove duplicate element in the list.
#          input : [1,2,3,4,4,5,5,6,7,8,9,9,10]
#          output : [1,2,3,4,5,6,7,8,9,10]   

l = [1,2,3,4,4,5,5,6,7,8,9,9,10]
l = list(set(l))
print(l)

# task  :4 take list from user append all element in list and print pelindorme word in list  
#          input : ["java", "python", "php","cpp","flutter","maam"]
#          output :  ['php','maam']
l = ["java", "python", "php","cpp","flutter","maam"]
palindromes = [word for word in l if word == word[::-1]]
print(palindromes)

# task  : 5 take list from user append all element in list and print pelindorme num in list 
 
#          input : [121 , 131 , 123 ,145 , 789 ]
#          output :  [121,131]

l = [121 , 131 , 123 ,145 , 789 ]
palindrome_numbers = [num for num in l if str(num) == str(num)[::-1]]
print(palindrome_numbers)

# task  : 6 Write a Python program to count the number of strings from a given list of strings. 
# 	The string length is 2 or more and the first and last characters are the same.
	
# 	Sample List : ['abc', 'xyz', 'aba', '1221']
# 	Expected Result : 2

l = ['abc', 'xyz', 'aba', '1221']
count = sum(1 for s in l if len(s) >= 2 and s[0] == s[-1])
print(count)
# task : 7 Write a Python program to get the second largest number from a list.
# 	input  : [1,2,3,4,10,9,6,7]
# 	output : 9
l = [1,2,3,4,10,9,6,7]
l = list(set(l))  # Remove duplicates
l.sort()
print(l[-2])  # Second largest element

# task : 8 
# 	Write a Python program to find a list of integers with exactly two occurrences of nineteen
# 	 and at least three occurrences of five.  count 
# 	Return True otherwise False.
# 	Input:
# 	[19, 19, 15, 5, 3, 5, 5, 2]
# 	Output:
# 	True
# 	Input:
# 	[19, 15, 15, 5, 3, 3, 5, 2]
# 	Output:
# 	False
# 	Input:
# 	[19, 19, 5, 5, 5, 5, 5]
# 	Output:
# 	True

l = [19, 19, 15, 5, 3, 5, 5, 2]
if l.count(19) == 2 and l.count(5) >= 3:
    print(True)
else:
    print(False)

# task : 9 
# 	Write a Python program that accepts a list of integers and calculates the length and the 
# 	fifth element. Return true if the 
# 	length of the list is 8 and the fifth element occurs thrice in the said list.
# 	Input:
# 	[19, 19, 15, 5, 5, 5, 1, 2]
# 	Output:
# 	True
# 	Input:
# 	[19, 15, 5, 7, 5, 5, 2]
# 	Output:
# 	False

l = [19, 19, 15, 5, 5, 5, 1, 2]
if len(l) == 8 and l.count(l[4]) == 3:
    print(True)
else:
    print(False)

# task  : 10 
# 	Write a Python program to find the length of a given list of non-empty strings.
# 	Input:
# 	['cat', 'car', 'fear', 'center']
# 	Output:
# 	[3, 3, 4, 6]
# 	Input:
# 	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# 	Output:
# 	[3, 3, 7, 5, 2, 4, 0]

l = ['cat', 'car', 'fear', 'center']
lengths = [len(s) for s in l]
print(lengths)
# task  : 11 Write a Python program to check, for each string in a given list, whether the 
# last character is an isolated letter or not. 
# Return True otherwise False.
# Input:
# ['cat', 'car', 'fear', 'center']
# Output:
# [False, False, False, False]
# Input:
# ['ca t', 'car', 'fea r', 'cente r']
# Output:
# [True, False, True, True]

l = ['ca t', 'car', 'fea r', 'cente r']
result = [s[-1] == ' ' or s[-2] == ' ' if
            len(s) > 1 else False for s in l]
print(result)

# task : 12 
# Write a Python program to find strings in a given list containing a given substring.
# Input:
# [(ca,('cat', 'car', 'fear', 'center'))]
# Output:
# ['cat', 'car']
# Input:
# [(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# ['dog', 'donut', 'todo']
# Input:
# [(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
# Output:
# []

l = ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
substring = 'o'
filtered_strings = [s for s in l if substring in s]
print(filtered_strings)

# task  : 13 
# Write a Python program to find the length of a given list of non-empty strings.
# 	Input:
# 	['cat', 'car', 'fear', 'center']
# 	Output:
# 	[3, 3, 4, 6]
# 	Input:
# 	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
# 	Output:
# 	[3, 3, 7, 5, 2, 4, 0]

l = ['cat', 'car', 'fear', 'center']
lengths = [len(s) for s in l]   
print(lengths)
