import numpy

class Dots:

    def __init__(self, a, b):
        self.st = a
        self.fin = b

    def __getitem__(self, ind):
        if not isinstance(ind, slice):
            i = self.st
            mas = []
            if not ind: return
            if ind == 1: return self.st
            stepper = (self.fin - self.st) / (ind - 1)
            while i <= self.fin:
                mas.append(i)
                i += stepper
            return mas
        indstart = ind.start
        indstop = ind.stop
        if ind.step == None:    return self.st + ind.start * (self.fin - self.st) / (ind.stop - 1)
        if ind.start == None: indstart = 0
        if ind.stop == None: indstop = ind.step
        mas = []
        i = indstart
        stepper = (self.fin - self.st) / (ind.step - 1)
        if int(stepper) == stepper:
            stepper = int(stepper)
            return iter(range(self.st + stepper * indstart, self.st + stepper * indstop, stepper))
        while i < indstop:
            mas.append(self.st + i * stepper)
            i += 1
        return mas
