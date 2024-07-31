import re
total_price = 0
pattern = re.compile(r'(%)(?P<name>[A-Z][a-z]+)(%)([^\|\$\%\.]*)(<)'
                     r'(?P<product>\w+)(>)([^\|\$\%\.]*)(\|)'
                     r'(?P<count>\d+)(\|)([^\|\$\%\.]*)'
                     r'(?P<price>[1-9]+[.0-9]*)\$')

while True:
    command = input()
    if command == "end of shift":
        break

    matches = pattern.finditer(command)

    for match in matches:
        name = match.group("name")
        product = match.group("product")
        count = int(match.group("count"))
        price = float(match.group("price"))
    
        total_price_for_product = count * price
        total_price += total_price_for_product

        print(f"{name}: {product} - {total_price_for_product:.2f}")

print(f"Total income: {total_price:.2f}")

    