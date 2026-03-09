# Write a Python program to read a text file and do following: 
# 1. Print no. of words 
# 2. Print no. statements    ==> friend.txt 

# Friends are crazy, Friends are naughty !
# Friends are honest, Friends are  best !
# Friends are like keygen, friends are like license key !
# We are nothing without friends, Life is not possible without friends !

file = open("friends.txt","w")
file.write("friends are crazy , friends are naughty!\n")
file.write("friend are honest , friends are loyal!\n")
file.write("friends are like keygen , friends are like license key!\n")
file.write("we are nothing without friends ,life is not without friends!\n")
file.close()
file = open("friends.txt","r")
data = file.read()
words = data.split()
count = 0
print("Number of words:", len(words))
for i in data:
    if i == "\n":
        count += 1
print("Number of statements:", count)
file.close()



# Write a Python program to reverse the content of a one file and store it in second file and also convert content of second 
# file into uppercase and store it in third file and also count number of Vowels in third file and also print only 2nd line from 
# the content of third file.

# Examples:
# If data file one contains the following data:
# Friends are crazy, Friends are naughty !
# Friends are honest, Friends are  best !
# Output 1:
# ! tseb  era sdneirF ,tsenoh era sdneirF
# ! ythguan era sdneirF ,yzarc era sdneirF

# Output 2:
# ! TSEB  ERA SDNEIRF ,TSENOH ERA SDNEIRF
# ! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF

# Output 3:
# Vowels = 22

# Output 4:
# ! YTHGUAN ERA SDNEIRF ,YZARC ERA SDNEIRF

file1 = open("file1.txt","w")
file1.write("Friends are crazy, Friends are naughty !\n")
file1.write("Friends are honest, Friends are  best !\n")
file1.close()
file1 = open("file1.txt","r")
data = file1.readlines()
file1.close()
reversed_lines = data[::-1]
file2 = open("file2.txt","w")
for line in reversed_lines:
    file2.write(line[::-1])
file2.close()
file2 = open("file2.txt","r")
data2 = file2.readlines()
file2.close()
file3 = open("file3.txt","w")
vowel_count = 0
for line in data2:
    upper_line = line.upper()
    file3.write(upper_line)
    for char in upper_line:
        if char in "AEIOU":
            vowel_count += 1
file3.close()
file3 = open("file3.txt","r")
data3 = file3.readlines()
file3.close()
print("Vowels =", vowel_count)  
print("Second line from third file:", data3[1].strip())
