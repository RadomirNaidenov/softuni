data = input()
strength = 0
final_text = ""

for index in range(len(data)):
    if strength > 0 and data[index] != ">":
        strength -= 1

    elif data[index] == ">":
        strength += int(data[index + 1])
        final_text += data[index]

    else:
        final_text += data[index]

print(final_text)
