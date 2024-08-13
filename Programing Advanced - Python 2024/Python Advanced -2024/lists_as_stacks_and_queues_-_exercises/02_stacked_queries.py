from collections import deque

deque_with_numbers = []
number_of_command = int(input())

for _ in range(number_of_command):
    queries = input().split()
    action = queries[0]

    if action == "1":
        deque_with_numbers.append(int(queries[1]))
    elif action == "2":
        if deque_with_numbers:
            deque_with_numbers.pop()
    elif action == "3":
        if deque_with_numbers:
            print(max(deque_with_numbers))
    elif action == "4":
        if deque_with_numbers:  
            print(min(deque_with_numbers))

print(", ".join(str(x) for x in deque_with_numbers[::-1]))

