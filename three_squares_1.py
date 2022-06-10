#import time


s = set(eval(input()))
#start_time = time.time()
m = max(s)
slag_1 = (i * i for i in range(1, int(m ** 0.5) + 1))
slag_2 = lambda x: (j * j for j in range(int(x ** 0.5), int((m - x) ** 0.5) + 1))
slag_3 = lambda x, y: (k * k for k in range(int(y ** 0.5), int((m - x - y) ** 0.5) + 1))
squares = {i + j + k for i in slag_1 for j in slag_2(i) for k in slag_3(i, j)}
print(len(squares & s))
#print('=== {} seconds ==='.format(time.time() - start_time))
