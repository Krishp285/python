# bytes are used to store binary data and are immutable
# bytearray is a mutable counterpart of bytes
# memoryview provides a way to access the memory of another binary object without copying it

my_bytes = b"Hello World"
print(my_bytes)
print(type(my_bytes))
# my_bytes[0] = 72 # This would raise a TypeError as bytes are immutable


my_bytearray = bytearray(b"Hello World")
print(my_bytearray)
print(type(my_bytearray))
my_bytearray[0] = 65  # Modifying the first byte
print(my_bytearray)

data = bytearray(b"abcdefg")
mv = memoryview(data) # memory view is a view of the bytearray without copying it means it uses less memory
print(mv[0:3]) # View the first three bytes
mv[0] = ord(b'X') # Modify the underlying bytearray through the memoryview
print(data)


print(ord('H'))  # Returns 72
print(chr(72))   # Returns 'H'

# what is this used for? anwer : Converting between characters and their ASCII (or Unicode) integer representations.
sample_bytes = b"Python"
for byte in sample_bytes:
    print(byte, chr(byte))







my_set = {1, 2, 3}
my_set.add(4)  # Adding an element
my_set.remove(2) # Removing an element
print(my_set) # Output: {1, 3, 4}



my_frozenset = frozenset([1, 2, 3])
# my_frozenset.add(4) # This would raise an AttributeError as frozensets are immutable
print(my_frozenset) # Output: frozenset({1, 2, 3})

# Using a frozenset as a dictionary key
my_dict = {frozenset({1, 2}): "Value A"}
print(my_dict[frozenset({1, 2})]) # Output: Value A



