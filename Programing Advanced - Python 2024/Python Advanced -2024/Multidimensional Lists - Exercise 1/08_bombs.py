def bomb_explosion(row: int, col: int):
    explosion_direction = (
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1),
        (-1, -1),
        (-1, 1),
        (1, -1),
        (1, 1)
    )

    explosion_power = matrix[row][col]
    for dmg_row, dmg_col in explosion_direction:
        current_row, current_col = row + dmg_row, col + dmg_col
        if check_valid_index(current_row, current_col):
            if matrix[current_row][current_col] > 0:
                matrix[current_row][current_col] -= explosion_power
    matrix[row][col] = 0


def check_valid_index(row, col):
    if 0 <= row < matrix_size and 0 <= col < matrix_size:
        return True


def find_alive_cells():
    result = []
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] > 0:
                result.append(matrix[row][col])
    return len(result), sum(result)


matrix_size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]
bomb_positions = input().split()

for indexes in bomb_positions:
    end_index = indexes.index(",")
    row, col = int(indexes[:end_index]), int(indexes[end_index + 1])
    if matrix[row][col] > 0:
        bomb_explosion(row, col)

alive_cells, sum_of_alive_cells = find_alive_cells()
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
[print(*matrix[row], sep=' ') for row in range(matrix_size)]


