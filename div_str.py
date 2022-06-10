class DivStr(str):
    
    def __init__(self, s):
        self.s = s
        self.leng = len(s)

    def __getitem__(self, ind):
        return DivStr(self.s[ind])

    def __add__(self, other):
        return DivStr(self.s + other)

    def __radd__(self, other):
        return DivStr(other + self.s)

    def __mul__(self, other):
        return DivStr(self.s * other)

    def __rmul__(self, other):
        return DivStr(self * other)

    def __floordiv__(self, other):
        out = []
        word_len = self.leng // other
        if word_len == 0: return ['' for i in range(other)]
        j = 0
        cur_str = DivStr(self.s[:self.leng - self.leng % word_len])
        while j < cur_str.leng:
            out.append(cur_str[j:j + word_len])
            j += word_len
        return out

    def __mod__(self, other):
        out_len = self.leng % other
        return DivStr(self.s[self.leng - out_len:])

    def lower(self):
        return DivStr(self.s.lower())

    def capitalize(self):
        return DivStr(self.s.capitalize())

    def casefold(self):
        return DivStr(self.s.casefold())

    def center(self, *arg):
        return DivStr(self.s.center(*arg))

    def encode(self, *arg):#
        return DivStr(self.s.encode(*arg))

    def endswith(self, *arg):
        return DivStr(self.s.endswith(*arg))

    def expandtabs(self, *arg):
        return DivStr(self.s.expandtabs(*arg))

    def format(self, *args, **kwargs):
        return DivStr(self.s.format(*args, *kwargs))

    def format_map(self, *arg):
        return DivStr(self.s.format_map(*arg))

    def join(self, *arg):
        return DivStr(self.s.join(*arg))

    def ljust(self, *arg):
        return DivStr(self.s.ljust(*arg))

    def lstrip(self, *arg):
        return DivStr(self.s.lstrip(*arg))

    def maketrans(self, *arg):
        return DivStr(self.s.maketrans(*arg))

    def partition(self, *arg):
        return DivStr(self.s.partition(*arg))

    def replace(self, *arg, **kwargs):
        return DivStr(self.s.replace(*arg, **kwargs))

    def rjust(self, *arg):
        return DivStr(self.s.rjust(*arg))

    def rpartition(self, *arg):
        return DivStr(self.s.rpartition(*arg))

    def rstrip(self, *arg):
        return DivStr(self.s.rstrip(*arg))

    def strip(self, *arg):
        return DivStr(self.s.strip(*arg))

    def swapcase(self):
        return DivStr(self.s.swapcase())

    def title(self):
        return DivStr(self.s.title())

    def translate(self, *arg):
        return DivStr(self.s.translate(*arg))

    def upper(self):
        return DivStr(self.s.upper())

    def zfill(self, *arg):
        return DivStr(self.s.zfill(*arg))

    def removeprefix(self, *arg):
        return DivStr(self.s.removeprefix(*arg))

    def removesuffix(self, *arg):
        return DivStr(self.s.removesuffix(*arg))
