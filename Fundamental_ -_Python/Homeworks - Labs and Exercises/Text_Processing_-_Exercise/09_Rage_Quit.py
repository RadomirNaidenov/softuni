data = input()
final_data = ""
sub_string = ""
repetitions = ""

for index in range(len(data)):
    if not data[index].isdigit():
        sub_string += data[index].upper()

    else:
        for next_characters in range(index, len(data)):
            if not data[next_characters].isdigit():
                break

            repetitions += data[next_characters]
        final_data += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(final_data))}")
print(final_data)




