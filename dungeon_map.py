dun_map = dict()
s = input().split()
while len(s) > 1:
    if s[0] not in dun_map:
        dun_map[s[0]] = {s[1]}
    else:
        dun_map[s[0]].add(s[1])
    if s[1] not in dun_map:
        dun_map[s[1]] = {s[0]}
    else:
        dun_map[s[1]].add(s[0])
    s = input().split()
st = s[0]
fin = input()
#print(dun_map)
out = {st}
len_cur = 0

while len_cur != len(out):
    len_cur = len(out)
    current = list(out)
    i = 0
    while i < len_cur:
        j = 0
        peweri = list(dun_map[current[i]])
        while j < len(peweri):
            out.add(peweri[j])
            j += 1
        i += 1
if fin in out:  print('YES')
else:   print('NO')
#print(out)
    

