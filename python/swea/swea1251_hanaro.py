def Search(n):
    global N, result, E
    if n == 1:
        if tempcheck in checked: return
        else:
            for vertex in tempcheck:
                tempset = tempcheck - {vertex} | {(vertex[1], vertex[0])}
                checked.append(tempset)            
        
        Lsq = 0
        lst = list(tempcheck)
        for i in range(len(lst)):
            x1, y1, x2, y2 = lst[i][0][0], lst[i][0][1], lst[i][1][0], lst[i][1][1]
            Lsq += (x2-x1) ** 2 + (y2-y1) ** 2
        result = min(result, Lsq*E)
        return
    else:
        for i in range(N-1):
            for j in range(i+1, N):
                if not visited[j]:
                    visited[j] = 1
                    tempcheck.add((V[i],V[j]))
                    Search(n-1)
                    visited[j] = 0
                    tempcheck.remove((V[i],V[j]))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    rawx = list(map(int, input().split()))
    rawy = list(map(int, input().split()))
    E = float(input())
    V = list(zip(rawx, rawy))
    visited = [0 for i in range(N)]
    tempcheck = set()
    checked = list()
    result = float('inf')

    Search(N)

    print('#{0} {1}'.format(t, int(result)))
