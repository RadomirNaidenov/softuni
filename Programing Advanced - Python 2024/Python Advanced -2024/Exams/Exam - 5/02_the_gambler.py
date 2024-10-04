def create_and_fine_start(matrix_size: int) -> tuple[list[list], int, int]:
    matrix = []
    start_row, start_col = 0, 0
    for row in range(matrix_size):
        row_input = list(input())
        if STARTING_POSITION in row_input:
            start_row = row
            start_col = row_input.index(STARTING_POSITION)
            row_input[start_col] = EMPTY_POSITION
        matrix.append(row_input)
    
    return matrix, start_row, start_col


def valid_index(matrix: list[list[str]], row: int, col: int) -> bool:
    return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])


def display_matrix(some_matrix: list[list]) -> None:
    for row in some_matrix:
        print("".join(row))


def main(some_matrix: list[list], start_row: int, start_col: int) -> None:

    current_amount = INITIAL_AMOUNT
    win_jacpot = False
    leave_boundaries = False

    while current_amount > 0:


        direction = input()

        if direction == "end":
            break
        elif not valid_index(
            some_matrix,
            start_row + movements[direction][0],
            start_col + movements[direction][1]
        ):
            leave_boundaries = True
            break
        
        start_row += movements[direction][0]
        start_col += movements[direction][1]

        current_block = some_matrix[start_row][start_col]

        if current_block == "J":
            current_amount += JACKPOT_WIN
            some_matrix[start_row][start_col] = STARTING_POSITION
            win_jacpot = True
            break
        elif current_block == EMPTY_POSITION:
            continue
        elif current_block == PENALTY_POSITION:
            current_amount -= AMOUNT_OF_PENALTY_POSITION
        elif current_block == WELL_POSITION:
            current_amount += ADD_AMOUNT
            
        some_matrix[start_row][start_col] = EMPTY_POSITION


    some_matrix[start_row][start_col] = STARTING_POSITION

    if win_jacpot:
        print("You win the Jackpot!")
        print(f"End of the game. Total amount: {current_amount}$")
        display_matrix(some_matrix) 
    elif not win_jacpot and not leave_boundaries and current_amount >= 0:
        print(f"End of the game. Total amount: {current_amount}$")
        display_matrix(some_matrix) 
    if leave_boundaries or current_amount <= 0:
        print("Game over! You lost everything!")


STARTING_POSITION = "G"
INITIAL_AMOUNT = 100
EMPTY_POSITION = "-"
WELL_POSITION = "W"
ADD_AMOUNT = 100
PENALTY_POSITION = "P"
AMOUNT_OF_PENALTY_POSITION = 200
JACKPOT_WIN = 100000


movements = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}


main(
    *create_and_fine_start(
    int(input())
    )
)