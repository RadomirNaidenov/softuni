presents = int(input())

matrix_size = int(input())

matrix = []
santa = []
nice_kids = 0
nice_kids_gifted = 0

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == "S":
            santa = [row, col]
        elif matrix[row][col] == "V":
            nice_kids += 1

possible_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break

    row, col = santa[0] + possible_directions[command][0], santa[1] + possible_directions[command][1]
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        if matrix[row][col] == "V":
            presents -= 1
            nice_kids_gifted += 1
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            for direction in possible_directions.values():
                next_row, next_col = row + direction[0], col + direction[1]
                if matrix[next_row][next_col] in ["V", "X"] and presents > 0:
                    presents -= 1
                    if matrix[next_row][next_col] == "V":
                        nice_kids_gifted += 1
                    matrix[next_row][next_col] = "-"
        matrix[santa[0]][santa[1]] = "-"
        santa = [row, col]
        matrix[row][col] = "S"

if presents < 1 and nice_kids - nice_kids_gifted > 0:
    print("Santa ran out of presents!")

for row in matrix:
    print(*row)

if nice_kids - nice_kids_gifted > 0:
    kids_left = nice_kids - nice_kids_gifted
    print(f"No presents for {kids_left} nice kid/s.")
else:
    print(f"Good job, Santa! {nice_kids_gifted} happy nice kid/s.")