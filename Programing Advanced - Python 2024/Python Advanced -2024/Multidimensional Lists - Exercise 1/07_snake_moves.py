rows, columns = [int(x) for x in input().split()]
snake = input()
matrix = [['' for _ in range(columns)] for _ in range(rows)]

snake_length = len(snake)
index = 0

for row in range(rows):
    if row % 2 != 0:
        for col in range(columns - 1, -1, -1):
            matrix[row][col] = snake[index % snake_length]
            index += 1
    else:
        for col in range(columns):
            matrix[row][col] = snake[index % snake_length]
            index += 1

for row in matrix:
    print("".join(row))

