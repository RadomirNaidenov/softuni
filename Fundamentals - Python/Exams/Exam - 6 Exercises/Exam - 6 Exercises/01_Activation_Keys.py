def contains(substring):
    if substring in input_data:
        return f"{input_data} contains {substring}"
    return "Substring not found!"

def flip(lower_or_upper, start_index, end_index):
    global input_data

    right_part = input_data[:start_index]
    changing_part = input_data[start_index:end_index]
    left_part = input_data[end_index:]

    if lower_or_upper == "Upper":
        changing_part = changing_part.upper()
    elif lower_or_upper == "Lower":
        changing_part = changing_part.lower()

    input_data = right_part + changing_part + left_part
    return input_data
    



def slice_str(start_index, end_index):
    global input_data
    input_data = input_data[:start_index] + input_data[end_index:]
    return input_data


input_data = input().strip()

while True:

    command = input()

    if command == "Generate":
        break

    parts = command.split(">>>")
    action = parts[0]


    if action == "Contains":
        substring = parts[1]
        result = contains(substring)
        print(result)

    elif action == "Flip":
        lower_or_upper = parts[1]
        start_index = int(parts[2])
        end_index = int(parts[3])
        result = flip(lower_or_upper, start_index, end_index)
        print(result)

    elif action == "Slice":
        start_index = int(parts[1]) 
        end_index = int(parts[2])
        result = slice_str(start_index, end_index)
        print(result)

activation_key = input_data
print(f"Your activation key is: {activation_key}")