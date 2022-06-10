from decimal import *

import math

import time

        
degree = Decimal(input())
eps = int(input())
start_time = time.time()
getcontext().prec = 1001
pii = Decimal(0)
k = 0
while k < 30:
    d1 = Decimal(-1) ** k
    #if k % 2 == 0:  d1 = Decimal(1)
    #else:   d1 = Decimal(-1)
    #d1 = Decimal(-1) ** k
    d2 = Decimal(math.factorial(6 * k))
    d3 = Decimal(545140134) * k + Decimal(13591409)
    d1_1 = Decimal(math.factorial(3 * k))
    d2_1 = Decimal(math.factorial(k)) ** 3
    d3_1 = (Decimal(640320) ** 3) ** (k + Decimal(1 / 2))
    pii += d1 * d2 * d3 / (d1_1 * d2_1 * d3_1)
    k += 1
pii = Decimal(1) / (Decimal(12) * pii)
print('pi =', pii)
degree = degree * pii / (Decimal(200))
#print('degree =', degree)
k = Decimal(1)



sinn = Decimal(degree)
coss = Decimal(1)

d2_cos = Decimal(1)

d2_sin = degree

d1_1_cos = Decimal(1)


while k < eps + 1:
    d1 = Decimal(-1) ** k
    d2_cos = d2_cos * degree * degree
    d1_1_cos = d1_1_cos * 2 * k * (2 * k - 1)
    coss += d1 * d2_cos / d1_1_cos
    d2_sin = d2_cos * degree
    d1_1_sin = d1_1_cos * Decimal(2 * k + 1)
    sinn += d1 * d2_sin / d1_1_sin
    k += 1
getcontext().prec = eps
print(sinn / coss)

print("--- %s seconds ---" % (time.time() - start_time))
