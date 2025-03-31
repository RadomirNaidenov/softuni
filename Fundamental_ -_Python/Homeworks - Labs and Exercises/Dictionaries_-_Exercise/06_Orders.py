info_products = {}
price = 0
quantity = 1
# [float(price_data), int(quantity)]
command = input()

while True:
    if command == "buy":
        break
    product, product_price, _quantity = command.split(" ")
    if product not in info_products:
        info_products[product] = [float(product_price), 0]

    info_products[product][quantity] += int(_quantity)

    if info_products[product][price] != float(product_price):
        info_products[product][price] = float(product_price)

    command = input()

for product in info_products:
    print(f"{product} -> {info_products[product][price] * info_products[product][quantity]:.2f}")



