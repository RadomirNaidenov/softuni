number_of_lines = int(input())
tank_capacity = 255

for line in range(number_of_lines):
    litter_of_water = int(input())
    if tank_capacity - litter_of_water < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litter_of_water

print(255 - tank_capacity)
