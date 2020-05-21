N = int(input())
binnums = list(map(int, input()))
tree = dict()
nodes = [0] * (len(binnums) + 1)
idx = head = parent = node = 0
for binnum in binnums:
    idx += 1
    if binnum == 0:
        node += 1
        parent = head
        head = node
        tree[head] = parent
        nodes[idx] = head
    else:
        nodes[idx] = head
        head = tree.get(head)
        parent = tree.get(head)

rot1, rot2 = map(int, input().split())
if nodes[rot1] == nodes[rot2]:
    result = [rot1, rot2]
else:
    temp = []
    isfound = False
    target = 0
    rot1 = nodes[rot1]
    rot2 = nodes[rot2]
    while rot1:
        temp.append(rot1)
        rot1 = tree.get(rot1)
    while rot2:
        for p in temp:
            if p == rot2:
                target = p
                isfound = True
                break
        if isfound: break
        rot2 = tree.get(rot2)

    result = []
    for i in range(1, len(nodes)):
        if nodes[i] == target:
            result.append(i)
        if len(result) == 2: break

print(*result)

# print(nodes)