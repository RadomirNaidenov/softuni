from collections import deque

def main(some_amount_of_money: list, some_prices_of_foods: deque) -> None:
    eaten_foods = 0

    while some_amount_of_money and some_prices_of_foods:
        current_money = some_amount_of_money.pop()
        current_food_price = some_prices_of_foods.popleft()

        if current_money >= current_food_price:
            eaten_foods += 1
            current_money -= current_food_price
            if current_money > 0 and some_amount_of_money:
                some_amount_of_money[-1] += current_money

    if eaten_foods >= 4:
        print(f"Gluttony of the day! Henry ate {eaten_foods} foods.")
    elif 1 < eaten_foods < 4:
        print(f"Henry ate: {eaten_foods} foods.")
    elif eaten_foods == 1:
        print(f"Henry ate: {eaten_foods} food.")
    elif not eaten_foods:
        print("Henry remained hungry. He will try next weekend again.")

amount_of_money = [int(x) for x in input().split()]
prices_of_foods = deque([int(x) for x in input().split()])

main(amount_of_money, prices_of_foods)