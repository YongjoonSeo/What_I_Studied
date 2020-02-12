def Palincnt(lst, n):
    raw = lst[:]
    cnt = 0
    for i in range(len(lst)-n+1):
        if raw[i:i+n] == raw[i+n-1 - len(lst):i - len(lst) - 1:-1]:
            cnt += 1
    return cnt

for t in range(1, 11):
    L = int(input())
    field = [[i for i in list(input())] for j in range(8)]
    result = 0

    for i in range(8):
        tempv = []
        for j in range(8):
            tempv.append(field[j][i])
        result += Palincnt(field[i], L)
        result += Palincnt(tempv, L)

    print('#{0} {1}'.format(t, result))