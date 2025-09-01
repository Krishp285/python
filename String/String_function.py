# Built in function of string 

s = "Hello this is python programming"
# 1. len() - Returns the length of the string.

length = len(s)
print("Length of the string:", length) # This will output: 32

# 2. str() - Converts an object to a string.
string_representation = str(123)
print("String representation of 123:", string_representation) # This will output: "123"

# 3. format() - Formats the string using placeholders.

formatted_string = "Hello, {}. Welcome to {}.".format("Alice", "Python")
print("Formatted string:", formatted_string) # This will output: "Hello, Alice. Welcome to Python."


# 4. join() - Joins elements of an iterable with the string as a separator

words = ["Hello", "world", "from", "Python"]
joined_string = " ".join(words)
print("Joined string:", joined_string)  # This will output: "Hello world from Python"


# 5. split() - Splits the string into a list based on a delimiter.

split_string = s.split(" ")
print("Split string:", split_string)  # This will output: ['Hello', 'this', 'is', 'python', 'programming']

# 6. replace() - Replaces a substring with another substring.

replaced_string = s.replace("python", "Java")
print("Replaced string:", replaced_string)  # This will output: "Hello this is Java programming"

# 7. find() - Returns the index of the first occurrence of a substring.

index_of_python = s.find("python")
print("Index of 'python':", index_of_python)  # This will output: 10

# 8. count() - Returns the number of occurrences of a substring.

count_of_is = s.count("is")
print("Count of 'is':", count_of_is)  # This will output: 2

# 9. upper() - Converts the string to uppercase.

upper_string = s.upper()
print("Uppercase string:", upper_string)  # This will output: "HELLO THIS IS PYTHON PROGRAMMING"

# 10. lower() - Converts the string to lowercase.

lower_string = s.lower()
print("Lowercase string:", lower_string)  # This will output: "hello this is python programming"


# 11. strip() - Removes leading and trailing whitespace.

stripped_string = s.strip()
print("Stripped string:", stripped_string)  # This will output: "Hello this is python programming"


# 12. startswith() - Checks if the string starts with a specified substring.

starts_with_hello = s.startswith("Hello")
print("Does the string start with 'Hello'? :", starts_with_hello)  # This will output: True

# 13. endswith() - Checks if the string ends with a specified substring.

ends_with_programming = s.endswith("programming")
print("Does the string end with 'programming'? :", ends_with_programming)  # This will output: True

# 14. isalpha() - Checks if all characters in the string are alphabetic.

is_alpha = s.isalpha()
print("Is the string alphabetic? :", is_alpha)  # This will output: False (because of spaces and 'is')

# 15. isdigit() - Checks if all characters in the string are digits.

is_digit = s.isdigit()
print("Is the string numeric? :", is_digit)  # This will output: False (because it contains letters and spaces)


# 16. isalnum() - Checks if all characters in the string are alphanumeric.

is_alnum = s.isalnum()
print("Is the string alphanumeric? :", is_alnum)  # This will output: False (because of spaces)


# 17. title() - Converts the first character of each word to uppercase.

title_string = s.title()
print("Title case string:", title_string)  # This will output: "Hello This Is Python Programming"


# 18. capitalize() - Converts the first character of the string to uppercase.

capitalized_string = s.capitalize()
print("Capitalized string:", capitalized_string)  # This will output: "Hello this is python programming"


# 19. swapcase() - Swaps the case of all characters in the string.

swapped_case_string = s.swapcase()
print("Swapped case string:", swapped_case_string)  # This will output: "hELLO THIS IS PYTHON PROGRAMMING"

# 20. zfill() - Pads the string with zeros on the left to fill a specified width.

zfilled_string = "42".zfill(5)
print("Zfilled string:", zfilled_string)  # This will output: "00042"


# 21. rstrip() - Removes trailing whitespace from the string.

rstrip_string = s.rstrip()
print("Right stripped string:", rstrip_string)  # This will output: "Hello this is python programming"


# 22. lstrip() - Removes leading whitespace from the string.

lstrip_string = s.lstrip()
print("Left stripped string:", lstrip_string)  # This will output: "Hello this is python programming"


# 23. partition() - Splits the string into three parts: the part before the separator, the separator itself, and the part after the separator.

partitioned_string = s.partition("is")
print("Partitioned string:", partitioned_string)  # This will output: ('Hello this ', 'is', ' python programming')


# 24. rfind() - Returns the index of the last occurrence of a substring.

rfind_index = s.rfind("is")
print("Last index of 'is':", rfind_index)  # This will output: 17 (the last occurrence of 'is')


# 25. rindex() - Returns the index of the last occurrence of a substring, raises an error if not found.

rindex_index = s.rindex("is")
print("Last index of 'is' using rindex:", rindex_index)  # This will output: 17 (the last occurrence of 'is')


# 26. splitlines() - Splits the string into a list of lines.

split_lines = "Hello\nthis is\nPython programming".splitlines()
print("Split lines:", split_lines)  # This will output: ['Hello', 'this is', 'Python programming']


# 27. format_map() - Formats the string using a mapping (dictionary).

mapping = {"name": "Alice", "language": "Python"}
formatted_map_string = "Hello, {name}. Welcome to {language}.".format_map(mapping)
print("Formatted string using format_map:", formatted_map_string)  # This will output: "Hello, Alice. Welcome to Python."


# 28. casefold() - Converts the string to lowercase, more aggressive than lower().

casefolded_string = s.casefold()
print("Casefolded string:", casefolded_string)  # This will output: "hello this is python programming"  


# 29. translate() - Translates characters in the string using a translation table.

translation_table = str.maketrans("aeiou", "12345")  # Example translation table
translated_string = s.translate(translation_table)
print("Translated string:", translated_string)  # This will output: "H2ll4 th3s 3s pyth4n pr4gr1mm3ng"

# 30. maketrans() - Creates a translation table for use with translate().

translation_table = str.maketrans("abc", "123")  # Example translation table
print("Translation table:", translation_table)  # This will output: {97: 49, 98: 50, 99: 51} (ASCII values of 'a', 'b', 'c' mapped to '1', '2', '3')


# 31. center() - Centers the string within a specified width, padding with spaces.

centered_string = s.center(50)
print("Centered string:", centered_string)  # This will output: "               Hello this is python programming                " (with spaces padding on both sides)


# 32. ljust() - Left-justifies the string within a specified width, padding with spaces.

left_justified_string = s.ljust(50)
print("Left justified string:", left_justified_string)  # This will output: "Hello this is python programming               " (with spaces padding on the right)


# 33. rjust() - Right-justifies the string within a specified width, padding with spaces.

right_justified_string = s.rjust(50)
print("Right justified string:", right_justified_string)  # This will output: "               Hello this is python programming" (with spaces padding on the left)

# 34. format_spec() - Formats the string using a format specification.

# Note: This is not a built-in string method, but rather a concept in Python's string formatting.
# It is used in conjunction with the format() method to specify how the string should be formatted.
# Example of format_spec usage:
formatted_spec_string = "{:>10}".format("Python")
print("Formatted with spec:", formatted_spec_string)  # This will output: "    Python" (right-aligned within 10 characters)


# 35. encode() - Encodes the string to bytes using a specified encoding.

encoded_string = s.encode('utf-8')
print("Encoded string:", encoded_string)  # This will output: b'Hello this is python programming' (bytes representation of the string)
#   # Additional string methods (some may be duplicates or similar to above):

# 36. decode() - Decodes bytes to a string using a specified encoding.

# Note: This is not a built-in string method, but rather a method of bytes objects.
# It is used to convert bytes back to a string.
decoded_string = encoded_string.decode('utf-8')
print("Decoded string:", decoded_string)  # This will output: "Hello this is python programming"


# 37. isspace() - Checks if all characters in the string are whitespace.

is_space = s.isspace()
print("Is the string whitespace? :", is_space)  # This will output: False (because it contains letters and spaces)

# 38. isprintable() - Checks if all characters in the string are printable.

is_printable = s.isprintable()
print("Is the string printable? :", is_printable)  # This will output: True (because it contains printable characters)

# 39. isidentifier() - Checks if the string is a valid identifier (variable name).

is_identifier = s.isidentifier()
print("Is the string a valid identifier? :", is_identifier)  # This will output: False (because it contains spaces and is not a valid variable name)

# 40. swapcase() - Swaps the case of all characters in the string.

swapped_case_string = s.swapcase()
print("Swapped case string:", swapped_case_string)  # This will output: "hELLO THIS IS PYTHON PROGRAMMING"

# 41. format_string() - Formats the string using a format string.

# Note: This is not a built-in string method, but rather a concept in Python's string formatting.
# It is used in conjunction with the format() method to specify how the string should be formatted.
formatted_string = "Hello, {name}. Welcome to {language}.".format(name="Alice", language="Python")
print("Formatted string using format_string:", formatted_string)  # This will output: "Hello, Alice. Welcome to Python."


# 42. rpartition() - Splits the string into three parts: the part before the last occurrence of the separator, the separator itself, and the part after the separator.

rpartitioned_string = s.rpartition("is")
print("Right partitioned string:", rpartitioned_string)  # This will output: ('Hello this ', 'is', ' python programming')



# 43. casefold() - Converts the string to lowercase, more aggressive than lower().

casefolded_string = s.casefold()
print("Casefolded string:", casefolded_string)  # This will output: "hello this is python programming"


# 44. rsplit() - Splits the string into a list from the right based on a delimiter.

rsplit_string = s.rsplit(" ", 2)  # Splitting from the right, max 2 splits
print("Right split string:", rsplit_string)  # This will output: ['Hello this is', 'python', 'programming']



# 45. isdecimal() - Checks if all characters in the string are decimal characters.

is_decimal = s.isdecimal()
print("Is the string decimal? :", is_decimal)  # This will output: False (because it contains letters and spaces)


# 46. islower() - Checks if all characters in the string are lowercase.

is_lower = s.islower()
print("Is the string lowercase? :", is_lower)  # This will output: False (because it contains uppercase letters)


# 47. isupper() - Checks if all characters in the string are uppercase.

is_upper = s.isupper()
print("Is the string uppercase? :", is_upper)  # This will output: False (because it contains lowercase letters)


# 48. istitle() - Checks if the string is in title case (first character of each word is uppercase).

is_title = s.istitle()
print("Is the string in title case? :", is_title)  # This will output: False (because not all words start with uppercase letters)


# 49. isprintable() - Checks if all characters in the string are printable.

is_printable = s.isprintable()
print("Is the string printable? :", is_printable)  # This will output: True (because it contains printable characters)


# 50. isidentifier() - Checks if the string is a valid identifier (variable name).

is_identifier = s.isidentifier()
print("Is the string a valid identifier? :", is_identifier)  # This will output: False (because it contains spaces and is not a valid variable name)


# 51. isspace() - Checks if all characters in the string are whitespace.

is_space = s.isspace()
print("Is the string whitespace? :", is_space)  # This will output: False (because it contains letters and spaces)


# 52. isalnum() - Checks if all characters in the string are alphanumeric.

is_alnum = s.isalnum()
print("Is the string alphanumeric? :", is_alnum)  # This will output: False (because it contains spaces)


# 53. isascii() - Checks if all characters in the string are ASCII characters.

is_ascii = s.isascii()
print("Is the string ASCII? :", is_ascii)  # This will output: True (because it contains only ASCII characters)


# 54. isdecimal() - Checks if all characters in the string are decimal characters.

is_decimal = s.isdecimal()
print("Is the string decimal? :", is_decimal)  # This will output: False (because it contains letters and spaces)


# 55. islower() - Checks if all characters in the string are lowercase.

is_lower = s.islower()
print("Is the string lowercase? :", is_lower)  # This will output: False (because it contains uppercase letters)


# 56. isupper() - Checks if all characters in the string are uppercase.

is_upper = s.isupper()
print("Is the string uppercase? :", is_upper)  # This will output: False (because it contains lowercase letters)


# 57. istitle() - Checks if the string is in title case (first character of each word is uppercase).

is_title = s.istitle()
print("Is the string in title case? :", is_title)  # This will output: False (because not all words start with uppercase letters)


# 58. isprintable() - Checks if all characters in the string are printable.

is_printable = s.isprintable()
print("Is the string printable? :", is_printable)  # This will output: True (because it contains printable characters)


# 59. isidentifier() - Checks if the string is a valid identifier (variable name).

is_identifier = s.isidentifier()
print("Is the string a valid identifier? :", is_identifier)  # This will output: False (because it contains spaces and is not a valid variable name)


# 60. isspace() - Checks if all characters in the string are whitespace.

is_space = s.isspace()
print("Is the string whitespace? :", is_space)  # This will output: False (because it contains letters and spaces)


# 61. isalnum() - Checks if all characters in the string are alphanumeric.

is_alnum = s.isalnum()
print("Is the string alphanumeric? :", is_alnum)  # This will output: False (because it contains spaces)


# 62. isascii() - Checks if all characters in the string are ASCII characters.

is_ascii = s.isascii()
print("Is the string ASCII? :", is_ascii)  # This will output: True (because it contains only ASCII characters)
