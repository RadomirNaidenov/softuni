def cache(func):

    def wrapper(number):

        if number not in wrapper.log:
            wrapper.log[number] = func(number)

        return wrapper.log[number]

    wrapper.log = {}
    return wrapper

