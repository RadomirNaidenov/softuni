def type_input(some_input, current_value):
    if some_input == "int":
        return int(current_value) * 2
    elif some_input == "real":
        return f"{int(current_value) * 1.5:.2f}"
    else:
        return f"${current_value}$"


some_string = input()
value = input()
print(type_input(some_string, value))