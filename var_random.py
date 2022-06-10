from random import randint


#import copy


#import time


#from itertools import tee


def randomes(mas):
    #iter1, iter2 = tee(mas)
    iter_mas = iter(mas)
    mas_copy = []
    flag = 1
    while 1:
        cur_tuple = next(iter_mas, 'aboba')
        if cur_tuple == 'aboba':
            flag = 0
            iter_mas = iter(mas_copy)
            continue
        cur_tuple = list(cur_tuple)
        if flag:    mas_copy.append(cur_tuple)
        #print(cur_tuple)
        yield randint(cur_tuple[0], cur_tuple[1])
        #yield randint(next(cur_tuple), next(cur_tuple))

             

