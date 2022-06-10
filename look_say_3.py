#import time


from collections import deque


#start_time = time.time()


def LookSay():
    mas_konv = deque([1, 0])
    counter = 0
    next_num = 1
    while 1:
        cur_num = mas_konv.popleft()
        if not cur_num - next_num:  counter += 1
        elif next_num:
            mas_konv.append(counter)
            mas_konv.append(next_num)
            next_num = cur_num
            counter = 1
        else:
            mas_konv.append(next_num)
            next_num = cur_num
            counter = 1
        if cur_num: yield cur_num
    
            
"""       
L = LookSay()
for i in range(1205000):
    n = next(L)
print(n)

#print('=== {} seconds ==='.format(time.time() - start_time))
"""
