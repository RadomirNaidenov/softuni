number_of_cars = int(input())
cars = []
for car in range(number_of_cars):
    car = input().split(", ")
    car_info = car[0]
    car_number = car[1]

    if car_info == "IN":
        if car_number not in cars:
            cars.append(car_number)
    elif car_info == "OUT":
        if car_number in cars:
            cars.remove(car_number)

if not cars:
    print("Parking Lot is Empty")
for car in cars:
    print(car)

