numbers_str = input().split(", ")
even_indices = []

for index, num_str in enumerate(numbers_str):
    num = int(num_str)
    if num % 2 == 0:
        even_indices.append(index)

print(even_indices)