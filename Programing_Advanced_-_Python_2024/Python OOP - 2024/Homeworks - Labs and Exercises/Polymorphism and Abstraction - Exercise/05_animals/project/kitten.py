from project.cat import Cat


class Kitten(Cat):

    def __init__(self, name: str, age: str, gender="Female"):
        super().__init__(name, age, gender)

    @staticmethod
    def make_sound() -> str:
        return "Meow"

