import time

import math


s = set(eval(input()))
start_time = time.time()
m = max(s)
sqr3 = set()
m_sqr = math.ceil(math.sqrt(m))#int(m ** 0.5) + 1
i = 1
"""
slag_1 = set()
slag_2 = set()
slag_3 = set()
while i < m_sqr:
    slag_1.add(i * i)
    i += 1
j = i
i -= 1
mi_sqr = int((m - i * i) ** 0.5) + 1
while j < mi_sqr:
    slag_2.add(j * j)
    j += 1
k = j
j -= 1
mij_sqr = int((m - i * i - j * j) ** 0.5) + 1
while k < mij_sqr:
    slag_3.add(k * k)
    k += 1
print(slag_1, slag_2, slag_3, sep = '\n')


"""
while i < m_sqr:
    j = i
    mi_sqr = math.ceil(math.sqrt(m - i * i))#int((m - i * i) ** 0.5)
    while j < mi_sqr:
        mij_sqr = math.ceil(math.sqrt(m - i * i - j * j)) + 1#int((m - i * i - j * j) ** 0.5)
        k = j
        while k < mij_sqr:
            sqr3.add(i * i + j * j + k * k)
            k += 1
        j += 1
    i += 1
    print(i)
#print(sqr3)
print(len(s & sqr3))
print('=== {} seconds ==='.format(time.time() - start_time))

