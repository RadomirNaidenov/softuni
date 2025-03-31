deck_of_card = input().split()
count_of_shuffle = int(input())

for shuffle in range(count_of_shuffle):
    middle_od_the_deck = len(deck_of_card) // 2
    left_pard = deck_of_card[:middle_od_the_deck]
    right_pard = deck_of_card[middle_od_the_deck:]
    deck_after_shuffling = []
    for card_index in range(len(left_pard)):
        deck_after_shuffling.append(left_pard[card_index])
        deck_after_shuffling.append(right_pard[card_index])
    deck_of_card = deck_after_shuffling

print(deck_of_card)