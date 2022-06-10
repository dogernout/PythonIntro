n = int(input())
i = 2
while n % i != 0 and i < n // 2 + 1:
    i += 1
print(i)
#if n % i != 0:
 #   i = n # n - prostoe
 #   print('NO')
#else:
copy_i = i
while i < n:
    print(i)
    i *= copy_i
print('YES' * (i == n) + 'NO' * (i != n))
