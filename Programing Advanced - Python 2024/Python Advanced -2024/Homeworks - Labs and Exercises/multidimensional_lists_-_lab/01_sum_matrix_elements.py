rows, columns = [int(x) for x in input().split(", ")]
matrix = []
total_sum = 0

for _ in range(rows):
    numbers = [int(x) for x in input().split(", ")]
    matrix.append(numbers)
    total_sum += sum(numbers)

print(total_sum)
print(matrix)

