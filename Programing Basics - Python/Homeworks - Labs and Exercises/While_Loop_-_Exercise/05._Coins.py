change_amount = float(input())
change_amount_coins = int(change_amount * 100)
total_coins = 0
while change_amount_coins > 0:
    if change_amount_coins >= 200:
        change_amount_coins -= 200
    elif change_amount_coins >= 100:
        change_amount_coins -= 100
    elif change_amount_coins >= 50:
        change_amount_coins -= 50
    elif change_amount_coins >= 20:
        change_amount_coins -= 20
    elif change_amount_coins >= 10:
        change_amount_coins -= 10
    elif change_amount_coins >= 5:
        change_amount_coins -= 5
    elif change_amount_coins >= 2:
        change_amount_coins -= 2
    elif change_amount_coins >= 1:
        change_amount_coins -= 1

    total_coins += 1

print(total_coins)