from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        ...

    @property
    @abstractmethod
    def weight_that_gain(self):
        ...

    @property
    @abstractmethod
    def food_that_eat(self):
        ...

    def feed(self, food: Food):
        if type(food) not in self.food_that_eat:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_that_gain
        self.food_eaten += food.quantity


class Bird(Animal, ABC):

    def __init__(self, name: str, weight: int, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Mammal(Animal, ABC):

    def __init__(self, name: str, weight: int, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"



