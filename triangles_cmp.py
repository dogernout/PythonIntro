class Triangle:

    def __init__(self, a, b, c):
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def __bool__(self):
        return self.a > 0 and self.b > 0 and self.c > 0 and self.a + self.b > self.c and self.b + self.c > self.a and self.a + self.c > self.b

    def __abs__(self):
        if self:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        return 0

    def __eq__(self, other):
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return True
        if self.a == other.a and self.b == other.c and self.c == other.b:
            return True
        if self.a == other.b and self.b == other.a and self.c == other.c:
            return True
        if self.a == other.b and self.b == other.c and self.c == other.a:
            return True
        if self.a == other.c and self.b == other.a and self.c == other.b:
            return True
        if self.a == other.c and self.b == other.b and self.c == other.a:
            return True
        return False

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __str__(self):
        return str(str(self.a) + ':' + str(self.b) + ':' + str(self.c))
