def Re(field):
    cnt1 = cnt2 = 0
    for i in range(8):
        for j in range(8):
            if (i+j) & 1:
                if field[i][j] == 'B': cnt1 += 1
                elif field[i][j] == 'W': cnt2 += 1
            else:
                if field[i][j] == 'W': cnt1 += 1
                elif field[i][j] == 'B': cnt2 += 1
    return min(cnt1, cnt2)

N, M = map(int, input().split())
inp = [list(input()) for _ in range(N)]
result = 65

for i in range(N-7):
    for j in range(M-7):
        field = [[inp[n][m] for m in range(j, j+8)] for n in range(i, i+8)]
        temp = Re(field)
        if temp < result:
            result = temp

print(result)