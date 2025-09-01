# 4. Problem Description: Given two names A and B as input, print "A says Hi to B", where A and B are the names in input.
# Problem Constraints
# 1 <= len(A), len(B) <= 15
# Characters in A and B are in lowercase English Alphabets.
# Input Format:
# There are two input lines
# The first line has a string A.
# The second line has a string B.
# Output Format:
# Print in a single line A says Hi to B.
# Examples
# Input:
# Ram
# Shyam
# Output:
# Ram says Hi to Shyam
a = input("Enter a :-")
b = input("Enter b :-")
print(a, end=" ")
print("says Hi to", b)
