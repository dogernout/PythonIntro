s = input()
mas = []
counter = 0
mas.append(s)
#print(mas, s)
while 1:
    s = input()
    mas.append(s)
    if s[0] == '-': break
#print(mas)
i = 0
leng = len(mas)
while i < leng:
    j = 0
    len_str = len(mas[i])
    while j < len_str:
        if mas[i][j] == '#':
            i_start = i
            j_start = j
            while mas[i][j] == '#':
                j += 1
            j_fin = j
            j = j_start
            while mas[i][j] == '#':
                i += 1
            i_fin = i
            i = i_start
            while i_start < i_fin + 1:
                k = j_start
                while k < j_fin + 1:
                    mas[i_start] = mas[i_start][:k] + '.' + mas[i_start][k + 1:]
                    k += 1
                i_start += 1
            counter += 1
        j += 1
    i += 1
print(counter)
