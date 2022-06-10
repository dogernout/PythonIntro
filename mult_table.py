n, m = eval(input())

# input
N, M = [int(i) for i in input().split(',')]

num_size = len(str(N))
result_size = len(str(N*N))

print('=' * M)

pos = 0
i = 1
while i < N+1:
    for j in range(1, N+1):
        num1 = i
        line = []
        while num1 < N+1:
        
            s = ''
            
            s += str(num1).rjust(num_size) + ' * '
            s += str(j).ljust(num_size) + ' = '
            s += str(num1*j).ljust(result_size) 
            
            if pos + len(s) > M:
                pos = 0
                break
        
            pos += len(s) + 3
            num1 += 1
            line.append(s)
        
        print(*line, sep=' | ')   
        
        if num1 == N+1:
            pos = 0
        
    i += num1 - i
    print('=' * M)
