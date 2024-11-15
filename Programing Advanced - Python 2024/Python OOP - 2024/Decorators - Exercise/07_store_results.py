class store_results:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        with open('results.txt', 'a') as text_file:
            text_file.write(f'Function \'{self.func.__name__}\' was called. Result: {self.func(*args)}\n')
            
