from collections import deque

quantity_of_water = int(input())
name = input()
people = deque()

while name != "Start":
    people.append(name)

    name = input()

command = input()

while command != "End":
    data = command.split()
    if len(data) != 1:
        refill_litters = int(data[1])
        quantity_of_water += refill_litters
        command = input()
        continue

    litters_requested = int(data[0])
    person = people.popleft()

    if quantity_of_water >= litters_requested:
        print(f"{person} got water")
        quantity_of_water -= litters_requested
        command = input()
        continue

    print(f"{person} must wait")

    command = input()

print(f"{quantity_of_water} liters left")