import sys
input = sys.stdin.readline


def find(x, parents):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def union(x, y, parents, ranks):
    xroot = find(x, parents)
    yroot = find(y, parents)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
    else:
        parents[xroot] = yroot
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1
    
def solution():
    n, m = map(int, input().split())
    parents = [i for i in range(n+1)]
    ranks = [0 for i in range(n+1)]
    for _ in range(m):
        sw, a, b = map(int, input().split())
        if sw == 0: union(a, b, parents, ranks)
        else:
            if find(a, parents) == find(b, parents):
                print('YES')
            else:
                print('NO')

if __name__ == '__main__':
    solution()
