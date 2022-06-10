def squares(w, h, *args):
    s = ['.' * w for i in range(h)] # w * h
    leng = len(args)
    i = 0
    while i < leng:
        j = args[i][1] #str
        k = args[i][0] #col     s[j][k]
        counter = 0
        while counter < args[i][2]:
            s[j] = s[j][:k] + args[i][3] * args[i][2] + s[j][k + args[i][2]:]
            counter += 1
            j += 1
        i += 1

    i = 0
    while i < len(s):
        print(s[i])
        i += 1
    return


#squares(20,23,(1,1,5,'@'), (2,3,1,'!'), (4,5,11,'#'), (8,11,9,'/'))
