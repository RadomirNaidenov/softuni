wagons_count = int(input())
train = [0] * wagons_count

while True:
    command = input().split()

    if command[0] == "End":
        print(train)
        break

    elif command[0] == "add":
        number_of_people = int(command[1])
        train[-1] += number_of_people

    elif command[0] == "insert":
        given_index = int(command[1])
        number_of_people = int(command[2])
        train[given_index] += number_of_people

    elif command[0] == "leave":
        given_index = int(command[1])
        number_of_people = int(command[2])
        train[given_index] -= number_of_people



