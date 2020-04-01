from collections import deque

T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    q = deque(list(input()))
    startpoint = q.copy()
    result = set()
    q.rotate()

    while q != startpoint:
        for i in range(4):
            temp = ''
            for j in range(N//4):
                temp += q[i*(N//4)+j]
            result.add(temp)
        q.rotate()
    else:
        for i in range(4):
            temp = ''
            for j in range(N//4):
                temp += q[i*(N//4)+j]
            result.add(temp)
    resultlst = [int(i, 16) for i in result]
    resultlst.sort(reverse=True)
    print('#{0} {1}'.format(t, resultlst[K-1]))