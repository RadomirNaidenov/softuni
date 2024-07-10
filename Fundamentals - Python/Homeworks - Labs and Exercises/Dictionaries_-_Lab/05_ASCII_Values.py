# list_of_characters = input().split(", ")
# ascii_list = {}
# for character in list_of_characters:
#     ascii_character = ord(character)
#     ascii_list[character] = ascii_character
#
# print(ascii_list)

list_of_characters = input().split(", ")
ascii_list = {letter: ord(letter) for letter in list_of_characters}
print(ascii_list)


