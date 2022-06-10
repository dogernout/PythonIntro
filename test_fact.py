import math

from decimal import *


i = Decimal(1)
mas = []
mas.append(i)
rez = Decimal(1)
while i <= 180:
    rez *= i
    mas.append(rez)
    i += 1
print(mas)
    
