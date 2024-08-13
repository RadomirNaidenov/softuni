matrix_size = int(input())
matrix = []
primary_diagonal_sum = 0
for i in range(matrix_size):
    matrix.append([int(x) for x in input().split()])
    primary_diagonal_sum += matrix[i][i]

print(primary_diagonal_sum)

