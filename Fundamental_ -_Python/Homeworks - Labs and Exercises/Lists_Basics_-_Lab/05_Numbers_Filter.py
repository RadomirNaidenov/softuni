n = int(input())
numbers = []
for _ in range(n):
    current_num = int(input())
    numbers.append(current_num)

command = input()
filtered_numbers = []

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered_numbers.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered_numbers.append(num)
elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered_numbers.append(num)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered_numbers.append(num)
print(filtered_numbers)