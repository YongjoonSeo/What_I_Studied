T = int(input())
for t in range(1, T+1):
    n = int(input())
    field = [[i for i in list(map(int, input().split()))] for j in range(n)]
    result = []

    for i in range(n):
        for j in range(n):
            if field[i][j] > 0:
                h = v = 0
                while j+h < n and field[i][j+h] > 0: h += 1
                while i+v < n and field[i+v][j] > 0: v += 1
                for a in range(i, i+v):
                    for b in range(j, j+h):
                        field[a][b] = -1
                if not result:
                    result.append(v)
                    result.append(h)
                else:
                    for k in range(0, len(result), 2):
                        if h * v <= result[k] * result[k+1]:
                            result.insert(k, v)
                            result.insert(k+1, h)
                            break
                        elif h * v == result[k] * result[k+1]:
                            if v < result[k]:
                                result.insert(k, v)
                                result.insert(k+1, h)
                                break
                    else:
                        result.append(v)
                        result.append(h)
    
    print('#{0} {1}'.format(t, len(result)//2), end=' ')
    print(*result)




    # for _ in range(len(field)):
    #     print(field[_])