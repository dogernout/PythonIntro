#import time
#from decimal import *


def dist_3d(a, b):
    f1 = float(b[0]) - float(a[0])
    f2 = float(b[1]) - float(a[1])
    f3 = float(b[2]) - float(a[2])
    return abs(f1 * f1 + f2 * f2 + f3 * f3)
    #return abs(((float(b[0]) - float(a[0])) * (float(b[0]) - float(a[0]) + (float(b[1]) - float(a[1])) * (float(b[1]) - float(a[1])) + (float(b[2]) - float(a[2])) * (float(b[2]) - float(a[2])))) # ** 0.5
    #getcontext().prec = 5
    #return abs(((Decimal(b[0]) - Decimal(a[0])) ** 2 + (Decimal(b[1]) - Decimal(a[1])) ** 2 + (Decimal(b[2]) - Decimal(a[2])) ** 2)) # ** 0.5

    
"""
a = input().split()
mas = dict()
while len(a) > 1:
    if a[-1] not in mas:
        mas[a[-1]] = (a[0] + ' ' + a[1] + ' ' + a[2]).split()
    else:
        mas[a[-1] + ' PUTIN'] = (a[0] + ' ' + a[1] + ' ' + a[2]).split()
    a = input().split()
"""

a = input().split()
mas = []
while len(a) > 1:
    mas.append(a)
    a = input().split()

#start_time = time.time()
leng = len(mas)
i = 0
maxi = -1
maxi_names = ''
cur_names = ''
while i < leng:
    j = i + 1
    while j < leng:
        cur_dist = dist_3d(mas[i], mas[j])
        cur_names = mas[i][-1] + ' ' + mas[j][-1]
        if cur_dist > maxi:
            maxi = cur_dist
            maxi_names = cur_names
        j += 1
    i += 1
#print(maxi)
maxi_names = maxi_names.split()
maxi_names.sort()
print(maxi_names[0] + ' ' + maxi_names[1])

#print('=== {} seconds ==='.format(time.time() - start_time))
