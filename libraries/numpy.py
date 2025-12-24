import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0:2, 1:3]) 


 # explain slicing in 2D arrays
# Slicing in 2D arrays allows you to extract a sub-array by specifying the range of rows and columns you want to include.
# In this example, arr[0:2, 1:3] extracts rows 0 to 1 (the first two rows) and columns 1 to 2 (the second and third columns).

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(a.T) 

# import matplotlib.pyplot as plt
# sizes = [40,35,25]
# labels = ["Java","Python","C"]

# plt.pie(sizes, labels=labels, autopct="%1.1f%%")
# plt.title("Pie Chart")
# plt.show()

