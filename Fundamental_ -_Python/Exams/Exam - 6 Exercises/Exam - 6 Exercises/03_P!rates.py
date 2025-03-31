def plunder(tawns_info, some_tawn, some_people, some_gold):
    if some_tawn in tawns_info.keys():
        tawns_info[some_tawn]["population"] -= some_people
        tawns_info[some_tawn]["gold"] -= some_gold
        if tawns_info[some_tawn]["population"] and tawns_info[some_tawn]["gold"] > 0:
            return f"{some_tawn} plundered! {some_gold} gold stolen, {some_people} citizens killed."
        else:
            del tawns_info[some_tawn]
            print(f"{some_tawn} plundered! {some_gold} gold stolen, {some_people} citizens killed.")
            return f"{some_tawn} has been wiped off the map!"
    
def prosper(tawns_info, some_tawn, some_gold):
    if some_gold > 0:
        tawns_info[some_tawn]["gold"] += some_gold
        return f"{some_gold} gold added to the city treasury. {some_tawn} now has {tawns_info[some_tawn]['gold']} gold."

    return "Gold added cannot be a negative number!" 
        

tawns_info = {}

while True:
    command = input()
    if command == "Sail":
        break
    
    parts = command.split("||")
    cities = parts[0]
    population = int(parts[1])
    gold = int(parts[2])
    if cities not in tawns_info.keys():
        tawns_info[cities] = {"population": 0, "gold": 0}
    
    tawns_info[cities]["population"] += population
    tawns_info[cities]["gold"] += gold

while True:
    command = input()


    if command == "End":
        break

    parts = command.split("=>")
    action = parts[0]

    if action == "Plunder":
        town = parts[1]
        people = int(parts[2])
        gold = int(parts[3])
        result = plunder(tawns_info, town, people, gold)
        print(result)

    elif action == "Prosper":
        tawn = parts[1]
        gold = int(parts[2])
        result = prosper(tawns_info, tawn, gold)
        print(result)

if not tawns_info:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(tawns_info)} wealthy settlements to go to:")

for tawn, info in tawns_info.items():
    print(f'{tawn} -> Population: {info["population"]} citizens, Gold: {info["gold"]} kg')