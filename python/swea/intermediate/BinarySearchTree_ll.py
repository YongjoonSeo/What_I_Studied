class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

class BinarySearchTree:

    def __init__(self, *args):
        self.displst = []
        if args: 
            self.head = Node(args[0])
            self.displst.append(args[0])
        else: self.head = None
        for i in range(1, len(args)):
            self.Insert(args[i])
        
    def Search(self, val):
        node = Node(val)
        temphead = self.head
        while temphead:
            if temphead.data == node.data:
                return temphead
            elif temphead.data < node.data:
                if not temphead.right:
                    return False, temphead
                temphead = temphead.right
            else:
                if not temphead.left:
                    return False, temphead
                temphead = temphead.left
    
    def Insert(self, val):
        node = Node(val)
        temphead = self.Search(val)
        if type(temphead) == tuple: # val값을 가지는 노드를 찾지 못한 경우
            temphead = temphead[1]
        elif temphead:
            raise ValueError # BST에서는 중복된 값을 가질 수 없다.

        if node.data < temphead.data:
            temphead.left = node
            self.displst.append(val)
        else:
            temphead.right = node
            self.displst.append(val)
    
    def Delete(self, val):
        temphead = self.head # temphead: 삭제할 노드
        prevhead = None # prevhead: 삭제할 노드(temphead)의 부모 노드
        while temphead:
            if temphead.data == val: # 제거해야할 때
                if not temphead.left and not temphead.right: 
                    # (1) 자식 노드가 없는 경우
                    temphead = None
                    break
                elif temphead.left and temphead.right:
                    # (2) 자식 노드가 두 개 - 왼쪽 가지에서 최대 노드를 찾는다
                    # 1. 찾은 최대 노드(readj)의 부모 노드와 링크를 끊어준다
                    # 2. 찾은 최대 노드(readj)를 삭제할 노드의 부모, 자식 노드
                    #     (temphead의 부모, 자식 노드) 모두와 링크해준다.
                    readj = temphead.left # readj: 삭제 후 트리를 재조정할 최대 노드
                    prevreadj = None # prevreadj: readj의 부모 노드
                    while readj.right:
                        prevreadj = readj
                        readj = readj.right
                    
                    # 1번 과정.
                    # 찾은 최대 노드의 왼쪽 서브트리가 있는 경우 readj의 부모 노드와 연결하고,
                    # 그렇지 않으면 자식 노드가 없는 것이므로 None으로 변경한다.
                    if readj.left: 
                        prevreadj.right = readj.left
                    else:
                        prevreadj.right = None
                    
                    # 2번 과정.
                    if prevhead.data < readj.data:
                        prevhead.right = readj
                    else:
                        prevhead.left = readj
                    readj.left = temphead.left
                    readj.right = temphead.right
                    break

                else:
                    # (3) 자식 노드가 한 개 - 삭제한 노드의 위치로 자식 노드를 이동한다.
                    if temphead.left: childhead = temphead.left
                    elif temphead.right: childhead = temphead.right
                    if prevhead.data < childhead.data:
                        prevhead.right = childhead
                    else:
                        prevhead.left = childhead
                    break
            elif temphead.data < val:
                prevhead = temphead
                temphead = temphead.right
            else:
                prevhead = temphead
                temphead = temphead.left
        else:
            raise ValueError # 트리에 없는 값을 제거할 수 없다.
        self.displst.remove(val)

    def __repr__(self):
        return str(self.displst)




sample = BinarySearchTree(15, 9, 23, 3, 12, 17, 28, 8)
print(sample, end='\n\n')

sample.Insert(1)
print(sample, end='\n\n')

sample.Insert(4)
print(sample, end='\n\n')

sample.Delete(28)
print(sample, end='\n\n')

sample.Delete(8)
print(sample, end='\n\n')

sample.Delete(9)
print(sample)