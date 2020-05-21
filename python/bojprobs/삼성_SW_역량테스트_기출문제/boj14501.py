def BT(n, cnt):
    global N, result
    if n > N or (n + T[n] - 1) > N:
        result = max(result, cnt)
        return
    for i in range(1, N+1):
        if not visited[i] and i >= (n + T[n]):
            if (i + T[i] - 1) > N:
                result = max(result, cnt)
                continue
            visited[i] = 1
            BT(i, cnt + P[i])
            visited[i] = 0
    else:
        BT(n+N, cnt)

N = int(input())
T = [0]
P = [0]
visited = [0 for i in range(N+1)]
result = 0
for i in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

BT(0, 0)

print(result)

# print(T)
# print(P)