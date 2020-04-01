N, L = map(int, input().split())
field = [list(map(int, input().split())) for j in range(N)]
result = 0

for i in range(N):
    cnth = j = 1
    while j < N:
        if abs(field[i][j] - field[i][j-1]) > 1: break
        elif field[i][j] - field[i][j-1] == 1:
            if cnth < L: break
            else:
                cnth = 1
                j += 1
        elif field[i][j] - field[i][j-1] == -1:
            t = 0
            while j+t < N and field[i][j] == field[i][j+t] and t < L: t += 1
            if t == L: 
                j += t
                cnth = 0
            else: break
        else:
            cnth += 1
            j += 1
    else:
        result += 1
    
    cntv = j = 1
    while j < N:
        if abs(field[j][i] - field[j-1][i]) > 1: break
        elif field[j][i] - field[j-1][i] == 1:
            if cntv < L: break
            else:
                cntv = 1
                j += 1
        elif field[j][i] - field[j-1][i] == -1:
            t = 0
            while j+t < N and field[j][i] == field[j+t][i] and t < L: t += 1
            if t == L: 
                j += t
                cntv = 0
            else: break
        else:
            cntv += 1
            j += 1
    else:
        result += 1

print(result)

# for _ in range(N):
#     print(field[_])