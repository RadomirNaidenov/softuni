def create_matrix(matrix_size: int, starting_symbol: str, symbol_after_step: str) -> tuple[list[list[str]], int, int]:
    p_row, p_col = 0, 0
    matrix = []
    for row in range(matrix_size):
        row_input = list(input())
        if starting_symbol in row_input:
            p_row = row
            p_col = row_input.index(starting_symbol)
            row_input[p_col] = symbol_after_step
        matrix.append(row_input)
    
    return matrix, p_row, p_col


def valid_index(matrix: list[list[str]], row: int, col: int) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def main(matrix: list[list[str]], start_row: int, start_col: int) -> None:
    current_health = INITIAL_HEALTH

    while current_health > 0:
        direction = input()
        
        if not valid_index(matrix,
                       start_row + movements[direction][0],
                       start_col + movements[direction][1]
                       ):
            continue

        start_row += movements[direction][0]
        start_col += movements[direction][1]

        current_block = matrix[start_row][start_col] 

        if current_block == EXIT_FROM_MATRIX:
            break
        elif current_block == MONSTER:
            current_health -= MONSTER_DMG
            if current_health <= 0:
                current_health = 0
                continue
            
            matrix[start_row][start_col] = EMPTY_SPOT
        elif current_block == HEALTH_POTION:
            current_health = min(current_health + HEALTH_AMOUNT, MAX_HEALTH)
            matrix[start_row][start_col] = EMPTY_SPOT


    matrix[start_row][start_col] = STARTING_POSITION    

    if current_health <= 0:
        print("Player is dead. Maze over!")
    elif current_health > 0:
        print("Player escaped the maze. Danger passed!")

    print(f"Player's health: {current_health} units")

    for row in matrix:
        print("".join(row))

STARTING_POSITION = "P"
EXIT_FROM_MATRIX = "X"
MONSTER = "M"
HEALTH_POTION = "H"
EMPTY_SPOT = "-"
INITIAL_HEALTH = 100
MAX_HEALTH = 100
HEALTH_AMOUNT = 15
MONSTER_DMG = 40



movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

main(
    *create_matrix(
        int(input()),
        STARTING_POSITION,
        EMPTY_SPOT
    )
)