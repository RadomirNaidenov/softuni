rows, columns = [int(n) for n in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]
found_count = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current_letter = matrix[row][column]
        current_letter_beside = matrix[row][column + 1]
        current_letter_below = matrix[row + 1][column]
        current_letter_below_beside = matrix[row + 1][column + 1]

        if current_letter == current_letter_beside\
                and current_letter == current_letter_below\
                and current_letter == current_letter_below_beside:

            found_count += 1

print(found_count)



