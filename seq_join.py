from itertools import *


def joinseq(*seq):
    #print(seq)
    mas_cur_min = []
    i = 0
    leng = len(seq)
    itera_seq = iter(seq)
    double_iter = []
    while i < leng:
        double_iter.append(iter(next(itera_seq)))
        i += 1
    i = 0
    while i < leng:
        mas_cur_min.append(next(double_iter[i], 'aboba'))
        i += 1
    cur_min = max(mas_cur_min)
    cur_max = cur_min
    counter_abob = -1
    flag = 1
    #print(mas_cur_min)
    while counter_abob < leng:
        if counter_abob == leng - 1:
            i = 0
            while i < leng:
                if mas_cur_min[i] != 'aboba':
                    break
                i += 1
            min_ind = i
            #print(mas_cur_min, min_ind)
            yield mas_cur_min[min_ind]
            cur_min = next(double_iter[min_ind], 'aboba')
            while cur_min != 'aboba':
                yield cur_min
                cur_min = next(double_iter[min_ind], 'aboba')
            #yield next(double_iter[min_ind])
            break
        i = 0
        min_ind = 0
        counter_abob = 0
        #cur_min = cur_max
        cur_min = cur_max * 100
        while i < leng:
            if mas_cur_min[i] == 'aboba':
                counter_abob += 1
            elif mas_cur_min[i] < cur_min:
                cur_min = mas_cur_min[i]
                min_ind = i
            elif mas_cur_min[i] > cur_max:
                cur_max = mas_cur_min[i]
            i += 1
        yield cur_min
        mas_cur_min[min_ind] = next(double_iter[min_ind], 'aboba')
    return




    
    """

[range(30, 36), range(35, 49), range(40, 64),
range(45, 81), range(50, 100), range(55, 121)]
    while i < leng:
        mas_cur_min.append(next(seq[i], 'aboba'))
        i += 1
    cur_min = mas_cur_min[-1]
    counter_abob = -1
    flag = 1
    while counter_abob < leng:
        i = 0
        min_ind = 0
        counter_abob = 0
        while i < leng:
            if mas_cur_min[i] == 'aboba':   counter_abob += 1
            elif mas_cur_min[i] < cur_min:
                cur_min = mas_cur_min[i]
                min_ind = i
            i += 1
        yield cur_min
        mas_cur_min[min_ind] = next(seq[min_ind], 'aboba')
    return
    """
    
#print("".join(joinseq("abs", "qr", "azt")))

"""
def joinseq(*seq):
    seq_concat = list(chain.from_iterable(seq))
    while len(seq_concat):
        yield seq_concat.pop(seq_concat.index(min(seq_concat)))
    return
"""
