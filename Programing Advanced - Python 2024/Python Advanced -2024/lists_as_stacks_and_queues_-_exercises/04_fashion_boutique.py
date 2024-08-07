clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

rack_count = 1
current_rack_capacity = rack_capacity

while clothes:
    cloth = clothes.pop()
    if current_rack_capacity < cloth:
        rack_count += 1
        current_rack_capacity = rack_capacity - cloth
        continue
       
    current_rack_capacity -= cloth

print(rack_count)



        

