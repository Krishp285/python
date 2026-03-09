# File :- it handles basic file operations like reading, writing, and appending text files.
# Modes:
# 'r' - Read mode   : Default mode. Opens a file for reading. Raises an error if the file does not exist.
# 'w' - Write mode  : Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'a' - Append mode : Opens a file for appending. Creates a new file if it does not exist.
# 'r+' - Read and Write mode : Opens a file for both reading and writing. Raises an error if the file does not exist.
# 'b' - Binary mode : Opens a file in binary mode.
# 't' - Text mode : Default mode. Opens a file in text mode.

# write 
with open("krish.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# read
with open("krish.txt", "r") as file:
    content = file.read()
    content = file.readline()
    content = file.readlines()
    print("File Content:\n", content)

# append
with open("krish.txt", "a") as file:
    file.write("Appending a new line.\n")   