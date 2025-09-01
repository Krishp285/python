# task :1 Write a Python program to find a list of integers with exactly two occurrences of nineteen
# 	 and at least three occurrences of five.  count 
# 	Return True otherwise False.
# 	Input:
# 	[19, 19, 15, 5, 3, 5, 5, 2]
# 	Output:
# 	True
# 	Input:
# 	[19, 15, 15, 5, 3, 3, 5, 2]
# 	Output:
# 	False

l = [19, 19, 15, 5, 3, 5, 5, 2]
if l.count(19) == 2 and l.count(5) >= 3:
    print(True)
else:
    print(False)