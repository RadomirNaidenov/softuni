from itertools import permutations


def possible_permutations(some_list: list):
    for el in permutations(some_list):
        yield list(el)


[print(n) for n in possible_permutations([1, 2, 3])]