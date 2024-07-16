def move_letter(some_number_of_letters_to_move, some_encrypted_message):
    letter_to_move = some_encrypted_message[:some_number_of_letters_to_move]
    final_message = some_encrypted_message[some_number_of_letters_to_move:] + letter_to_move
    return final_message


def insert_value(some_encrypted_message, some_given_index, some_given_value):
    final_message = some_encrypted_message[:some_given_index] +\
                             some_given_value + some_encrypted_message[some_given_index:]
    return final_message


def change_all_symbols(some_encrypted_message, some_given_substring, some_given_replacement_symbol):
    final_message = some_encrypted_message.replace(some_given_substring, some_given_replacement_symbol)
    return final_message


encrypted_message = input()

while True:
    command = input()
    if command == "Decode":
        print(f"The decrypted message is: {encrypted_message}")
        break

    command = command.split("|")

    if command[0] == "Move":
        number_of_letters_to_move = int(command[1])
        encrypted_message = move_letter(number_of_letters_to_move, encrypted_message)

    elif command[0] == "Insert":
        given_index = int(command[1])
        given_value = command[2]
        encrypted_message = insert_value(encrypted_message, given_index, given_value)

    elif command[0] == "ChangeAll":
        given_substring = command[1]
        given_replacement_symbol = command[2]
        encrypted_message = change_all_symbols(encrypted_message, given_substring, given_replacement_symbol)



