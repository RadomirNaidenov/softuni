number_of_symbols = int(input())

for first_index in range(97, 97 + number_of_symbols):
    for second_index in range(97, 97 + number_of_symbols):
        for third_index in range(97, 97 + number_of_symbols):
            print(f"{chr(first_index)}{chr(second_index)}{chr(third_index)} ")

