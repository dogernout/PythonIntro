def check_counter(counter):
    if counter == 9: return 0
    return counter + 1


m, n = list(map(int, input().split(',')))   # m - stolb, n - string
mas = [[-1] * m for i in range(n)]
i = 0
j = -1
counter = 0
fuller = n * m
while fuller > 0:
    """
    print('fuller =', fuller)
    a = 0
    while a < n:
        b = 0
        while b < m:
            print(mas[a][b], end = ' ')
            b += 1
        print()
        a += 1
    """
    j += 1
    while j < m and mas[i][j] == -1:
        mas[i][j] = counter
        counter = check_counter(counter)
        fuller -= 1
        j += 1
    i += 1
    j -= 1
    #print(i, j, 111)
    while i < n and mas[i][j] == -1:
        mas[i][j] = counter
        counter = check_counter(counter)
        fuller -= 1
        i += 1
    i -= 1
    j -= 1
    #print(i, j, 222)
    while j > -1 and mas[i][j] == -1:
        mas[i][j] = counter
        counter = check_counter(counter)
        fuller -= 1
        j -= 1
    j += 1
    i -= 1
    #print(i, j, 333)
    while i > -1 and mas[i][j] == -1:
        mas[i][j] = counter
        counter = check_counter(counter)
        fuller -= 1
        i -= 1
    i += 1
    #print(i, j, 444)

i = 0
j = 0
while i < n:
    j = 0
    while j < m:
        print(mas[i][j], end = ' ')
        j += 1
    print()
    i += 1

    
#print(mas)
