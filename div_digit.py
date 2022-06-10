def divdigit(n):
    str_n = str(n)
    i = 0
    counter = 0
    leng = len(str_n)
    while i < leng:
        if str_n[i] != '0' and n % int(str_n[i]) == 0:
            counter += 1
        i += 1
    return counter
