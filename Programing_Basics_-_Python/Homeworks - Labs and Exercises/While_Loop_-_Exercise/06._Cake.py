length_cake = int(input())
width_cake = int(input())
command = input()
cake_size = length_cake * width_cake
cake_parts_left = cake_size
while command != "STOP":
    current_parts = int(command)
    cake_parts_left -= current_parts
    if cake_parts_left < 0:
        break

    command = input()

if command == "STOP":
    print(f"{cake_parts_left} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_parts_left)} pieces more.")

