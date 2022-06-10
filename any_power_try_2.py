def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return gcd(a % b, b)
    return gcd(a, b % a)


n = int(input())
divider = 2
count = 0 # zdesb budet stepenb prostogo chisla
count_old = 0 # a zdesb budet stepenb prediduwego
gcd_check = -1
flag = 1
while n > 1:
    if n % divider == 0:
        n //= divider
        count += 1
    else:
        if count != 0:  count_old = count      
        if count_old != 0:
            gcd_check = gcd(count, count_old)
            if gcd_check == 1:
                flag = 0
                break
        count = 0
        divider += 1
if flag == 1 and count > 1: print('YES')
else:   print('NO')
        
    

