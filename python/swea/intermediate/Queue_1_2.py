T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(input().split())

    for i in range(M):
        lst.append(lst.pop(0))
    
    print('#{0} {1}'.format(t, lst[0]))