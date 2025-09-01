a = input("enter a character:")
if a >= 'A' and a <= 'Z':
    print(chr(ord(a) + 32))
else:
    print(chr(ord(a) - 32))
