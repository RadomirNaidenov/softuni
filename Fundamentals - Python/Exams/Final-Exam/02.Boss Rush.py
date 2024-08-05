import re

number_of_inputs = int(input())
matches_list = []
for _ in range(number_of_inputs):

    command = input()
    pattern = r"\|([A-Z]+)\|\:#([A-Z-a-z]+\s[A-Z-a-z]+)#"

    matches = re.findall(pattern, command)
    matches_list.append(matches)


for match in matches_list:
    if not match:
        print("Access denied!")
        continue
    print(f"{match[0][0]}, The {match[0][1]}")
    print(f">> Strength: {len(match[0][0])}")
    print(f">> Armor: {len(match[0][1])}")