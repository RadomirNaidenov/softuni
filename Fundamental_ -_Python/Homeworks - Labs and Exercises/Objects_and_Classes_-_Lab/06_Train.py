class Train:

    def __init__(self, number_of_wagons):
        self.wagons = [0] * number_of_wagons

    def add_people(self, people):
        self.wagons[-1] += people

    def insert_people(self, insert_index, people):
        self.wagons[insert_index] += people

    def leave_people(self, leave_index, people):
        self.wagons[leave_index] -= people

    def __str__(self):
        return str(self.wagons)


def main_function():
    number_of_wagons = int(input())
    train = Train(number_of_wagons)


    while True:
        command = input()

        if command == "End":
            break

        command_parts = command.split()
        current_action = command_parts[0]

        if current_action == "add":
            people = int(command_parts[1])
            train.add_people(people)

        elif current_action == "insert":
            insert_index = int(command_parts[1])
            people = int(command_parts[2])
            train.insert_people(insert_index, people)

        elif current_action == "leave":
            leave_index = int(command_parts[1])
            people = int(command_parts[2])
            train.leave_people(leave_index, people)

    print(train)

main_function()



