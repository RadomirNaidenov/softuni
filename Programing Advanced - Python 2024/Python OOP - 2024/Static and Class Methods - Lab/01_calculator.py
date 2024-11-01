from functools import reduce


class Calculator:

    @staticmethod
    def add(*args) -> int:
        return reduce(lambda x, y: x + y, args)

    @staticmethod
    def multiply(*args) -> int:
        return reduce(lambda x, y: x * y, args)

    @staticmethod
    def divide(*args) -> int:
        return reduce(lambda x, y: x / y, args)

    @staticmethod
    def subtract(*args) -> int:
        return reduce(lambda x, y: x - y, args)

