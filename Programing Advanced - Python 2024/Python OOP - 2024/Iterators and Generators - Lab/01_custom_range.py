class custom_range:

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current_number = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_number += 1
        if self.current_number > self.end:
            raise StopIteration

        return self.current_number


