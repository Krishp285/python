
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
