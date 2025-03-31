def create_and_fine_start(some_matrix_size: int) -> tuple[list[list], int, int]:
    matrix = []
    start_row, start_col = 0, 0
    for row in range(some_matrix_size):
        input_row = list(input())
        if STARTING_POSITION in input_row:
            start_row = row
            start_col = input_row.index(STARTING_POSITION)
            input_row[start_col] = EMPTY_POSITION
        matrix.append(input_row)

    return matrix, start_row, start_col


def valid_index(row: int, col: int) -> bool:
    return 0 <= row < matrix_size and 0 <= col < matrix_size


def traverse_ship(row: int, col: int) -> tuple[int, int]:
    if row < 0:
        row = matrix_size - 1

    elif row >= matrix_size:
        row = 0

    if col < 0:
        col = matrix_size - 1

    elif col >= matrix_size:
        col = 0

    return row, col


def display_matrix(some_matrix: list[list]):
    for row in some_matrix:
        print("".join(row))


def main(some_matrix: list[list], start_row: int, start_col: int):
    tons = 0
    direction = input()
    has_sank = False

    while direction != "collect the nets" or tons == 20:
        start_row += movements[direction][0]
        start_col += movements[direction][1]

        if not valid_index(
                start_row,
                start_col
        ):
            start_row, start_col = traverse_ship(start_row, start_col)

        current_block = some_matrix[start_row][start_col]
        if current_block.isdigit():
            tons += int(current_block)

        if current_block == WHIRLPOOLS:
            has_sank = True
            tons = 0
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{start_row},{start_col}]")
            break

        some_matrix[start_row][start_col] = EMPTY_POSITION

        direction = input()

    if tons >= 20:
        print("Success! You managed to reach the quota!")

    elif not has_sank and tons < 20:
        tons_needed = 20 - tons
        print(f"You didn't catch enough fish and didn't reach the quota! You need {tons_needed} tons of fish more.")

    if tons:
        print(f"Amount of fish caught: {tons} tons.")

    some_matrix[start_row][start_col] = STARTING_POSITION

    if not has_sank:
        display_matrix(some_matrix)


STARTING_POSITION = "S"
WHIRLPOOLS = "W"
EMPTY_POSITION = "-"

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix_size = int(input())

main(
    *create_and_fine_start(
        matrix_size
    )
)
