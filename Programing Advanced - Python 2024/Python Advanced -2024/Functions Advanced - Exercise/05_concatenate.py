def concatenate(*args, **kwargs):
    result = ""
    for element in args:
        result += element

    for kay, value in kwargs.items():
        if kay in result:
            result = result.replace(kay, value)

    return result


