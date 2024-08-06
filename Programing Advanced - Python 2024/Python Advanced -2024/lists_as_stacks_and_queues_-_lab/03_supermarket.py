from collections import deque

people = deque()
command = input()


while command != "End":

    if command != "Paid":
        people.append(command)
        command = input()
        continue
    
    while people:
        print(people.popleft())

    command = input()

print(f"{len(people)} people remaining.")