n = int(input())
unique_elements = set()
for _ in range(n):
    elements = input().split()

    for element in elements:
        if element in unique_elements:
            continue
        unique_elements.add(element)

for element in unique_elements:
    print(element)