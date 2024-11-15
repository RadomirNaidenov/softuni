def type_check(data_type):

    def decorator(function):
        def wrapper(arg):
            if isinstance(arg, data_type):
                return function(arg)
            return "Bad Type"

        return wrapper

    return decorator

