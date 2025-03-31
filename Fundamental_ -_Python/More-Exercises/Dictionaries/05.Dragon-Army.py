number_of_dragons = int(input()) 
drakes_infos = {}

dammage_if_nill = 45 
health_if_null = 250 
armor_if_null = 10 

for dragon in range(number_of_dragons): 
    drake_info = input() 
    type_drake, drake_name, damage, health, armor = drake_info.split()
    
    if type_drake not in drakes_infos:
        drakes_infos[type_drake] = {}
    
    if drake_name not in drakes_infos[type_drake]:
        drakes_infos[type_drake][drake_name] = {} 
    
    drakes_infos[type_drake][drake_name]["damage"] = int(damage) if damage != "null" else dammage_if_nill
    drakes_infos[type_drake][drake_name]["health"] = int(health) if health != "null" else health_if_null
    drakes_infos[type_drake][drake_name]["armor"] = int(armor) if armor != "null" else armor_if_null


for type_drake in drakes_infos:
    total_dragons = len(drakes_infos[type_drake])
    avg_damage, avg_health, avg_armor = 0, 0, 0

    for drake_stats in drakes_infos[type_drake].values():
        avg_damage += drake_stats["damage"]
        avg_health += drake_stats["health"]
        avg_armor += drake_stats["armor"]

    avg_damage = avg_damage / total_dragons
    avg_health =  avg_health /total_dragons
    avg_armor = avg_armor /total_dragons

    print(f"{type_drake}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    for drake_name, drake_stats in sorted(drakes_infos[type_drake].items()):
        print(f'-{drake_name} -> damage: {drake_stats["damage"]}, health: {drake_stats["health"]}, armor: {drake_stats["armor"]}')
# ----------------------------

# number_of_dragons = int(input()) 
# drakes_infos = {}

# dammage_if_nill = 45
# healt_if_null = 250 
# armor_if_null = 10 #
# for dragon in range(number_of_dragons): 
#     drake_info = input() 
#     type_drake, drake_name, dammage, health, armor = [int(item) if item.isdigit() else item for item in drake_info.split(" ")]

#     drakes_infos[type_drake] = drakes_infos.get(type_drake, {})
#     drakes_infos[type_drake][drake_name] = {"damage": dammage, "health": health, "armor": armor}
       
#     if drakes_infos[type_drake][drake_name]["damage"] == "null":
#         drakes_infos[type_drake][drake_name]["damage"] = dammage_if_nill
#     elif drakes_infos[type_drake][drake_name]["health"] == "null":
#         drakes_infos[type_drake][drake_name]["health"] = healt_if_null
#     elif drakes_infos[type_drake][drake_name]["armor"] == "null":
#         drakes_infos[type_drake][drake_name]["armor"] = armor_if_null

# for type_drake in drakes_infos:
#     total_dragons = len(drakes_infos[type_drake])
#     avg_damage, avg_health, avg_armor = 0, 0, 0

#     for drake_stats in drakes_infos[type_drake].values():
#         avg_damage += drake_stats["damage"]
#         avg_health += drake_stats["health"]
#         avg_armor += drake_stats["armor"]

#     avg_damage = avg_damage / total_dragons
#     avg_health =  avg_health /total_dragons
#     avg_armor = avg_armor /total_dragons

#     print(f"{type_drake}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

#     for drake_name, drake_stats in sorted(drakes_infos[type_drake].items()):
#         print(f'-{drake_name} -> damage: {drake_stats["damage"]}, health: {drake_stats["health"]}, armor: {drake_stats["armor"]}')



        
        



