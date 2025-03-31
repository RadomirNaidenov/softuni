def cast_spell(dict_of_collection_heroes: dict, some_hero_name: str, some_manna_points_needed: int, some_spell_name: str) -> str:
    if some_hero_name in dict_of_collection_heroes.keys():
        if dict_of_collection_heroes[some_hero_name]["mana_points"] >= some_manna_points_needed:
            dict_of_collection_heroes[some_hero_name]["mana_points"] -= some_manna_points_needed
            return f"{some_hero_name} has successfully cast {some_spell_name} and now has {dict_of_collection_heroes[some_hero_name]['mana_points']} MP!"
        return f"{some_hero_name} does not have enough MP to cast {some_spell_name}!"


def take_damage(dict_of_collection_heroes: dict, some_hero_name: str, some_damage: int, some_attacker: str) -> str:
    if some_hero_name in dict_of_collection_heroes.keys():
        dict_of_collection_heroes[some_hero_name]["hit_points"] -= some_damage
        if dict_of_collection_heroes[some_hero_name]["hit_points"] > 0:
            return f"{some_hero_name} was hit for {some_damage} HP by {some_attacker} and now has {dict_of_collection_heroes[some_hero_name]['hit_points']} HP left!"
        del dict_of_collection_heroes[some_hero_name]
        return f"{some_hero_name} has been killed by {some_attacker}!"


def recharge(dict_of_collection_heroes: dict, some_hero_name: str, adding_some_mana_amount: int) -> str:
    current_mana = dict_of_collection_heroes[some_hero_name]["mana_points"] 
    if some_hero_name in dict_of_collection_heroes.keys():
        dict_of_collection_heroes[some_hero_name]["mana_points"] += adding_some_mana_amount
        if dict_of_collection_heroes[some_hero_name]["mana_points"] > 200:
            dict_of_collection_heroes[some_hero_name]["mana_points"] = 200
        recharged_amount = dict_of_collection_heroes[some_hero_name]["mana_points"] - current_mana
        return f"{some_hero_name} recharged for {recharged_amount} MP!"


def heal(dict_of_collection_heroes: dict, some_hero_name: str, adding_some_hit_points_amount: int) -> str:
    current_hp = dict_of_collection_heroes[some_hero_name]["hit_points"]
    if some_hero_name in dict_of_collection_heroes.keys():
        dict_of_collection_heroes[some_hero_name]["hit_points"] += adding_some_hit_points_amount
        if dict_of_collection_heroes[some_hero_name]["hit_points"] > 100:
            dict_of_collection_heroes[some_hero_name]["hit_points"] = 100
        healed_amount = dict_of_collection_heroes[some_hero_name]["hit_points"] - current_hp
        return f"{some_hero_name} healed for {healed_amount} HP!"

    

number_of_heroes = int(input())
collection_heroes = {}


for hero in range(number_of_heroes):
    command = input().split()
    hero_name = command[0]
    hit_points = int(command[1])
    mana_points = int(command[2])
    collection_heroes[hero_name] = {"hit_points": hit_points, "mana_points": mana_points}



while True:
    command = input()
    if command == "End":
        break

    command = command.split(" - ")
    action = command[0]

    if action == "CastSpell":
        hero_name = command[1]
        mana_points_needed = int(command[2])
        spell_name = command[3]
        result = cast_spell(collection_heroes, hero_name, mana_points_needed, spell_name)
        print(result)
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        result = take_damage(collection_heroes, hero_name, damage, attacker)
        print(result)

    elif action == "Recharge":
        hero_name = command[1]
        adding_mana_amount = int(command[2])
        result = recharge(collection_heroes, hero_name, adding_mana_amount)
        print(result)
    elif action == "Heal":
        hero_name = command[1]
        adding_hit_points = int(command[2])
        result = heal(collection_heroes, hero_name, adding_hit_points)
        print(result)
    
    


for key, value in collection_heroes.items():
    print(key)
    print(f'  HP: {value["hit_points"]}')
    print(f'  MP: {value["mana_points"]}')
