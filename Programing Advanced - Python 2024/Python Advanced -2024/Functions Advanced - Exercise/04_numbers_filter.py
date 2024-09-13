def even_odd_filter(**kwargs):
    for key in kwargs.keys():
        if key == "odd":
            kwargs[key] = list(filter(lambda x: x % 2 != 0, kwargs[key]))
        else:
            kwargs[key] = list(filter(lambda x: x % 2 == 0, kwargs[key]))

    return kwargs

