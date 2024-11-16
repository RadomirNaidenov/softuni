class countdown_iterator:

    def __init__(self, count: int):
        self.index = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration

        self.index -= 1
        return self.index

