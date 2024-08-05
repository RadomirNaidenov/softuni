from collections import deque

expression = input()

open_parentheses_index = []

for index in range(len(expression)):
    if expression[index] == "(":
        open_parentheses_index.append(index)

    elif expression[index] == ")":
        start_index = open_parentheses_index.pop()
        end_index = index + 1
        print(expression[start_index:end_index])