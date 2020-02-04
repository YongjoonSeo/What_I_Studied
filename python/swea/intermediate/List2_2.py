T = int(input())
A = list(range(1,13))
for _ in range(1, T+1):
    N, K = map(int, input().split())
    result = 0
    for i in range(1<<12):
        temp = []
        for j in range(12):
            if i & (1<<j):
                temp.append(A[j-1])
        if len(temp) == N:
            if sum(temp) == K:
                result += 1
    
    print('#{0} {1}'.format(_, result))