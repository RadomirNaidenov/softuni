data = input()
while True:
    if data == "end":
        break

    reversed_word = [char for char in reversed(data)]

    print(f"{data} = {''.join(reversed_word)}")
    data = input()
