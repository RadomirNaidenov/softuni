concealed_message = input()


def insert_space(index):
    global concealed_message
    concealed_message = concealed_message[:index] + ' ' + concealed_message[index:]
    print(concealed_message)


def reverse(substring):
    global concealed_message
    if substring in concealed_message:
        occurrence = concealed_message.find(substring)
        concealed_message = concealed_message[:occurrence] + concealed_message[occurrence + (len(substring)):]
        concealed_message += substring[::-1]
        print(concealed_message)
    else:
        print("error")


def change_all(under_string, replace):
    global concealed_message
    concealed_message = concealed_message.replace(under_string, replace)
    print(concealed_message)


while True:
    command = input()
    if command == "Reveal":
        break

    command = command.split(':|:')
    action = command[0]

    if action == "InsertSpace":
        index = int(command[1])
        insert_space(index)

    elif action == "Reverse":
        substring = command[1]
        reverse(substring)

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        change_all(substring, replacement)

print(f"You have a new text message: {concealed_message}")
