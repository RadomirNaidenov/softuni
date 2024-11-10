painted_eggs = {
    "red": 0,
    "orange": 0,
    "blue": 0,
    "green": 0
}

for _ in range(int(input())):
    egg_color = input()
    painted_eggs[egg_color] += 1

mag_eggs_color = max(painted_eggs, key=lambda k: painted_eggs[k])
max_eggs_color_count = painted_eggs[mag_eggs_color]

result = []

for paint, count in painted_eggs.items():
    paint = paint[:1].upper() + paint[1:]
    print(f"{paint} eggs: {count}")


mag_eggs_color = max(painted_eggs, key=lambda k: painted_eggs[k])
max_eggs_color_count = painted_eggs[mag_eggs_color]

print(f"Max eggs: {max_eggs_color_count} -> {mag_eggs_color}")




