def check_coordinates(row1, col1, row2, col2):
    if (0 <= row1 < rows and 0 <= col1 < columns and
            0 <= row2 < rows and 0 <= col2 < columns):
        return True
    return False


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

command = input()
while command != "END":
    parts = command.split()

    if len(parts) == 5 and parts[0] == "swap":

        try:
            row1, col1, row2, col2 = [int(x) for x in parts[1:]]
            is_valid = check_coordinates(row1, col1, row2, col2)
            if not is_valid:
                print("Invalid input!")
                command = input()
                continue

            matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
            for row in matrix:
                print(*row)

        except ValueError:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()

