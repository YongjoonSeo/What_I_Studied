def BT(n):
    global cnt, N
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if not visited[i]:
            p1 = p2 = m1 = m2 = 1
            isTrue = False
            while n+p1 < N and i+p1 < N:
                if field[n+p1][i+p1]:
                    isTrue = True
                    break
                p1 += 1
            if isTrue: continue
            while n+p2 < N and i-p2 >= 0:
                if field[n+p2][i-p2]:
                    isTrue = True
                    break
                p2 += 1
            if isTrue: continue
            while n-m1 >= 0 and i-m1 >= 0:
                if field[n-m1][i-m1]:
                    isTrue = True
                    break
                m1 += 1
            if isTrue: continue
            while n-m2 >= 0 and i+m2 < N:
                if field[n-m2][i+m2]:
                    isTrue = True
                    break
                m2 += 1
            if isTrue: continue
            visited[i] = 1
            field[n][i] = 1
            BT(n+1)
            visited[i] = 0
            field[n][i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [[0 for i in range(N)] for j in range(N)]
    visited = [0 for i in range(N)]
    cnt = 0
    BT(0)
    print('#{0} {1}'.format(t, cnt))