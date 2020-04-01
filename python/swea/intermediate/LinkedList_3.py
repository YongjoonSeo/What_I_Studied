T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    i = 0
    for _ in range(K):
        i = (i + M) 
        if i == len(lst):
            lst.append(lst[-1] + lst[0])
        else:
            i %= len(lst)
            lst.insert(i, lst[i-1] + lst[i])
    
    result = []
    j = 1
    while j <= len(lst) and j <= 10:
        result.append(lst[len(lst) - j])
        j += 1
    
    print('#{0}'.format(t), end=' ')
    print(*result)
