def return_decipher(secret_massage):

    final_list = []
    for current_massage in secret_massage:
        characters = [char for char in current_massage if not char.isdigit()]
        numbers = [num for num in current_massage if num.isdigit()]

        ascii_characters = [chr(int("".join(numbers)))]
        current_word = ascii_characters + characters

        current_word[1], current_word[-1] = current_word[-1], current_word[1]
        final_list.append("".join(current_word))


    return " ".join(final_list)


secret_massage = input().split()
print(return_decipher(secret_massage))

