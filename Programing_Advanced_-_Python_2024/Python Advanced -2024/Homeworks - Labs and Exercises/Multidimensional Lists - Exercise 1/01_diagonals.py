rows = int(input())
matrix = [[int(n) for n in input().split(", ")] for _ in range(rows)]
primary_diagonals = [matrix[i][i] for i in range(len(matrix))]
second_diagonal = [matrix[i][len(matrix) - i - 1] for i in range(len(matrix))]
primary_sum = sum(primary_diagonals)
second_sum = sum(second_diagonal)

print(f'Primary diagonal: {", ".join([str(x) for x in primary_diagonals])}. Sum: {primary_sum}')
print(f'Secondary diagonal: {", ".join([str(x) for x in second_diagonal])}. Sum: {second_sum}')







