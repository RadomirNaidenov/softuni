def read_next(*args, **kwargs):

    for el in args:
        for sub_el in el:
            yield sub_el

    for kwarg in kwargs:
        yield kwarg




