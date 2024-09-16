import sys


def check_sum(some_rows, some_columns, some_matrix):
    max_sum = -sys.maxsize
    sub_matrix = []
    for row in range(some_rows - 2):
        for col in range(some_columns - 2):

            square = [some_matrix[row][col:col + 3] for row in range(row, row + 3)]

            current_sum = sum([num for sub_lst in square for num in sub_lst])
            if current_sum > max_sum:
                max_sum = current_sum
                sub_matrix = square

    return max_sum, sub_matrix


rows, columns = [int(n) for n in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum, sub_matrix = check_sum(rows, columns, matrix)
print(f"Sum = {max_sum}")
for numbers in sub_matrix:
    print(*numbers)






