import re

pattern = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>[0-9]+[\\.0-9]*)!(?P<quantity>[0-9]+)"

purchases = input()

furniture = []
total_price = []

while True:

    if purchases == "Purchase":
        break

    matches = re.finditer(pattern, purchases)

    for match in matches:
        current_item_price = float(match["price"]) * float(match["quantity"])
        furniture.append(match["furniture"])
        total_price.append(current_item_price)

    purchases = input()
print("Bought furniture:")
for item in furniture:
    print(item)

print(f"Total money spend: {sum(total_price):.2f}")
