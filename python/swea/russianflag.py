def count(w, b):
    global result, N, M
    cnt = 0
    for i in range(w+1):
        for j in range(M):
            if field[i][j] != 'W':
                cnt += 1
                if cnt > result: return
    for i in range(w+1, b+1):
        for j in range(M):
            if field[i][j] != 'B':
                cnt += 1
                if cnt > result: return
    for i in range(b+1, N):
        for j in range(M):
            if field[i][j] != 'R':
                cnt += 1
                if cnt > result: return
    result = min(cnt, result)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(input()) for j in range(N)]
    result = 2501

    for i in range(N-2):
        for j in range(i+1, N-1):
            count(i, j)

    print('#{0} {1}'.format(t, result))


    # for _ in range(len(field)):
    #     print(field[_])