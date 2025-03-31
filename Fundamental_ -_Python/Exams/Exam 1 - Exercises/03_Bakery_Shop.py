shop_info = {}
total_products = 0
while True:
    command = input()
    if command == "Complete":
        break

    command = command.split()
    action = command[0]
    quantity = int(command[1])
    food = command[2]

    if action == "Receive":
        if quantity <= 0:
            continue

        if food in shop_info:
            shop_info[food] += quantity
        else:
            shop_info[food] = quantity

    elif action == "Sell":
        if food not in shop_info:
            print(f"You do not have any {food}.")

        else:
            if shop_info[food] < quantity:
                sold_quantity = shop_info[food]
                total_products += sold_quantity
                print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
                del shop_info[food]

            else:
                shop_info[food] -= quantity
                total_products += quantity
                print(f"You sold {quantity} {food}.")
                if shop_info[food] == 0:
                    del shop_info[food]


for food, quantity in shop_info.items():
    print(f"{food}: {quantity}")

print(f"All sold: {total_products} goods")






