def takeodd():
    odd_string = ""
    for index, char in enumerate(input_data):
        if index != 0:
            if index % 2 != 0:
                odd_string += char
    input_data = odd_string
    return input_data

def cut(given_index, given_length):
    final_index = given_index + given_length
    input_data = input_data[:given_index] + input_data[final_index:]

    return input_data


def substitute(given_substring, some_substitute):
    if given_substring not in input_data:
        return "Nothing to replace!"
    
    input_data = input_data.replace(given_substring, some_substitute)

    return input_data


input_data = input()
command = input()
while True:
    
    if command == "Done":
        break

    command = command.split(" ")
    action = command[0]


    if action == "TakeOdd":

       result = takeodd()
       print(result)


    elif action == "Cut":
        index = int(command[1])
        length = int(command[2])
        result = cut(index, length)
        print(result)



    elif action == "Substitute":
        substring = command[1]
        given_substitute = command[2]
        result = substitute(substring, given_substitute)
        print(result)
    
    command = input()

password = input_data
print(f"Your password is: {password}")