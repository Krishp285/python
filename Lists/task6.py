# Write a Python program that accepts a list of integers and calculates the length and the 
# 	fifth element. Return true if the 
# 	length of the list is 8 and the fifth element occurs thrice in the said list.
# 	Input:
# 	[19, 19, 15, 5, 5, 5, 1, 2]
# 	Output:
# 	True
# 	Input:
# 	[19, 15, 5, 7, 5, 5, 2]
# 	Output:
# 	False
l = [19, 15, 5, 7, 5, 5, 2]
if len(l) == 8 and l[4] == 5 and l.count(5) == 3:
    print(True)
else:
    print(False)