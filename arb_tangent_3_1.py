from decimal import *

import math

import time

       
degree = Decimal(input())
eps = int(input())
start_time = time.time()
getcontext().prec = 1100
k = 1

d64 = Decimal(640320) ** Decimal(3)
d64sqrt = Decimal(d64 ** Decimal(0.5))
pii = Decimal(13591409) / d64sqrt

while k < 100:
    d1 = Decimal(-1) ** k
    d6k = Decimal(math.factorial(6 * k))
    d13 = Decimal(13591409 + 545140134 * k)
    d3k = Decimal(math.factorial(3 * k))
    dk = Decimal(math.factorial(k)) ** 3
    d64sqrt = d64sqrt * d64
    pii += d1 * d6k * d13 / (d3k * dk * d64sqrt)
    k += 1



pii = Decimal(1) / (Decimal(12) * pii)
#print('pi =', pii)
degree = degree * pii / (Decimal(200))
#print('degree =', degree)


k = Decimal(1)



sinn = Decimal(degree)
coss = Decimal(1)

d2_cos = Decimal(1)

d2_sin = degree

d1_1_cos = Decimal(1)


while k < 1000:
    d1 = Decimal(-1) ** k
    d2_cos = d2_cos * degree * degree
    d1_1_cos = d1_1_cos * 2 * k * (2 * k - 1)
    coss += d1 * d2_cos / d1_1_cos
    d2_sin = d2_cos * degree
    d1_1_sin = d1_1_cos * Decimal(2 * k + 1)
    sinn += d1 * d2_sin / d1_1_sin
    k += 1
    #print(d1_1_sin, d1_1_cos, k - 1)
getcontext().prec = eps
print(sinn / coss)

#print("--- %s seconds ---" % (time.time() - start_time))
