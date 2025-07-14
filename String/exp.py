
s = "abcdefghijklmnopqrstuvwxyz"

# 1 extract value fourth character from the string

print(s[3])

# 2 extract value every 5th character starting from 2nd character the string

print(s[1::5])

#4 extract every 4th character from string in reverse order(with and without string inbuit function)
print(s[::-4])  # using slicing


#5 extract first 10 character and last 10 character from the string and concatenate them

print(s[:10] + s[-10:])

#6 extract character from index 7 upto (but not including) index 20 with a step of 2

print(s[7:20:2])

#7 extract entire string in reverse order excluding the first and last character

print(s[-2:0:-1])  # using slicing

# 8 extract every 3rd character from the end of the string strating from 2nd to last character

print(s[-2::-3])  # using slicing

#9 create new string by taking first 5 characters , middle 5 characteer and  last 5 characters from the string

middle_index = len(s) // 2 # output 13
new_string = s[:5] + s[middle_index - 2:middle_index + 3] + s[-5:] # output 'abcdeijklmnoxyz'
print(new_string)

