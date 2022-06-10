n = int(input())
i = 0
while 10 ** i <= n:
    i += 1
#print(i)
first_half = n // 10 ** (i // 2 + i % 2)
last_half = n % 10 ** (i // 2)
#print(first_half, last_half)
i //= 2
while last_half != 0:
    first_half -= last_half % 10 * 10 ** (i - 1)
    last_half = (last_half - last_half % 10) // 10
    i -= 1
#print(first_half)
if first_half == 0: print('YES')
else: print('NO')
