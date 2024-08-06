from collections import deque

people = deque() 
name = input()

while name != "End":

    if name != "Paid":
        people.append(name)
        name = input()
        continue
    
    while people:
        print(people.popleft())

    name = input()

print(f"{len(people)} people remaining.")
