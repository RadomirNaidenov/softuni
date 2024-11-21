from project.vehicle import Vehicle


class Car(Vehicle):
    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, name, horse_power):
        super().__init__(name, horse_power)
        self.fuel_consumption = Car.DEFAULT_FUEL_CONSUMPTION
