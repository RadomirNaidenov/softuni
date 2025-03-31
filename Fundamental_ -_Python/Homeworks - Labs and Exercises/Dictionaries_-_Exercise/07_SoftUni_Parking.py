number_of_commands = int(input())
registered = {}

for _ in range(number_of_commands):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate_number = command[2]
        if username not in registered.keys():
            registered[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif command[0] == "unregister":
        username = command[1]

        if username not in registered.keys():
            print(f"ERROR: user {username} not found")

        else:
            print(f"{username} unregistered successfully")
            registered.pop(username)

for username, license_plate_number in registered.items():
    print(f"{username} => {license_plate_number}")


