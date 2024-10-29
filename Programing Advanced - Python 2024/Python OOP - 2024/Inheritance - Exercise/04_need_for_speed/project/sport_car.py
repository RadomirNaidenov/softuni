from project.car import Car


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, name, horse_power):
        super().__init__(name, horse_power)
        self.fuel_consumption = SportCar.DEFAULT_FUEL_CONSUMPTION
