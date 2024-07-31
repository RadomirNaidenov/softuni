import re
names = input().split(", ")

names_pattern = re.compile(r'[A-Za-z]')
digits_pattern = re.compile(r'\d')

runners = {name: 0 for name in names}


while True:
    command = input()
    if command == "end of race":
        break

    name_chars = names_pattern.findall(command)
    digit_chars = digits_pattern.findall(command)
    current_person_name = ''.join(name_chars)
    kilometres_run = sum(int(digit) for digit in digit_chars)

    if current_person_name in runners:
        runners[current_person_name] += kilometres_run

sorted_runners = sorted(runners.items(), key=lambda item: item[1], reverse=True)
positions = ["st", "nd", "rd"]
for counter, (name, distance) in enumerate(sorted_runners[:3], 1):
    position = positions[counter - 1]
    print(f"{counter}{position} place: {name}")

    
