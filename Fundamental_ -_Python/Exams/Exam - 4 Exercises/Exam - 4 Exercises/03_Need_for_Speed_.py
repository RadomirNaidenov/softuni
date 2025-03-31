def drive(some_info_about_cars: dict, some_brand_car: str, some_distance: int, some_fuel: int) -> str:
    returning_list = []
    if some_info_about_cars[some_brand_car]['fuel'] >= some_fuel:
        some_info_about_cars[some_brand_car]['mileage'] += some_distance
        some_info_about_cars[some_brand_car]['fuel'] -= some_fuel
        returning_list.append(f"{some_brand_car} driven for {some_distance} kilometers. {some_fuel} liters of fuel consumed.")
        if some_info_about_cars[some_brand_car]['mileage'] >= 100000:
            del some_info_about_cars[some_brand_car]
            returning_list.append(f"Time to sell the {some_brand_car}!")
        return returning_list
    
    return "Not enough fuel to make that ride"


def refuel(some_info_about_cars: dict, some_brand_car: str, some_fuel: int) -> str:
    if some_info_about_cars[some_brand_car]['fuel'] + some_fuel > 75:
        refueled_ltr = 75 - some_info_about_cars[some_brand_car]['fuel']
        some_info_about_cars[some_brand_car]['fuel'] = 75
    else:
        refueled_ltr = some_fuel
        some_info_about_cars[some_brand_car]['fuel'] += some_fuel
    return f"{some_brand_car} refueled with {refueled_ltr} liters"


def revert(some_info_about_cars: dict, some_brand_car: str, some_kilometers: int) -> str:
    some_info_about_cars[some_brand_car]["mileage"] -= some_kilometers
    if some_info_about_cars[some_brand_car]["mileage"] < 10000:
        some_info_about_cars[some_brand_car]["mileage"] = 10000
        return ""
    else:
        return f"{some_brand_car} mileage decreased by {some_kilometers} kilometers"
        

number_of_cars = int(input())
info_about_cars = {}

for car in range(number_of_cars):
    car = input().split("|")
    car_brand = car[0]
    mileage = int(car[1])
    fuel = int(car[2])
    info_about_cars[car_brand] = {'mileage': mileage, 'fuel': fuel}


while True:
    command = input()
    if command == "Stop":
        break

    command = command.split(" : ")

    action = command[0]
    brand_car = command[1]

    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        result = (drive(info_about_cars, brand_car, distance, fuel))
        print("\n".join(result))

    elif action == "Refuel":
        fuel = int(command[2])
        print(refuel(info_about_cars, brand_car, fuel))

    elif action == "Revert":
        kilometars = int(command[2])
        result = revert(info_about_cars, brand_car, kilometars)
        if result:
            print(result)
    
for car_brand, data in info_about_cars.items():
    print(f"{car_brand} -> Mileage: {data['mileage']} kms, Fuel in the tank: {data['fuel']} lt.")