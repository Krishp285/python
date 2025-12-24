# 1.Make a Python program to convert first occurrences of "h" into uppercase in given string. 
s = "hello world, how are you"
s = s.replace("h", "H", 1)
print(s)

# 2.Write a program in Python that asks 2 strings from the user and interchanges first 3 characters 
# of both the strings.
# eg:
# input strings:
# color
# full
# Output:
# fulor
# coll

s1 = "color"
s2 = "full"
s1 = s1[0:3] + s2[3:]
s2 = s2[0:3] + s1[3:]
print(s1)
print(s2)

# 3.Write a Python code that prints the index numbers of all the occurrences of "o" in a given string . 

# 	input string : "i am going to goa next month."
# 	output  :     first "o" index number is  : 6 
# 		      2nd  "o"  index number is : 12
# 		      3rd  "o"  index number is  :15 
# 		      4 th "o"  index number is  :18
# 		      5 th "o"  index number is  :27

s = "i am going to goa next month."
for i in range(len(s)):
    if s[i] == 'o':
        print(f'"o" found at index: {i}')

# 4.Write a Python code that asks a string from user and replace the first occurance of " " with "_" and last occurance of " " with "#".'''
# input string: Keep yourself mute while not speaking.
# output: Keep_yourself mute while not#speaking.

s = "Keep yourself mute while not speaking."
s  = s.replace(" ","_",1)
s = s[::-1].replace(" ","#",1)[::-1]
print(s)

# 5.Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is'''
# input: dishant dipakkuamr shah
# output: d.d.shah
s = "dishant dipakkuamr shah"
names = s.split()
for i in range(len(names)-1):
    names[i] = names[i][0] + '.'
abbreviated_name = ''.join(names)
print(abbreviated_name)

# 6.Write a program to make a new string with the word "the" deleted in the given string.
# input string: This is the lion in the cage.
# output: This is lion in cage.
s = "This is the lion in the cage."
s = s.replace(" the", "")
print(s)

# 7.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

s = "restart"
s = s[::-1].replace(s[0], "$", 1)[::-1]
print(s)
 
# 8.Write a program that takes a string input and outputs the reverse of the string using slicing.
# Input:- Dishant Shah
# Output:- hahS tnahsiD	
s = "Dishant Shah"
s = s[::-1]
print(s)

# 9. 
# Write a python program that take one input string and in output count the no of words,
# Find No of letters in String,Find the longest word in the String.
# For Example:-
# Input:-This is the python program
# Output:-No of Words=5
# 	    No of letters=26(including whitespace)
# 	    Longest Word=program

s = "This is the python program"
words = s.split()
print("No of Words =", len(words))
print("No of letters =", len(s))
longest_word = max(words, key=len)
print("Longest Word =", longest_word)