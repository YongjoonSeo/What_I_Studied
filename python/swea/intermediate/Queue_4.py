from collections import deque

def BFS(s, e):
    q = deque()
    q.append(s)
    cnt = 0

    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()

            if not visited[v]:
                visited[v] = 1

            for i in range(1, V+1):
                if field[v][i] == 1 and not visited[i]:
                    if i == e: return cnt
                    else:
                        visited[i] = 1 
                        q.append(i) 
    
    return 0

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    field = [[0 for i in range(V+1)] for j in range(V+1)]
    visited = [0 for i in range(V+1)]

    for i in range(E):
        s, e = map(int, input().split())
        field[s][e] = 1
        field[e][s] = 1
    
    S, G = map(int, input().split())

    result = BFS(S, G)
    print('#{0} {1}'.format(t, result))

    # for _ in range(len(field)):
    #     print(field[_])