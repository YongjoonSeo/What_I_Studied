T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    field = [list(map(int, input().split())) for j in range(N)]
    result = -1

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = 0
            for n in range(M):
                for m in range(M):
                    temp += field[i+n][j+m]
            result = max(result, temp)

    print('#{0} {1}'.format(t, result))


    # for _ in range(len(field)):
    #     print(field[_])