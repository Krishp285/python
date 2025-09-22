a = [[1,2,3],[4,5,6],[7,8,9]]
rows = len(a)
cols = len(a[0])

row_sums = []
for i in range(rows):
    current_row_sum = 0
    for j in range(cols):
        current_row_sum += a[i][j]
    row_sums.append(current_row_sum)
print(row_sums)

col_sums = []
for j in range(cols):
    current_col_sum = 0
    for i in range(rows):
        current_col_sum += a[i][j]
    col_sums.append(current_col_sum)

print(col_sums)