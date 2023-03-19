from pprint import pprint

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
size = len(matrix)

prefix_sum = [[0] * (size + 1) for _ in range(size + 1) ]
for i in range(1, size + 1):
    for j in range(1, size + 1):
        #prefix_sum(i, j) = matrix(i, j) + prefix_sum(i - 1, j) + prefix_sum(i, j - 1) - prefix_sum(i - 1, j - 1)
        prefix_sum[i][j] = matrix[i - 1][j - 1]  + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i -1][j - 1]

for m in matrix:
    print(m)
pprint(prefix_sum)