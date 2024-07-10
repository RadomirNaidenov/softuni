number_of_string = int(input())
for current_strings in range(number_of_string):
    current_string = input()
    if "," in current_string or \
            "." in current_string or \
            "_" in current_string:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")