budget = float(input())
price_per_kg_flour = float(input())
price_for_1_pack_eggs = price_per_kg_flour * (- 0.25)
price_per_pack_eggs = 0.75 * price_per_kg_flour
price_per_liter_milk = 1.25 * price_per_kg_flour
price_per_250ml_milk = price_per_liter_milk / 4

price_per_loaf = price_per_kg_flour + price_per_pack_eggs + price_per_250ml_milk

number_of_loaves = 0
colored_eggs = 0

while budget >= price_per_loaf:
    budget -= price_per_loaf
    number_of_loaves += 1
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")






