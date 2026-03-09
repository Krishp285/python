import pandas as pd
s = pd.Series([1, 2, 3, 4, 5] , index=['a', 'b', 'c', 'd', 'e']) 
print(s)    # error: ValueError: Length of passed values is 5, index implies 4

s2 = pd.Series({"maths": 90, "english": 80, "science": 85})
print(s2) 

print(s2.index[0])        # Print the first index value (maths)