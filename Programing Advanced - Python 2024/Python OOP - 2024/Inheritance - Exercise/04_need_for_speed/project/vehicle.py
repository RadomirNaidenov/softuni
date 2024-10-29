class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = Vehicle.DEFAULT_FUEL_CONSUMPTION
        self.can_drive = True

    def drive(self, kilometers):
        if self.can_drive:
            if self.fuel - (kilometers * self.DEFAULT_FUEL_CONSUMPTION) >= 0:
                self.fuel -= (kilometers * self.DEFAULT_FUEL_CONSUMPTION)
                if self.fuel == 0:
                    self.can_drive = False






vehicle = Vehicle(50, 150)