"""
s = input()
wablon = input()
counter = s.count(wablon[:wablon.find('@')])
ind = s.find(wablon[:wablon.find('@')])
while counter > 0:
    i = 0
    j = ind
    flag = 1
    while i < len(wablon) and j < len(s):
        #print(wablon[i], s[j])
        if wablon[i] != s[j]:
            if wablon[i] != '@':
                flag = 0
                break
        i += 1
        j += 1
    if counter == 1 and len(s) - s.rfind(wablon[:wablon.find('@')]) < len(wablon):
        flag = 0
        ind = -1
        break
    if flag:    break
    else:   ind = s.find(wablon[:wablon.find('@')], j)
    counter -= 1
print(ind)
"""


s = input()
w = input()
subz = w[:w.find('@')]
copy_s = s
rez = -1
iterr = 1
while subz in s:
    i = s.find(subz)
    rez = i
    j = 0
    while j < len(w) and i < len(s):
        print(w[j], s[i])
        if w[j] == s[i] or w[j] == '@':
            j += 1
            i += 1
        else:
            rez = -1
            break
    print(rez)
    if j != len(w): rez = -1
    s = s[s.find(subz) + 1:]
    iterr += 1
print(copy_s)
print(s)
if rez != -1:
    print(copy_s.find(subz, copy_s.find(s) - len(w) - iterr))
else:
    print(-1)





    
