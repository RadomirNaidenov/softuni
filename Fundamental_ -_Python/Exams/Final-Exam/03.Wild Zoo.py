animals = {}
area_of_the_animals = {}
command = input()
while command != "EndDay":

    action, animal_data = command.split(": ")

    if action == "Add":
        animal_name, needed_food_quantity, area = animal_data.split("-")
        needed_food_quantity = int(needed_food_quantity)
        if animal_name not in animals.keys():
            animals[animal_name] = {"food": 0, "area": area}
            if area not in area_of_the_animals:
                area_of_the_animals[area] = 0
            area_of_the_animals[area] += 1

        animals[animal_name]["food"] += needed_food_quantity
    elif action == "Feed":
        animal_name, food = animal_data.split("-")
        food = int(food)
        if animal_name not in animals.keys():
            continue

        animals[animal_name]["food"] -= food
        if animals[animal_name]["food"] > 0:
            continue

        print(f"{animal_name} was successfully fed")
        area = animals[animal_name]["area"]
        area_of_the_animals[area] -= 1
        if area_of_the_animals[area] == 0:
            del area_of_the_animals[area]
        del animals[animal_name]
        
    command = input()

print("Animals:")
for animal_name, info in animals.items():
    print(f" {animal_name} -> {info['food']}g")


if area_of_the_animals:
    print("Areas with hungry animals:")
    for area, count_of_areas in area_of_the_animals.items():
        if count_of_areas > 0:
            print(f" {area}: {count_of_areas}")