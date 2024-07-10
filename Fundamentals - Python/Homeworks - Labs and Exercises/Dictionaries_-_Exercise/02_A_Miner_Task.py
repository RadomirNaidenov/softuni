collect_resource = {}

while True:
    command = input()
    if command == "stop":
        break

    number = int(input())
    if command not in collect_resource:
        collect_resource[command] = number
    else:
        collect_resource[command] += number

for kay, value in collect_resource.items():
    print(f"{kay} -> {value}")
