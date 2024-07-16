def adding_piece(some_info_about_pieces, some_piece_name, some_composer, some_key):
    if some_piece_name not in some_info_about_pieces.keys():
        some_info_about_pieces[some_piece_name] = {"composer": some_composer, "key": some_key}
        return f"{some_piece_name} by {some_composer} in {some_key} added to the collection!"
    else:
        return f"{some_piece_name} is already in the collection!"


def removing_piece(some_info_about_pieces, some_piece_name):
    if some_piece_name in some_info_about_pieces:
        del some_info_about_pieces[some_piece_name]
        return f"Successfully removed {some_piece_name}!"
    else:
        return f"Invalid operation! {some_piece_name} does not exist in the collection."


def changing_key(some_info_about_pieces, some_piece_name, some_new_key):
    if some_piece_name in some_info_about_pieces.keys():
        some_info_about_pieces[some_piece_name]["key"] = some_new_key
        return f"Changed the key of {some_piece_name} to {some_new_key}!"
    else:
        return f"Invalid operation! {some_piece_name} does not exist in the collection."


number_of_pieces = int(input())
info_about_pieces = {}
for piece in range(number_of_pieces):
    command = input().split("|")
    pieces_name = command[0]
    composer = command[1]
    key = command[2]
    info_about_pieces[pieces_name] = {"composer": composer, "key": key}


while True:
    command = input()

    if command == "Stop":
        break

    command = command.split("|")

    if command[0] == "Add":
        piece_name = command[1]
        composer = command[2]
        key = command[3]
        print(adding_piece(info_about_pieces, piece_name, composer, key))

    elif command[0] == "Remove":
        piece_name = command[1]
        print(removing_piece(info_about_pieces, piece_name))

    elif command[0] == "ChangeKey":
        piece_name = command[1]
        new_key = command[2]
        print(changing_key(info_about_pieces, piece_name, new_key))

for piece_name, details in info_about_pieces.items():
    print(f"{piece_name} -> Composer: {details['composer']}, Key: {details['key']}")

