def draw_cards(*args, **kwargs):
    cards = {}

    for card_name, card_type in args:
        cards[card_type ] = cards.get(card_type , []) + [card_name]
    
    for dragon_name, type_dragon in kwargs.items():
        cards[type_dragon] = cards.get(type_dragon, []) + [dragon_name]

    type_dragon_lst = cards.get("dragon", [])
    type_spell_lst = cards.get("spell", [])

    sorted_type_dragon_lst = sorted(type_dragon_lst)
    sorted_type_spell_lst = sorted(type_spell_lst)

    if type_dragon_lst:
        print("Monster cards:")
        for dragon in sorted_type_dragon_lst:
            print(f"  ***{dragon}")

    if type_spell_lst:
        print("Spell cards:")
        for spell_name in sorted_type_spell_lst:
            print(f"  $$${spell_name}")


print(draw_cards(("brave attack", "spell"), ("freeze", "spell"), lightning_bolt="spell", fireball="spell",))