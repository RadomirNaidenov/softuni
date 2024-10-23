from collections import deque

green_light = int(input())
free_window = int(input())
waiting_cars = deque()

green_light_duration = green_light
total_passed_cars = 0
is_crashed = False
command = input()
while command != "END":

    if command != "green":    
        waiting_cars.append(command) 
        command = input()
        continue
    

    while green_light_duration > 0 and waiting_cars:
        car = waiting_cars.popleft()
        can_pass =  free_window + green_light_duration >= len(car)
        if can_pass:
            green_light_duration -= len(car)
            total_passed_cars += 1
            continue

        character_hit = car[free_window + green_light_duration:free_window + green_light_duration + 1]
        print(f"A crash happened!\n{car} was hit at {character_hit}.")
        is_crashed = True
        break

    green_light_duration = green_light

    if is_crashed:
        break
        
    command = input()

else:
    print("Everyone is safe.")
    print(f"{total_passed_cars} total cars passed the crossroads.")



