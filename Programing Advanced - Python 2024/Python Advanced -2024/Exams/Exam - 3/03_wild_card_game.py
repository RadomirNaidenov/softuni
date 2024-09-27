def draw_cards(*args, **kwargs):
    type_dragon_lst = []
    type_spell_lst = []

    for arg in args:
        name_of_the_card = arg[0]
        type_of_the_card = arg[1]
        if type_of_the_card == "monster":
            type_dragon_lst.append(name_of_the_card)
        elif type_of_the_card == "spell":
            type_spell_lst.append(name_of_the_card)
    
    for dragon_name, type_dragon in kwargs.items():
        if type_dragon == "spell":
            type_spell_lst.append(dragon_name)
        elif type_dragon == "monster":
            type_dragon_lst.append(dragon_name)
    
    sorted_type_dragon_lst = sorted(type_dragon_lst)
    sorted_type_spell_lst = sorted(type_spell_lst)

    
    if type_dragon_lst:
        print("Monster cards:")
        print()
        for dragon in sorted_type_dragon_lst:
            print(f"  ***{dragon}")
            print()
    if type_spell_lst:
        print("Spell cards:")
        print()
        for spell_name in sorted_type_spell_lst:
            print(f"  $$${spell_name}")
            print()


print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))