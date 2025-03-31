data = input()
for index, char in enumerate(data):
    if char == ":":
        print(char + data[index + 1])
