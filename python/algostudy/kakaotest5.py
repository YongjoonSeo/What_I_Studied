class Node:
    def __init__(self, num, idx):
        self.num = num
        self.prev = None
        self.next = None
        self.idx = idx

class Linkedlist:
    def __init__(self, node=None):
        self.head = node
        
    def orderaddnode(self, num, idx):
        temphead = self.head
        prevhead = None
        while temphead != None and temphead.idx < idx:
            prevhead = temphead
            temphead = temphead.next
        node = Node(num, idx)
        if prevhead:
            prevhead.next = node
            node.next = temphead
            if temphead:
                temphead.prev = node
        else:
            self.head = node
            node.next = temphead
            if temphead:
                temphead.prev = node
        
    def addnode(self, num, idx):
        temphead = self.head
        prevhead = None
        while temphead != None:
            prevhead = temphead
            temphead = temphead.next
        node = Node(num, idx)
        if prevhead:
            prevhead.next = node
            node.next = temphead
            if temphead:
                temphead.prev = node
        else:
            self.head = node
            node.next = temphead
            if temphead:
                temphead.prev = node

    def findlongest(self):
        temphead = self.head
        tempidx = self.head.idx
        maxval = -1
        cnt = 1
        while temphead.next != None:
            temphead = temphead.next
            if temphead.idx == tempidx + 1:
                cnt += 1
            else:
                maxval = max(cnt, maxval)
                cnt = 1
            tempidx = temphead.idx
        return maxval 

def solution(stones, k):
    answer = 0
    zeros = Linkedlist()
    stone = Linkedlist()
    for i in range(len(stones)):
        stone.addnode(stones[i], i)
    
    while True:
        answer += 1
        temphead = stone.head
        while temphead != None:
            temphead.num -= 1
            if temphead.num == 0:
                zeros.orderaddnode(0, temphead.idx)
            temphead = temphead.next
        if zeros.findlongest() == k:
            break

    # while True:
    #     answer += 1
    #     for i in range(len(stones)):
    #         stones[i] -= 1
    #         if not stones[i]:
    #             zeros.addnode(i)
    #     if zeros.findlongest() == k:
    #         break
                
    return answer

stone =	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stone, k))