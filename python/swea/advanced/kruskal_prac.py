def Find(parents, idx):
    if parents[idx] == idx:
        return idx
    parents[idx] = Find(parents, parents[idx])
    return parents[idx]

def Union(parents, rank, x, y):
    xroot = Find(parents, x)
    yroot = Find(parents, y)
    if rank[xroot] >= rank[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if rank[xroot] == rank[yroot]:
        rank[xroot] += 1

edges = [(0, 1, 32), (0, 2, 31), (0, 6, 51), (0, 5, 60), (1, 2, 21), (2, 4, 46), (6, 2, 25), (6, 4, 51), (3, 4, 34), (3, 5, 18), (5, 4, 40)]
N = 7
p = [i for i in range(N)]
r = [0 for i in range(N)]
mst= []
mst_cost = 0
edges.sort(key=lambda x: x[2])
for edge in edges:
    s, e, val = edge
    if Find(p, s) != Find(p, e):
        Union(p, r, s, e)
        mst.append((s,e))
        mst_cost += val

print(mst)
print(mst_cost)