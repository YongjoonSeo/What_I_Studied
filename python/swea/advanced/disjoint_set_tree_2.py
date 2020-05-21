def Find(x):
    if parents[x] == x:
        return x
    parents[x] = Find(parents[x])
    return parents[x]

def Union(x, y):
    xroot = Find(x)
    yroot = Find(y)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot # y를 루트로 하는 트리를 x를 루트로 하는 트리에 합친다.
    else:
        parents[xroot] = yroot # x를 루트로 하는 트리를 y를 루트로 하는 트리에 합친다.
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

parents = [i for i in range(10)]
# 원소가 10개 있는 경우.
# i번째 항목의 값이 i라고 선언하는 것 자체가 각각의 트리를 만든 것이라 보면 된다.
# 인덱스는 각 항목, 값은 부모 노드로 볼 수 있다.
ranks = [0 for i in range(10)]
# 루트 노드가 i인 트리의 랭크 값 저장

print('Initial root nodes and ranks : ')
print(parents)
print(ranks)
print('------------------------------')

Union(2, 3)
Union(4, 5)
Union(2, 4)

print('Root nodes and ranks after Union : ')
print(parents)
print(ranks)
print('------------------------------')

print(Find(5))
print('After find(5) : ')
print(parents)
print('Root node for 5 has been updated')