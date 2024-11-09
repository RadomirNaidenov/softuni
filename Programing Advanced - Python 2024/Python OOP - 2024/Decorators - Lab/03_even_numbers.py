def even_numbers(function):

    def wrapper(numbers):
        return [n for n in numbers if n % 2 == 0]

    return wrapper


