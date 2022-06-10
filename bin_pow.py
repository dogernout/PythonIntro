"""
def BinPow2(a, n, f):
    #res = type(a)(1)
    if type(a) == str:  res = ''
    elif type(a) == int: res = 1
    elif type(a) == tuple: res = (1, 1)
    while n:
        if n & 1:
            res = f(res, a)
        a = f(a, a)
        n >>= 1
    return res


def BinPow2(a, n, f):
    if n == 0:  return a
    if n % 2 == 1:   return BinPow2(a, n - 1, f)
    else:
        b = BinPow2(a, n // 2, f)
        return f(b, b)


"""

def BinPow(a, n, f):
    """
    if n == 0:
        if type(a) == str:
            return ""
        elif type(a) == int:
            return 1
        elif type(a) == tuple:
            return (1, 1)
    """
    if n == 0:
        if type(a) == int:
            return 1
        return type(a)()
    
    if n % 2 == 1:
        return f(a, BinPow(a, n - 1, f))
    else:
        b = BinPow(a, n // 2, f)
        return f(b, b)
"""
print(*BinPow((1,2,56,23,56,7), 99999,  tuple.__add__))
print(BinPow(2,33,int.__mul__), 2**33)
print(BinPow("Se", 7, str.__add__))
def f(a,b): return a^b
print(BinPow(11234123, 223341, f))
"""
