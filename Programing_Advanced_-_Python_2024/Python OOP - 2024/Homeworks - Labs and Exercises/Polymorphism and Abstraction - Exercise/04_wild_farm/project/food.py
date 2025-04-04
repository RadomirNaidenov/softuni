from abc import ABC, abstractmethod


class Food(ABC):

    @abstractmethod
    def __init__(self, quantity: int):
        self.quantity = quantity


class Vegetable(Food, ABC):

    def __init__(self, quantity: int):
        super().__init__(quantity)


class Fruit(Food, ABC):

    def __init__(self, quantity: int):
        super().__init__(quantity)


class Meat(Food, ABC):

    def __init__(self, quantity: int):
        super().__init__(quantity)


class Seed(Food, ABC):

    def __init__(self, quantity: int):
        super().__init__(quantity)


