food_and_quantity = input().split(" ")
my_dict = {}

for i in range(0, len(food_and_quantity), 2):
    key = food_and_quantity[i]
    value = food_and_quantity[i + 1]
    my_dict[key] = int(value)

searched_product = input().split()

for product in searched_product:
    if product in my_dict:
        print(f"We have {my_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")