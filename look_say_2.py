#import time


#start_time = time.time()

def LookSay():
    #mas_konv = ['1', '11', '21', '1211']
    mas_konv = '1211'
    yield 1
    yield 1
    yield 1
    yield 2
    yield 1
    yield 1
    yield 2
    yield 1
    yield 1
    while 1:
        i = 0
        next_num = ''
        leng = len(mas_konv)
        while i < leng:
            counter = 1
            cur_num = ''
            while i < leng - 1 and mas_konv[i] == mas_konv[i + 1]:
                counter += 1
                i += 1
            cur_num += str(counter)
            if counter > 1: cur_num += mas_konv[i - 1]
            else: cur_num += mas_konv[i]
            next_num += cur_num
            i += 1
        mas_konv = next_num
        j = 0
        while j < len(mas_konv):
            yield int(mas_konv[j])
            j += 1

"""
L = LookSay()
for i in range(1205000):
    n = next(L)
print(n)
#print(' === {} seconds ==='.format(time.time() - start_time))

"""
