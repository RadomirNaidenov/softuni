def orders_func(product, quantity):
    price = 0
    if product == "coffee":
        price = 1.50
    elif product == "water":
        price = 1.00
    elif product == "coke":
        price = 1.40
    elif product == "snacks":
        price = 2.00

    return f"{price * quantity:.2f}"


type_product = input()
quantity_product = int(input())
print(orders_func(type_product, quantity_product))

