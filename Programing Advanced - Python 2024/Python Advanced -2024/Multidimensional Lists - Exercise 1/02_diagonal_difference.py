matrix_size = int(input())
matrix = [[int(x) for x in input().split(" ")] for _ in range(matrix_size)]
primary_diagonal = [matrix[i][i] for i in range(matrix_size)]
second_diagonal = [matrix[i][matrix_size - i - 1] for i in range(matrix_size)]

primary_diagonal_sum = sum(primary_diagonal)
second_diagonal_sum = sum(second_diagonal)
difference = primary_diagonal_sum - second_diagonal_sum
print(abs(difference))
