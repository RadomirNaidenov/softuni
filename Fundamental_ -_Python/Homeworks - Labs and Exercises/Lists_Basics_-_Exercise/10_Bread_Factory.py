events = input().split("|")
starting_energy = 100
starting_coins = 100
bakery_is_open = True

for current_event in events:
    index = current_event.split("-")
    type_event = index[0]
    number = int(index[1])

    if type_event == "rest":
        temporary_energy = starting_energy
        starting_energy += number
        if starting_energy > 100:
            starting_energy = 100
            gained_energy = starting_energy - temporary_energy

            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {starting_energy}.")

    elif type_event == "order":
        if starting_energy >= 30:
            starting_energy -= 30
            starting_coins += number
            print(f"You earned {starting_coins} coins.")

        else:
            starting_energy += 50
            if starting_energy > 100:
                starting_energy = 100
                print("You had to rest!")

    else:
        if starting_coins >= number:
            starting_coins -= number
            print(f"You bought {type_event}.")

        else:
            print(f"Closed! Cannot afford {type_event}.")
            bakery_is_open = False
            break

if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {starting_coins}")
    print(f"Energy: {starting_energy}")








