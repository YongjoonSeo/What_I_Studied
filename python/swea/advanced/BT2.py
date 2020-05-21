# N종의 제품을 N개의 공장 중 한 곳당 한 가지씩 생산.
# BT(제품, val)

def BT(n, val):
    global result, N
    if val >= result: return
    if n == N:
        result = min(result, val)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            BT(n+1, val+field[n][i])
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    result = float('inf')
    visited = [0 for i in range(N)]

    BT(0, 0)
    print('#{0} {1}'.format(t, result))

    # for _ in range(len(field)):
    #     print(field[_])