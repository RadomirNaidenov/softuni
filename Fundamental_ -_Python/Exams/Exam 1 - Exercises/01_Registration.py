data = input()

while True:
    command = input()
    if command == "Registration":
        break

    command = command.split()

    if command[0] == "Letters":
        if command[1] == "Lower":
            data = data.lower()
        elif command[1] == "Upper":
            data = data.upper()
        print(data)

    elif command[0] == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(data) and 0 <= end_index < len(data):
            reversed_text = data[start_index:end_index + 1][:: -1]
            print(reversed_text)

        else:
            continue

    elif command[0] == "Substring":
        substring = command[1]

        if substring in data:
            print(data.replace(substring, ""))
        else:
            print(f"The username {data} doesn't contain {substring}.")

    elif command[0] == "Replace":
        replacing_data = command[1]
        new_data = data.replace(replacing_data, "-")
        print(new_data)

    elif command[0] == "IsValid":
        validate_symbol = command[1]
        if validate_symbol in data:
            print("Valid username.")
        else:
            print(f"{validate_symbol} must be contained in your username.")







