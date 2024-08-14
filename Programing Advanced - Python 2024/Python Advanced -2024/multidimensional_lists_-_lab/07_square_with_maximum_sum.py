import sys

rows, columns = [int(x) for x in input().split(", ")]
matrix = [[int(x) for x in input().split(", ")]for _ in range(rows)]

max_sum = -sys.maxsize
sub_matrix = None
for row_index in range(rows - 1):
    for column_index in range(columns - 1):
        first_number = matrix[row_index][column_index]
        second_number = matrix[row_index][column_index + 1]
        first_number_below = matrix[row_index + 1][column_index]
        second_number_below = matrix[row_index + 1][column_index + 1]
        current_sum = sum([first_number, second_number, first_number_below, second_number_below])

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[first_number, second_number], [first_number_below, second_number_below]]

if sub_matrix:
    print(*sub_matrix[0], sep=" ")
    print(*sub_matrix[1], sep=" ")

print(max_sum)
