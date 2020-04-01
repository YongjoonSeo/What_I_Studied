def facto(n):
    if n == 1: return 1
    return n * facto(n-1)

def Combi(arr, start, r):
    global N, half, num
    if num == half: return
    if r == 0:
        cases.append(arr)
        num += 1
        return
    for i in range(start, N-r+1):
        Combi(arr+[i], i+1, r-1)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    half = facto(N) // (facto(N//2)*facto(N//2)) // 2
    num = 0
    cases = []
    result = float('inf')
    Combi([], 0, N//2)

    for case in cases:
        rest = set(range(N)) - set(case)
        diff = 0
        for i in case:
            for j in case: diff += field[i][j]
        for i in rest:
            for j in rest: diff -= field[i][j]
        result = min(result, abs(diff))

    print('#{0} {1}'.format(t, result))