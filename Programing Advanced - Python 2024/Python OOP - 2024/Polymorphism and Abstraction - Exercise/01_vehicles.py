from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    air_conditioner = 0.9

    def drive(self, distance):
        car_consumption = (self.fuel_consumption + Car.air_conditioner) * distance

        if car_consumption <= self.fuel_quantity:
            self.fuel_quantity -= car_consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    air_conditioner = 1.6

    def drive(self, distance: int):
        truck_consumption = (self.fuel_consumption + Truck.air_conditioner) * distance

        if truck_consumption <= self.fuel_quantity:
            self.fuel_quantity -= truck_consumption

    def refuel(self, fuel: int):
        self.fuel_quantity += fuel * 0.95





