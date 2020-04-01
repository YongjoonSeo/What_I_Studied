from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

class Heap:
    def __init__(self):
        self.head = None

    def Getlast(self):
        temphead = self.head
        if temphead == None: return self.head
        q = deque([temphead])
        while q:
            v = q.popleft()
            
            for i in range(2):
                if not (i & 1):
                    if v.left == None:
                        return v, 'left'
                    q.append(v.left)
                else:
                    if v.right == None:
                        return v, 'right'
                    q.append(v.right)
    
    def Insert(self, val):
        node = Node(val)
        temphead = self.Getlast()
        if type(temphead) == tuple:
            if temphead[1] == 'left':
                temphead[0].left = node
                node.parent = temphead[0]
            elif temphead[1] == 'right':
                temphead[0].right = node
                node.parent = temphead[0]
            valhead = node
            while valhead.parent and valhead.parent.data > valhead.data:
                valhead.parent.data, valhead.data = valhead.data, valhead.parent.data
                valhead = valhead.parent                
        else:
            self.head = node
    
    def Ancestorsum(self):
        temphead = self.head
        if temphead == None: return 0
        total = 0
        q = deque([temphead])
        TF = False
        while q:
            v = q.popleft() 
            for i in range(2):
                if not (i & 1):
                    if v.left == None:
                        temphead = prevhead
                        TF = True
                        break
                    q.append(v.left)
                else:
                    if v.right == None:
                        temphead = v
                        TF = True
                        break
                    q.append(v.right)
            prevhead = v
            if TF == True: break
        
        while temphead:
            total += temphead.data
            temphead = temphead.parent
        return total

T = int(input())
for t in range(1, T+1):
    N = int(input())
    deck = deque(map(int, input().split()))
    heap = Heap()
    while deck:
        heap.Insert(deck.popleft())
    result = heap.Ancestorsum()
    print('#{0} {1}'.format(t, result))