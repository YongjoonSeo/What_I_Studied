# 상호배타 집합으로 합친 다음
# parents를 모두 find해서 갱신하고 -> 동시에 set에 담아서 개수
# root node가 다른 것의 개수를 세어보자. (set에 담아서 개수)

def Find(n):
    if parents[n] == n:
        return n
    parents[n] = Find(parents[n])
    return parents[n]

def Union(x, y):
    xroot = Find(x)
    yroot = Find(y)
    if rank[xroot] >= rank[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if rank[xroot] == rank[yroot]:
        rank[xroot] += 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    parents = [i for i in range(N)]
    rank = [0 for i in range(N)]
    for i in range(0, M*2, 2):
        s, e = lst[i]-1, lst[i+1]-1
        Union(s, e)

    resultset = set()
    for i in range(len(parents)):
        resultset.add(Find(i))

    print('#{0} {1}'.format(t, len(resultset)))