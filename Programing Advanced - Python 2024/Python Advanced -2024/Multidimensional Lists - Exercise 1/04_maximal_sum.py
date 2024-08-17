import sys


def check_sum(some_rows, some_columns, some_matrix):
    max_sum = -sys.maxsize
    sub_matrix = []
    for row in range(rows - 2):
        for col in range(columns - 2):
            first_number_in_a_row = matrix[row][col]
            second_number_in_a_row = matrix[row][col + 1]
            third_number_in_a_row = matrix[row][col + 2]

            first_number_in_a_second_row = matrix[row + 1][col]
            second_number_in_a_second_row = matrix[row + 1][col + 1]
            third_number_in_a_second_row = matrix[row + 1][col + 2]

            first_number_in_a_third_row = matrix[row + 2][col]
            second_number_in_a_third_row = matrix[row + 2][col + 1]
            third_number_in_a_third_row = matrix[row + 2][col + 2]

            current_sum = first_number_in_a_row + \
                second_number_in_a_row + \
                third_number_in_a_row + \
                first_number_in_a_second_row + \
                second_number_in_a_second_row + \
                third_number_in_a_second_row + \
                first_number_in_a_third_row + \
                second_number_in_a_third_row + \
                third_number_in_a_third_row

            if current_sum > max_sum:
                max_sum = current_sum
                sub_matrix = [
                    [first_number_in_a_row, second_number_in_a_row, third_number_in_a_row],
                    [first_number_in_a_second_row, second_number_in_a_second_row, third_number_in_a_second_row],
                    [first_number_in_a_third_row, second_number_in_a_third_row, third_number_in_a_third_row]
                ]

    return max_sum, sub_matrix


rows, columns = [int(n) for n in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_sum, sub_matrix = check_sum(rows, columns, matrix)
print(f"Sum = {max_sum}")
for row in sub_matrix:
    print(" ".join(map(str, row)))






