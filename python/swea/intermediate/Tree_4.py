# from collections import deque

# class Node:
#     def __init__(self, data=0)
#         self.data = data
#         self.left = None
#         self.right = None

#     def __repr__(self):
#         return str(self.data)

# class CBT:
#     def __init__(self, N=0):
#         self.head = Node()
#         num = 1
#         temphead = self.head
#         q = deque([temphead])
#         TF = False
#         while q:
#             v = q.popleft()
#             for i in range(2):
#                 if v.left == None:
#                     node = Node()
#                     v.left = node
#                     q.append(node)
#                     num += 1
#                 elif v.right == None:
#                     node = Node()
#                     v.right = node
#                     q.append(node)
#                     num += 1
#                 if num > N:
#                     TF = True
#                     break
#             if TF: break

def Values(idx, maxleng):
    if idx >= maxleng: return 0
    if idx*2 >= maxleng: return tree[idx]
    elif idx*2 + 1 >= maxleng: return Values(idx*2, maxleng)
    return Values(idx*2, maxleng) + Values(idx*2+1, maxleng)

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for i in range(N+1)]
    
    for i in range(M):
        idx, num = map(int, input().split())
        tree[idx] = num
    
    for j in range(1, N+1):
        tree[j] = Values(j, len(tree))

    print('#{0} {1}'.format(t, tree[L]))