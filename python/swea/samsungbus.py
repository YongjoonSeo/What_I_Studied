T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = [0 for i in range(5002)]
    result = []
    for n in range(N):
        s, e = map(int, input().split())
        for i in range(s, e+1):
            lst[i] += 1
    P = int(input())
    for p in range(P):
        idx = int(input())
        result.append(lst[idx])
    
    print('#{0}'.format(t), end=' ')
    print(*result)