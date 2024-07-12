data = input()
char_data = ""
num_data = ""
other_data = ""
for char in data:
    if char.isdigit():
        num_data += char
    elif char.isalpha():
        char_data += char
    else:
        other_data += char

print(f"{num_data}\n{char_data}\n{other_data}")


