a, b, r = list(map(int, input().split(',')))
x1, y1 = list(map(int, input().split(',')))
flag = 1
while x1 != 0 or y1 != 0:
    if (x1 - a) ** 2 + (y1 - b) ** 2 > r ** 2:
        flag = 0
    x1, y1 = list(map(int, input().split(',')))
print(['NO', 'YES'][flag])
