from abc import ABC, abstractmethod


class BaseStore(ABC):

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value or value.strip() == "":
            raise ValueError("Store name cannot be empty!")

        self.__name = value

    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, value):
        if " " in value or len(value) != 3:
            raise ValueError("Store location must be 3 chars long!")

        self.__location = value

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")

        self.__capacity = value

    def get_estimated_profit(self):
        total_price = 0
        for product in self.products:
            total_price += product.price

        total_price *= 0.10

        return f"Estimated future profit for {len(self.products)} products is {total_price:.2f}"

    @property
    @abstractmethod
    def store_type(self):
        ...

    @abstractmethod
    def store_stats(self):
        ...












