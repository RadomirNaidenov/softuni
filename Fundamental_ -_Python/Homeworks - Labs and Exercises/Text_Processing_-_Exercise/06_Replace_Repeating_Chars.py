data = input()

for index, letter in enumerate(range(len(data) - 1), 1):
    if data[letter] != data[index]:
        print(data[letter], end="")

print(data[-1])
