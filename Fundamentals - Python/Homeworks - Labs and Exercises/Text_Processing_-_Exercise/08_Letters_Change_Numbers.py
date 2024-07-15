incoming_data = input().split()
total_sum = 0

for data in incoming_data:
    first_letter = data[0]
    last_letter = data[-1]
    number_in_data = int(data[1:-1])

    if first_letter.isupper():
        first_letter_position = ord(first_letter) - 64
        total_sum += number_in_data / first_letter_position

    elif first_letter.islower():
        first_letter_position = ord(first_letter) - 96
        total_sum += number_in_data * first_letter_position

    if last_letter.isupper():
        last_letter_position = ord(last_letter) - 64
        total_sum -= last_letter_position

    elif last_letter.islower():
        last_letter_position = ord(last_letter) - 96
        total_sum += + last_letter_position


print(f"{total_sum:.2f}")
