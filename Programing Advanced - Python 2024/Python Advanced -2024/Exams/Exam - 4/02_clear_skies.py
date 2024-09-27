def create_matrix_and_find_start(size: int) -> tuple[list[list[str]], int, int]:
    matrix = []
    start_row, start_col = 0, 0
    some_enemies = 0
    for row in range(size):
        row_input = list(input())
        if STARTING_POSITION in row_input:
            start_row = row
            start_col = row_input.index(STARTING_POSITION)
            row_input[start_col] = EMPTY_SPOT
        
        if ENEMY_AIRCRAFT in row_input:
            some_enemies += row_input.count(ENEMY_AIRCRAFT)

        matrix.append(row_input)
    
    return matrix, start_row, start_col, some_enemies

def display_matrix(some_matrix):
    for row in some_matrix:
        print("".join(row))

def main(matrix: list[list[str]], start_row: int, start_col: int, some_enemies: int) -> None:
    current_armor = RESTORE_ARMOR
    final_state = []


    while current_armor > 0 and some_enemies:

        direction = input()

        start_row += movements[direction][0]
        start_col += movements[direction][1]

        current_block = matrix[start_row][start_col]

        if current_block == EMPTY_SPOT:
            continue
        if current_block == REPAIR_POINTS:
            current_armor = RESTORE_ARMOR
            matrix[start_row][start_col] = EMPTY_SPOT
        if current_block == ENEMY_AIRCRAFT:
            some_enemies -= 1
            matrix[start_row][start_col] = EMPTY_SPOT
            if some_enemies:
                current_armor -= TAKE_DMG

    if not some_enemies:
        print("Mission accomplished, you neutralized the aerial threat!")
    if current_armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates {final_state}!")
    
    matrix[start_row][start_col] = STARTING_POSITION
    display_matrix(matrix)


STARTING_POSITION = "J"
ENEMY_AIRCRAFT = "E"
REPAIR_POINTS = "R"
EMPTY_SPOT = "-"
INITIAL_ARMOR = 300
RESTORE_ARMOR = 300
TAKE_DMG = 100

movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix_size = int(input())

main(
    *create_matrix_and_find_start(matrix_size)
)