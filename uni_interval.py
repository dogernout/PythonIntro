c = input()
if ' ' not in c: c = c.split(',')
else: c = c.split(', ')
#c = input().split(', ')
mas = []
i = 0
leng = len(c)
while i < leng:
    if '(' in c[i]:
        mas.append((int(c[i][1:]), 0))
    else:
        mas.append((int(c[i][:-1]), 1))
    i += 1
mas.sort(key = lambda x: x[0])
i = 0
while i < leng - 1:
    if mas[i][0] == mas[i + 1][0] and mas[i][1] > mas[i + 1][1]:
        mas[i], mas[i + 1] = mas[i + 1], mas[i]
    i += 1
i = 0
counter = 0
res = 0
while i < leng:
    if counter > 0: res += mas[i][0] - mas[i - 1][0]
    if mas[i][1]: counter -= 1
    else: counter += 1
    i += 1
print(res)
