matrix_size = int(input())
matrix = [list(input()) for _ in range(matrix_size)]
positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_the_most_attacks = []

    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == "K":
                attacks = 0

                for position in positions:
                    position_row = row + position[0]
                    position_col = col + position[1]

                    if 0 <= position_row < matrix_size and 0 <= position_col < matrix_size:
                        if matrix[position_row][position_col] == "K":
                            attacks += 1
                
                if attacks > max_attacks:
                    knight_with_the_most_attacks = [row, col]
                    max_attacks = attacks

    if not knight_with_the_most_attacks:
        break
        
    matrix[knight_with_the_most_attacks[0]][knight_with_the_most_attacks[1]] = "0"
    removed_knights += 1

print(removed_knights)