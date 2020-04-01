def Counting(s):
    global cnt
    
    if not s:
        return
    else:
        cnt += 1
        for i in range(2):
            start = field[i][s]
            Counting(start)

T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    field = [[0 for i in range(E+2)] for j in range(2)]
    cnt = 1

    for i in range(E):
        p, c = lst[i*2], lst[i*2+1]
        if field[0][p] == 0:
            field[0][p] = c
        else:
            field[1][p] = c
    
    for i in range(2):
        start = field[i][N]
        Counting(start)

    print('#{0} {1}'.format(t, cnt))


    # for _ in range(len(field)):
    #     print(field[_])
