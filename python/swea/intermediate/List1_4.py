T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    raw = list(map(int, input().split()))
    result = []
    for j in range(M, N+1):
        result.append(sum(raw[j-M:j]))
    print('#{0} {1}'.format(i, max(result) - min(result)))