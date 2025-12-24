# text = open("sample.txt", "a")
# text.write("Mango banana apple pear Banana grapes strawberry Apple pear mango banana Kiwi apple mango strawberry")
# text.write("\nThis is a new line added to the file.")
# text.write("\nEnd of file.")
# text.close()

lines = open("sample.txt", "r")
count = 0
for line in lines:
    count+=1
    print(line)
lines.close()
print(f"Total number of lines: {count}")

words = open("sample.txt", "r")
word_count = 0
d = {}
for line in words:
    word_list = line.split()
    word_count += len(word_list)
    for word in word_list:
        word = word.lower()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
words.close()
print(f"Total number of words: {word_count}")
print(f"Word frequency: {sum(d.values())}")



data = bytearray([65, 66, 67])  # A, B, C in ASCII

f = open("sample.bin", "wb")   # open in binary write mode
f.write(data)
f.close()

f = open("sample.bin", "rb") 
print(f.read())
f.close()