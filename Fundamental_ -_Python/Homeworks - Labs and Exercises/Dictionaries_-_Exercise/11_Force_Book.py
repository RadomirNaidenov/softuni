user_and_side = {}

while True:
    command = input()
    if command == "Lumpawaroo":
        break

    if " | " in command:
        side, user = command.split(" | ")
        if side not in user_and_side.keys():
            user_and_side[side] = []
            if user not in user_and_side.values():
                user_and_side[side].append(user)

    elif " -> " in command:
        user, side = command.split(" -> ")
        for list_of_force_side in user_and_side.values():
            if user in list_of_force_side:
                list_of_force_side.remove(user)
                break

        if side not in user_and_side.keys():
            user_and_side[side] = []
        user_and_side[side].append(user)
        print(f"{user} joins the {side} side!")


for side, users in user_and_side.items():
    if users:
        print(f"Side: {side}, Members: {len(users)}")
    for user in users:
        print(f"! {user}")








