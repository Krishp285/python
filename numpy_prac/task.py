import numpy as np
# NumPy Practice Questions (Medium Level)
# 1. Array Creation
# Create a NumPy array of numbers from 1 to 20. Then print its size.

a = np.arange(1, 21)
print(a.size)

# 2. Zeros & Ones
# Create:

# a 3×4 array filled with zeros
zeros_array = np.zeros((3, 4))
print(zeros_array)

# a 2×5 array filled with ones

ones_array = np.ones((2, 5))
print(ones_array)

# 3. Full Function
# Create a 4×4 array where every value is 7 using NumPy.

full_array = np.full((4, 4), 7)
print(full_array)

# 4. Reshape
# Create an array from 1 to 12 and reshape it into:

# 3×4
array_3x4 = np.arange(1, 13).reshape((3, 4))
print(array_3x4)

# 2×6
array_2x6 = np.arange(1, 13).reshape((2, 6))
print(array_2x6)

# 5. Flatten
# Take a 3×3 matrix and convert it into a 1D array using flatten.

matrix_3x3 = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
flattened_array = matrix_3x3.flatten()

# 6. Arrange (arange)
# Create an array starting from 10 to 50 with a step of 5.
arange_array = np.arange(10, 51, 5)
print(arange_array)

# 7. Sum of Elements
# Given array:
# [10, 20, 30, 40, 50]
# Find:

# total sum
total_sum = np.sum([10, 20, 30, 40, 50])
print(total_sum)

# sum of first 3 elements only
sum_first_3 = np.sum([10, 20, 30])
print(sum_first_3)

# 8. Matrix Addition
# Add the following two arrays:

# A = [[1,2,3],
#      [4,5,6]]


# B = [[6,5,4],
#      [3,2,1]]
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[6, 5, 4],
              [3, 2, 1]])
matrix_sum = A + B
print(matrix_sum)

# 9. Matrix Subtraction
# Subtract array B from array A (from Q8).

matrix_diff = A - B
print(matrix_diff)

# 10. Element-wise Multiplication
# Multiply arrays A and B element by element.

elementwise_product = A * B
print(elementwise_product)

# 11. Mean
# Find the mean of:
# [12, 15, 20, 25, 30]

mean_value = np.mean([12, 15, 20, 25, 30])
print(mean_value)
# 12. Median
# Find the median of:
# [5, 2, 9, 1, 7, 6]
median_value = np.median([5, 2, 9, 1, 7, 6])
print(median_value)

# 13. Standard Deviation
# Find the standard deviation of:
# [4, 8, 6, 5, 3, 7]

std_dev = np.std([4, 8, 6, 5, 3, 7])
print(std_dev)

# 14. Row-wise Sum
# Given matrix:

# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]


# Find sum of each row separately.
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
row_sums = np.sum(matrix, axis=1)
print(row_sums)

# 15. Column-wise Sum
# Using the same matrix from Q14, find sum of each column.
column_sums = np.sum(matrix, axis=0)
print(column_sums)

# 16. Reshape + Mean
# Create numbers from 1 to 16, reshape into 4×4, then find the mean of each row.

array_1_to_16 = np.arange(1, 17).reshape((4, 4))
row_means = np.mean(array_1_to_16, axis=1)
print(row_means)

# 17. Flatten + Size
# Create a 5×5 ones matrix. Flatten it and find its size.

ones_matrix = np.ones((5, 5))
flattened_ones = ones_matrix.flatten()
print(flattened_ones.size)

# 18. Arithmetic Combination
# Given:
# A = [1,2,3,4]
# B = [5,6,7,8]

# Compute:
# (A + B) * 2

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])
result = (A + B) * 2
print(result)

# 19. Mixed Operations
# Create array from 1–9, reshape to 3×3. Multiply entire matrix by 5 and then find total sum.

array_1_to_9 = np.arange(1, 10).reshape((3, 3))
multiplied_array = array_1_to_9 * 5
total_sum_after_mult = np.sum(multiplied_array)
print(total_sum_after_mult)

# 20. Statistics Combo
# Given:
# [15, 18, 21, 24, 27, 30]

# Find:

# mean

mean_value = np.mean([15, 18, 21, 24, 27, 30])
print(mean_value)

# median
median_value = np.median([15, 18, 21, 24, 27, 30])
print(median_value)

# standard deviation
std_dev = np.std([15, 18, 21, 24, 27, 30])
print(std_dev)

# ----------------------------------------------------------
# hard

# 1. Advanced Reshape + Sum

# Create an array from 1 to 48.
# Reshape it into 4 × 4 × 3.
# Find:

# sum along axis 0
array_1_to_48 = np.arange(1, 49).reshape((4, 4, 3))
sum_axis_0 = np.sum(array_1_to_48, axis=0)
print("Sum along axis 0:")
print(sum_axis_0)

# sum along axis 1
sum_axis_1 = np.sum(array_1_to_48, axis=1)
print("Sum along axis 1:")
print(sum_axis_1)

# sum along axis 2
sum_axis_2 = np.sum(array_1_to_48, axis=2)
print("Sum along axis 2:")
print(sum_axis_2)


# 2. Conditional Replacement

# Create array from 1 to 20.
# Replace all numbers:

# divisible by 3 → -1

# divisible by 5 → 100

# (Do it using NumPy, not loops.)

array_1_to_20 = np.arange(1, 21)
array_1_to_20[(array_1_to_20 % 3 == 0)] = -1
array_1_to_20[(array_1_to_20 % 5 == 0)] = 100
print(array_1_to_20)

# 3. Broadcasting Math

# Given:

# A = np.array([[1,2,3],
#               [4,5,6],
#               [7,8,9]])


# B = np.array([10,20,30])

# Add B to every row of A using broadcasting.

A = np.array([[1, 2, 3],
              [4, 5, 6],
                [7, 8, 9]])
B = np.array([10, 20, 30])
result = A + B
print(result)

# 4. Flatten vs Ravel Logic

# Create a 3×3 matrix.
# Use ravel() to flatten and modify the first element.
# Then check whether original array changes.
# Explain why.

matrix_3x3 = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])
flattened_ravel = matrix_3x3.ravel()
flattened_ravel[0] = 100
print("Original matrix after modifying ravel:")
print(matrix_3x3)

#due to  same memory reference


# 5. Indexing Challenge

# Create array 1–25 and reshape to 5×5.
# Extract:

# middle row

# last column

# corner elements only

array_1_to_25 = np.arange(1, 26).reshape((5, 5))
middle_row = array_1_to_25[2, :]    
print("Middle row:")
print(middle_row)
last_column = array_1_to_25[:, 4]
print("Last column:")
print(last_column)
corner_elements = np.array([array_1_to_25[0, 0], array_1_to_25[0, 4], array_1_to_25[4, 0], array_1_to_25[4, 4]])
print("Corner elements:")
print(corner_elements)
# 6. Statistical Axis Problem

# Given:

# arr = np.array([[10,20,30],
#                 [40,50,60],
#                 [70,80,90]])

# Find:

# mean of each column

# standard deviation of each row

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
mean_columns = np.mean(arr, axis=0)
print("Mean of each column:")
print(mean_columns)
std_rows = np.std(arr, axis=1)
print("Standard deviation of each row:")
print(std_rows)


# 7. Matrix Arithmetic Combo

# Create two random 3×3 arrays.
# Compute:

# (A + B) * 2 - A


A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
result = (A + B) * 2 - A
print("Result of (A + B) * 2 - A:")
print(result)

# 8. Pattern Matrix

# Create this matrix using NumPy only:

# [[1,0,1,0],
#  [0,1,0,1],
#  [1,0,1,0],
#  [0,1,0,1]]

# (No manual typing.)


matrix_pattern = np.zeros((4, 4), dtype=int)
matrix_pattern[::2, ::2] = 1
matrix_pattern[1::2, 1::2] = 1
print(matrix_pattern)

# 9. 3D Array Stats

# Create array from 1–27 and reshape to 3×3×3.
# Find:

# overall mean

# mean along axis 0

# median of entire array
array_1_to_27 = np.arange(1, 28).reshape((3, 3, 3))
overall_mean = np.mean(array_1_to_27)
print("Overall mean:")
print(overall_mean)
mean_axis_0 = np.mean(array_1_to_27, axis=0)
print("Mean along axis 0:")
print(mean_axis_0)
median_value = np.median(array_1_to_27)
print("Median of entire array:")
print(median_value)

# 10. Multi-step Transformation

# Create array from 1–16.
# Steps:

# Reshape to 4×4

# Multiply each column by [1,2,3,4]

# Flatten result

# Find standard deviation


array_1_to_16 = np.arange(1, 17).reshape((4, 4))
column_multiplier = np.array([1, 2, 3, 4])
transformed_array = array_1_to_16 * column_multiplier
flattened_result = transformed_array.flatten()
std_dev = np.std(flattened_result)
print("Standard deviation of the final result:")
print(std_dev)
