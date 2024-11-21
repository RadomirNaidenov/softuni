from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @property
    def food_that_eat(self) -> list:
        return [Meat]

    @property
    def weight_that_gain(self) -> float:
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    def make_sound(self) -> str:
        return "Cluck"

    @property
    def weight_that_gain(self) -> float:
        return 0.35

    @property
    def food_that_eat(self) -> list:
        return [Meat, Seed, Fruit, Vegetable]
