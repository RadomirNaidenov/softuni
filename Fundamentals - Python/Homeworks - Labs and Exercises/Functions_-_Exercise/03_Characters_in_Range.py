
def returned_characters(first_srt, last_str):
    characters = []
    for current_char_as_digit in range(ord(first_srt) + 1, (ord(last_str))):
        characters.append(chr(current_char_as_digit))
    return characters


first_string = input()
last_string = input()
result = (returned_characters(first_string, last_string))
print(" ".join(result))
