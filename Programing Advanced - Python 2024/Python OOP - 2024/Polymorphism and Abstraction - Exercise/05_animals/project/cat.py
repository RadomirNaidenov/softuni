from project.animal import Animal
from abc import ABC, abstractmethod


class Cat(Animal, ABC):

    def make_sound(self):
        return "Meow meow!"



