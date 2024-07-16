import re

input_data = input()

pattern = r'(#|\|)([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1'

result = re.findall(pattern, input_data)
products_list = []
total_calories = 0

for match in result:
    item_name = match[1]
    expiration_date = match[2]
    calories = int(match[3])
    products_list.append([item_name, expiration_date, calories])
    total_calories += calories

needed_days = total_calories // 2000
print(f"You have food to last you for: {needed_days} days!")

for element in products_list:
    print(f"Item: {element[0]}, Best before: {element[1]}, Nutrition: {element[2]}")
