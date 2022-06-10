s = input()
w = input()
subz = w[:w.find('@')]
counter = s.count(subz)
i = 0
ind = -1
rez = -1
while i < counter:
    j = 0
    ind = s.find(subz, ind + 1)
    k = ind
    flag = 1
    while k < len(s) and j < len(w):
        if s[k] == w[j] or w[j] == '@':
            k += 1
            j += 1
        else:
            flag = 0
            rez = -1
            break
    if j < len(w):
        flag = 0
        rez = -1
    elif flag:
        rez = ind
        break
    i += 1
print(rez)
