res = set()
f = open('anna.txt', 'r')
inp = f.readline()
counter = 1
#res.add(inp)
while len(inp):
    inp = f.readline()
    counter += 1
print(counter)
f.close()
"""
    inp = f.readline().split()
    if counter < 75:
        res.add(inp)
"""
