def add_number(matrix: list, row: int, col: int, value: int) -> None:
    matrix[row][col] += value
    


def sebtract_number(matrix: list, row: int, col: int, value: int) -> None:
    matrix[row][col] -= value
    


def valid_cordinates(matrix, row= int, col= int) -> bool:
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False
        

rows = int(input())
matrix = [[int(x) for x in input().split()] for row in range(rows)]

command = input()
while command != "END":
    command = command.split()

    if command[0] == "Add":
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])
        if not valid_cordinates(matrix, row, col):
            print("Invalid coordinates")
            command = input()
            continue
        add_number(matrix, row, col, value)
        
    elif command[0] == "Subtract":
        row = int(command[1])
        col = int(command[2])
        value = int(command[3])
        if not valid_cordinates(matrix, row, col):
            print("Invalid coordinates")
            command = input()
            continue
        sebtract_number(matrix, row, col, value)

    command = input()

for lst in matrix:
    print(*lst)

