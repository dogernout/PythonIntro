k = int(input())
n = -1
i = 0
while n * k != (k * 10 ** i + n - k) // 10:
    if (k * 10 ** (i + 1) - k) % (10 * k - 1) == 0:
        n = (k * 10 ** (i + 1) - k) // (10 * k - 1)
    else:
        n = -1
    i += 1
if k == 1: n = 1
print(n)
