name_of_gifts = input().split(" ")

while True:
    command = input()
    if command == "No Money":
        break

    command_part = command.split()
    action = command_part[0]
    gift = command_part[1]

    if action == "OutOfStock":
        for i in range(len(name_of_gifts)):
            if name_of_gifts[i] == gift:
                name_of_gifts[i] = "None"
    elif action == "Required":
        index = int(command_part[2])
        if 0 <= index < len(name_of_gifts):
            name_of_gifts[index] = gift
    elif action == "JustInCase":
        name_of_gifts[-1] = gift

result = (gift for gift in name_of_gifts if gift != "None")
print(" ".join(result))







