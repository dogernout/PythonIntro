from decimal import *

import time


def factorz(n):
    rez = Decimal(1)
    i = 1
    while i <= n:
        rez *= i
        i += 1
    return rez


def factorz1(n):
    rez = Decimal(1)
    i = 1
    mas = []
    mas.append(rez)
    while i <= n:
        rez *= i
        mas.append(rez)
        i += 1
    return mas
        
degree = Decimal(input())
eps = int(input())
start_time = time.time()
#if eps > 499:   getcontext().prec = eps
#else:   getcontext().prec = 500
getcontext().prec = 1000
f = open('mas.txt', 'w')
abc = 0
mas = factorz1(6000)
while abc < len(mas):
    f.write(str(mas[abc]) + ' ')
    abc += 1
f.close()

#print(mas)
pii = Decimal(0)
k = 0
while k < eps + 1:
    d1 = Decimal(-1) ** k
    d2 = factorz(6 * k)
    d3 = Decimal(545140134) * k + Decimal(13591409)
    d1_1 = factorz(3 * k)
    d2_1 = factorz(k) ** 3
    d3_1 = (Decimal(640320) ** 3) ** Decimal(k + 1 / 2)
    pii += d1 * d2 * d3 / (d1_1 * d2_1 * d3_1)
    k += 1
    #print(k)
pii = Decimal(1) / (Decimal(12) * pii)
#print('pi =', pii)
degree = degree * pii / (Decimal(200))
#print('degree =', degree)
k = 0
sinn = Decimal(0)
coss = Decimal(0)
while k < eps + 1:
    d1 = Decimal(-1) ** k
    d2_sin = degree ** Decimal(2 * k + 1)
    #d1_1_sin = factorz(2 * k + 1)
    d2_cos = degree ** Decimal(2 * k)
    #d2_sin = d2_cos * degree
    d1_1_cos = factorz(2 * k)
    d1_1_sin = d1_1_cos * Decimal(2 * k + 1)
    #print(d1, d2_sin, d1_1_sin, d1_1_cos)
    sinn += d1 * d2_sin / d1_1_sin
    coss += d1 * d2_cos / d1_1_cos
    k += 1
#print(sinn / coss, sinn, coss)
getcontext().prec = eps
print(sinn / coss)

print("--- %s seconds ---" % (time.time() - start_time))

