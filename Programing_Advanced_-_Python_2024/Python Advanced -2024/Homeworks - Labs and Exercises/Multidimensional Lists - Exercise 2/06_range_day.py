MATRIX_SIZE = 5

matrix = []
starting_position = []
targets = 0

for row in range(MATRIX_SIZE):
    matrix.append(input().split())
    for col in range(MATRIX_SIZE):
        if matrix[row][col] == "A":
            starting_position = [row, col]
        elif matrix[row][col] == "x":
            targets += 1

possible_directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

targets_hit = []
n_commands = int(input())

for _ in range(n_commands):
    command = input().split()
    action = command[0]
    direction = command[1]
    
    if action == "shoot":
        row = starting_position[0] + possible_directions[direction][0]
        col = starting_position[1] + possible_directions[direction][1]
        while 0 <= row < MATRIX_SIZE and 0 <= col < MATRIX_SIZE:
            if matrix[row][col] == "x":
                matrix[row][col] = "." 
                targets -= 1
                targets_hit.append([row, col]) 
                break 
            row += possible_directions[direction][0]
            col += possible_directions[direction][1]
        
        if targets == 0:
            print(f"Training completed! All {len(targets_hit)} targets hit.")
            break

    elif action == "move":
        steps = int(command[2])
        new_row = starting_position[0] + possible_directions[direction][0] * steps
        new_col = starting_position[1] + possible_directions[direction][1] * steps

        if 0 <= new_row < MATRIX_SIZE and 0 <= new_col < MATRIX_SIZE and matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = "A"
            matrix[starting_position[0]][starting_position[1]] = "."
            starting_position = [new_row, new_col]  

if targets > 0:
    print(f"Training not completed! {targets} targets left.")
[print(row) for row in targets_hit]

