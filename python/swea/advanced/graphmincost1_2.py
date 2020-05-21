def Find(x):
    if parents[x] == None:
        return x
    parents[x] = Find(parents[x])
    return parents[x]

def Union(x, y):
    xroot = Find(x)
    yroot = Find(y)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def kruskal(G, N):
    mst = []
    mst_cost = 0
    G.sort(key=lambda x: x[2])
    i = 0
    while len(mst) < N-1:
        s, e, val = G[i]
        if Find(s) != Find(e):
            Union(s, e)
            mst.append((s, e))
            mst_cost += val
        i += 1
    return mst_cost


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    edges = []
    for e in range(E):
        s, e, val = map(int, input().split())
        edges.append((s, e, val))

    parents = [None for i in range(V+1)]
    ranks = [0 for i in range(V+1)]

    print('#{0} {1}'. format(t, kruskal(edges, V+1)))
