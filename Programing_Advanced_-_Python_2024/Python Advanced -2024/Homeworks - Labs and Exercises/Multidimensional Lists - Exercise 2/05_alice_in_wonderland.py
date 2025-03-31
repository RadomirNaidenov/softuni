matrix_size = int(input())

matrix = []
alice_starting_point = []

for row in range(matrix_size):
    matrix.append(input().split())
    for col in range(matrix_size):
        if matrix[row][col] == "A":
            alice_starting_point = [row, col]
            matrix[row][col] = "*"

possible_moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_bags = 0

while tea_bags < 10:
    direction = input()
    move = possible_moves[direction]
    row = alice_starting_point[0] + move[0]
    col = alice_starting_point[1] + move[1]

    if row < 0 or row >= matrix_size or col < 0 or col >= matrix_size:
        break
    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break
    if matrix[row][col] not in "*.":
        tea_bags += int(matrix[row][col])
    
    matrix[row][col] = "*"
    alice_starting_point = [row, col]

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]
