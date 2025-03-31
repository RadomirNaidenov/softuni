rows, columns = [int(x) for x in input().split(", ")]
matrix = []
for _ in range(rows):
    numbers = [int(x) for x in input().split(" ")]
    matrix.append(numbers)

for column in range(len(matrix[0])):
    column_sum = 0
    for row in range(len(matrix)):
        column_sum += matrix[row][column]
    print(column_sum)
        





    