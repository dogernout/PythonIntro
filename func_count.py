class counter:
    aboba = 0
    def __init__(self, fun):
        self.fun = fun
        self.aboba = 0

    def __call__(self, *args, **kwargs):
        self.aboba += 1
        return self.fun(*args, **kwargs)

    def counter(self):
        return self.aboba
