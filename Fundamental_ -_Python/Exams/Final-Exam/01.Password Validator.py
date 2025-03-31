def make_upper(some_index):
    global password
    password = password[:index] + password[index].upper() + password[index+1:]
    return password


def make_lower(some_index):
    global password
    password = password[:index] + password[index].lower() + password[index + 1:]
    return password


def insert_char(some_index, some_char):
    global password
    password = password[:index] + char + password[index:]
    return password


def replace_char(some_char, some_value):
    global password
    if some_char in password:
        ord_char = chr(ord(char) + some_value)
        password = password.replace(char, ord_char)

    return password


def validate_password():
    global password
    is_valid = True
    if len(password) < 8:
        print("Password must be at least 8 characters long!")
        is_valid = False

    if not password.isalnum() and "_" not in password:
        print("Password must consist only of letters, digits and _!")
        is_valid = False

    if not any(letter.isupper() for letter in password):
        print("Password must consist at least one uppercase letter!")
        is_valid = False

    if not any(letter.islower() for letter in password):
        print("Password must consist at least one lowercase letter!")
        is_valid = False

    if not any(character.isdigit() for character in password):
        print("Password must consist at least one digit!")
        is_valid = False

    return is_valid


password = input()
while True:
    command = input()
    if command == "Complete":
        break

    parts = command.split()
    action = parts[0]

    if action == "Make":
        sub_action = parts[1]
        index = int(parts[2])
        if sub_action == "Upper":
            password = make_upper(index)
            print(password)
        elif parts[1] == "Lower":
            password = make_lower(index)
            print(password)

    if action == "Insert":
        index = int(parts[1])
        char = parts[2]
        password = insert_char(index, char)
        print(password)

    elif action == "Replace":
        char = parts[1]
        value = int(parts[2])
        password = replace_char(char, value)
        print(password)

    elif action == "Validation":
        validate_password()