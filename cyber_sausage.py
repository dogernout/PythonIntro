from fractions import Fraction


class Sausage:

    def __init__(self, meat = "pork!", vol = 1):
        self.meat = meat
        self.vol = Fraction(vol)

    def __abs__(self):
        if self.vol > 0:    return self.vol
        return 0

    def __bool__(self):
        return True if abs(self) else False

    def __mul__(self, other):
        rez = Sausage(self.meat, self.vol * Fraction(other))
        return rez

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        rez = Sausage(self.meat, self.vol / Fraction(other))
        return rez

    def __add__(self, other):
        rez = Sausage(self.meat, self.vol + other.vol)
        return rez

    def __sub__(self, other):
        rez = Sausage(self.meat, self.vol - other.vol)
        return rez

    def __str__(self):
        counter = int(12 * self.vol)
        if counter == 0: counter = -1
        first_line = '/'
        sec_line = '|'
        last_line = '\\'
        i = 1
        j = 0
        leng = len(self.meat)
        while i <= counter:
            if j == leng: j = 0
            sec_line += self.meat[j]
            j += 1
            first_line += '-'
            last_line += '-'
            if i % 12 == 0:
                j = 0
                first_line += '\\'
                last_line += '/'
                sec_line += '|'
                if i < counter:
                    first_line += '/'
                    sec_line += '|'
                    last_line += '\\'
            i += 1
        if counter % 12 > 0:
            first_line += '|'
            sec_line += '|'
            last_line += '|'
        rez = first_line + '\n' + sec_line + '\n' + sec_line + '\n' + sec_line + '\n' + last_line
        return rez
