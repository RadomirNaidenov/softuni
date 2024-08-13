number_of_matrix = int(input())
matrix = []
for _ in range(number_of_matrix):
    numbers = [int(x) for x in input().split(", ") if int(x) % 2 == 0]
    matrix.append(numbers)

print(matrix)