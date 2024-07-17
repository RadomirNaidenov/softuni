country_to_stop = input()


def add_stop(some_index, some_text):
    global country_to_stop
    if some_index in range(len(country_to_stop)):
        country_to_stop = country_to_stop[:some_index] + some_text + country_to_stop[some_index:]
    else:
        return country_to_stop


def remove_stop(some_start_index, some_end_index):
    global country_to_stop
    if some_start_index in range(len(country_to_stop)) and some_end_index in range(len(country_to_stop)):
        country_to_stop = country_to_stop[:some_start_index] + country_to_stop[some_end_index + 1:]
    else:
        return country_to_stop


def switch(some_old_text, some_new_text):
    global country_to_stop
    country_to_stop = country_to_stop.replace(some_old_text, some_new_text)


while True:
    command = input()
    if command == "Travel":
        break

    command = command.split(":")

    if command[0] == "Add Stop":
        index = int(command[1])
        text = command[2]
        add_stop(index, text)

    elif command[0] == "Remove Stop":
        start_index = int(command[1])
        end_index = int(command[2])
        remove_stop(start_index, end_index)

    elif command[0] == "Switch":
        old_text = command[1]
        new_text = command[2]
        switch(old_text, new_text)

    print(country_to_stop)

print(f"Ready for world tour! Planned stops: {country_to_stop}")