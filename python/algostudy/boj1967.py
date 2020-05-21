import sys
sys.setrecursionlimit(1000000)

def post(key):
    global result
    child = tree.get(key)
    childval = []
    for i in child:
        if tree.get(i):
            childval.append(child.get(i) + post(i))
        else:
            childval.append(child.get(i))
    if len(childval) == 1:
        result = max(result, childval[0])
        return childval[0]
    else:
        maxval = max(childval)
        childval.remove(maxval)
        secondval = max(childval)
        result = max(result, maxval + secondval)
        return maxval


tree = dict()
n = int(input())
if n == 1: print(0)
else:
    for i in range(n-1):
        p, c, val = map(int, input().split())
        if tree.get(p):
            tree[p][c] = val
        else:
            tree[p] = {c: val}
    result = -1

    post(1)
    print(result)