import sys
input = sys.stdin.readline


def find(x, parents):
    if parents[x] == x: return x
    parents[x] = find(parents[x], parents)
    return parents[x]

def howmany(x, parents, nums):
    if parents[x] == x: return nums[x]
    nums[x] = howmany(parents[x], parents, nums)
    return nums[x]

def union(x, y, parents, ranks, nums):
    xroot = find(x, parents)
    yroot = find(y, parents)
    if xroot == yroot: return
    x_num = howmany(x, parents, nums)
    y_num = howmany(y, parents, nums)
    if ranks[xroot] >= ranks[yroot]:
        parents[yroot] = xroot
        nums[xroot] += y_num
    else:
        parents[xroot] = yroot
        nums[yroot] += x_num
    if ranks[xroot] == ranks[yroot]:
        ranks[xroot] += 1

def solution():
    F = int(input())
    friends = dict()
    parents = []
    ranks = []
    nums = []
    idx = 0
    for i in range(F):
        s, e = input().split()
        if friends.get(s) == None:
            friends[s] = idx
            parents.append(idx)
            ranks.append(0)
            nums.append(1)
            idx += 1
        if friends.get(e) == None:
            friends[e] = idx
            parents.append(idx)
            ranks.append(0)
            nums.append(1)
            idx += 1
        union(friends[s], friends[e], parents, ranks, nums)

        print(howmany(friends[s], parents, nums))

if __name__ == '__main__':
    for t in range(int(input())):
        solution()