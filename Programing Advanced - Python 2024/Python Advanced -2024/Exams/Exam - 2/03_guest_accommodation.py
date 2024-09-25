def accommodate(*args, **kwargs):
    sorted_rooms = sorted(kwargs, key=lambda room: int(room.split("_")[1]))
    accommodated_rooms = {}
    for group in args:
        not_best_fit_room = ""
        for room in sorted_rooms:
            if room in accommodated_rooms:
                continue
            if kwargs[room] == group:
                accommodated_rooms[room] = group
                break
            if kwargs[room] > group:
                not_best_fit_room = room 
        else:
            if not_best_fit_room:
                accommodated_rooms[not_best_fit_room] = group

    output = []    
    if not accommodated_rooms:
        output.append("No accommodations were completed!")
    else:
        output.append(f"A total of {len(accommodated_rooms)} accommodations were completed!")
        for room in sorted_rooms:
            if room in accommodated_rooms:
                output.append(f"<Room {room.split('_')[1]} accommodates {accommodated_rooms[room]} guests>")

    total_guests = sum(args)
    total_accommodated_guests = sum(accommodated_rooms.values())
    if total_guests != total_accommodated_guests:
        output.append(f"Guests with no accommodation: {total_guests - total_accommodated_guests}")
    

    if len(kwargs) != len(accommodated_rooms):
        output.append(f"Empty rooms: {len(kwargs) - len(accommodated_rooms)}")

    return "\n".join(output)

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))