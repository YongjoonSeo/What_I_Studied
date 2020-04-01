class Node:
    def __init__(self, idx, data=None):
        self.data = data
        self.idx = idx
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)
    
class BST:
    def __init__(self, N):
        self.head = Node(1)
        temphead = self.head
        q = [temphead]
        i = 2
        while q and i <= N:
            v = q.pop(0)
            while not v.left or not v.right:
                if i <= N:
                    if not v.left:
                        v.left = Node(i)
                        i += 1
                        continue
                    elif not v.right:
                        v.right = Node(i)
                        i += 1
                        continue
                else:
                    break
            q.append(v.left)
            q.append(v.right)
    
    @staticmethod
    def Inorder_traversal(node):
        global n
        if node == None: return
        BST.Inorder_traversal(node.left)
        node.data = n
        n += 1
        BST.Inorder_traversal(node.right)
    
    @staticmethod
    def Preorder_traversal(node, target):
        global result
        if node == None: return
        elif node.idx == target:
            result = node.data
            return
        else:
            BST.Preorder_traversal(node.left, target)
            BST.Preorder_traversal(node.right, target)    

T = int(input())
for t in range(1, T+1):
    n = 1
    N = int(input())
    result = 0
    tree = BST(N)
    BST.Inorder_traversal(tree.head)
    root = tree.head.data
    BST.Preorder_traversal(tree.head, N//2)

    print('#{0} {1} {2}'.format(t, root, result))






