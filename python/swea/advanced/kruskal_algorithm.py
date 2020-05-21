def Find(x):
    if parents[x] == x:
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

def MST_KRUSKAL(G):
    mst = [] # 최소 신장 트리
    mst_cost = 0 # 최소 신장 트리의 가중치

    G.sort(key=lambda x: x[2])  # 가중치의 오름차순으로 정렬
    print(G) # 오름차순으로 정렬된 간선

    while len(mst) < N-1:
        s, e, val = G.pop(0)
        if Find(s) != Find(e): # 같은 집합에 속해있지 않다면 (사이클이 존재하지 않는다면)
            Union(s, e) # 각각의 집합을 합친다.
            mst.append((s, e)) # 그때의 간선을 MST에 저장
            mst_cost += val # 그때의 가중치를 저장

            print(s, e, val) # 선택된 간선과 그 가중치
            print(parents, ranks)  # 상호 배타 집합 정보
            print('----------------')

    return mst, mst_cost


edges = [(0, 1, 32), (0, 2, 31), (0, 6, 51), (0, 5, 60), (1, 2, 21), (2, 4, 46), (6, 2, 25), (6, 4, 51), (3, 4, 34), (3, 5, 18), (5, 4, 40)]
N = 7 # N은 정점의 개수
parents = [i for i in range(N)]
ranks = [0 for i in range(N)]

print(MST_KRUSKAL(edges))
