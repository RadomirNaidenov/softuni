from collections import deque
numbers = input().split()
reversed_numbers = deque()
for _ in range(len(numbers)):
    reversed_numbers.append(numbers.pop())

print(" ".join(reversed_numbers))