rows_and_columns = int(input())
matrix = [[r for r in input()] for r in range(rows_and_columns)]
element = input()
is_find = False

for row in range(len(matrix)):
    for column in range(len(matrix)):
        if matrix[row][column] != element:
            continue
        elif matrix[row][column] == element:
            is_find = True
            print(f"({row}, {column})")
    if is_find:
        break

if not is_find:
    print(f"{element} does not occur in the matrix")

