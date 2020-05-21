# visited 체크해가며 백트래킹 하면 될듯한데,
# 가장 마지막에 1로 돌아오는 것 필요 (visited 남은 개수가 1일 때(첫 자리만 남았을 때))
# 최소 넘어가는거면 잘라버리자

def BT(n, rest, val):
    global N, result
    if rest == 1:
        result = min(result, val+field[n][0])
        return
    for i in range(1, N):
        if not visited[i]:
            if val+field[n][i] >= result: continue
            visited[i] = 1
            BT(i, rest-1, val+field[n][i])
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    visited = [0 for i in range(N)]
    result = float('inf')

    BT(0, N, 0)
    print('#{0} {1}'.format(t, result))

    # for _ in range(len(field)):
    #     print(field[_])