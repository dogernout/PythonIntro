from decimal import *
import math


def factorz(n):
    i = Decimal(1)
    rez = Decimal(1)
    while i <= n:
        rez *= i
        i += 1
    return rez


n = Decimal(input())
rounder = int(input())
getcontext().prec = rounder


k = 0
sum_pi = Decimal(0)
sum_sin = Decimal(0)
sum_cos = Decimal(0)
while k < 1337:
    d1 = Decimal(-1)
    d1 **= k
    d2 = Decimal(factorz(Decimal(6 * k)))
    d3 = Decimal(13591409 + 545140134 * k)
    d11 = Decimal(factorz(Decimal(3 * k)))
    d22 = Decimal(factorz(Decimal(k))) ** 3
    d33 = Decimal(Decimal(640320) ** 3) ** Decimal(k + Decimal(1 / 2))
    sum_pi += d1 * d2 * d3 / (d11 * d22 * d33)
    k += 1
    #print(k)
k = 0
degr = Decimal(Decimal(1) / (sum_pi * 12))
degr = degr * Decimal(n / 200)
while k < 2000:
    d1 = Decimal(-1) ** k
    d2_cos = Decimal(degr ** Decimal(2 * k))
    d2 = d2_cos * degr
    d2_sin = Decimal(degr ** Decimal(2 * k + 1))
    d11_sin = Decimal(factorz(Decimal(2 * k + 1)))
    d11_cos = Decimal(factorz(Decimal(2 * k)))
    d11 = d11_cos * (2 * k + 1)
    sum_sin += d1 * d2_sin / d11_sin
    sum_cos += d1 * d2_cos  / d11_cos
    k += 1
    #print(k)
#getcontext().rounding = ROUND_DOWN
print(Decimal(sum_sin / sum_cos))
    
    
print(Decimal(math.tan(degr)))

    
#print(sum_pi)
#print(1 / (sum_pi * 12))
#print(math.tan(degr))
#print(math.pi)
