from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):

    def make_sound(self) -> str:
        return "Squeak"

    @property
    def weight_that_gain(self) -> float:
        return 0.10

    @property
    def food_that_eat(self) -> list:
        return [Fruit, Vegetable]


class Dog(Mammal):

    def make_sound(self) -> str:
        return "Woof!"

    @property
    def weight_that_gain(self) -> float:
        return 0.40

    @property
    def food_that_eat(self) -> list:
        return [Meat]


class Cat(Mammal):

    def make_sound(self) -> str:
        return "Meow"

    @property
    def weight_that_gain(self) -> float:
        return 0.30

    @property
    def food_that_eat(self) -> list:
        return [Meat, Vegetable]


class Tiger(Mammal):

    def make_sound(self) -> str:
        return "ROAR!!!"

    @property
    def weight_that_gain(self) -> float:
        return 1.00

    @property
    def food_that_eat(self) -> list:
        return [Meat]

