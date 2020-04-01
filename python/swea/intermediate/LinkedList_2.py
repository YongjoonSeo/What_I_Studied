# from collections import deque

# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     deck = deque()

#     for i in range(M):
#         inpdeck = deque(list(map(int, input().split())))
#         if i == 0:
#             deck.append(inpdeck)
#         else:
#             for j in range(len(deck)):
#                 if type(deck[j]) == deque:



#                 if deck[j] > inpdeck[0]:
#                     deck.insert(j+k, inpdeck)
#                     break
#             else:
#                 deck.append(inpdeck)
    
#     result = []
#     temp = None
#     while len(result) < 10:
#         if not temp:
#             temp = deck.pop()
#             continue
#         if type(temp) != deque:
#             result.append(temp)
#             temp = None
#         else:
#             if temp:
#                 result.append(temp.pop())
    
#     print('#{0}'.format(t), end=' ')
    # print(*result)

# # 시간 초과 8개 --> 인풋 받는 리스트도 덱으로 받아서 왼쪽부터 뽑아서 넣어보자. --> 똑같이 시간 초과 8개.

# T = int(input())
# for t in range(1, T+1):
#     N, M = map(int, input().split())
#     lst = []

#     for i in range(M):
#         templst = list(map(int, input().split()))
#         if i == 0:
#             lst.extend(templst)
#         else:
#             for j in range(len(lst)):
#                 if lst[j] > templst[0]:
#                     for k in range(len(templst)):
#                         lst.insert(j+k, templst[k])
#                     break
#             else:
#                 lst.extend(templst)
    
#     print('#{0}'.format(t), end=' ')
#     print(*lst[:-11:-1])

# # 시간 초과 7개

# import sys
# sys.stdin = open('sample_input.txt', 'r')

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self, *args):
        self.head = Node(args[0])
        self.count = 1
        temphead = self.head
        for i in range(1, len(args)):
            node = Node(args[i])
            temphead.next = node
            temphead = node
            self.count = self.count + 1
    
    def get(self, idx):
        tempidx = idx
        temphead = self.head
        while tempidx > 0:
            temphead = temphead.next
            tempidx -= 1
        return temphead

    def length(self):
        return self.count
    
    def add(self, idx, llst):
        if idx == 0:
            llst.get(llst.length()-1).next = self.head
            self.head = llst.get(0)
        else:
            temphead = self.get(idx-1)
            nextnode = temphead.next
            temphead.next = llst.head
            llst.get(llst.length()-1).next = nextnode
        self.count = self.count + llst.count

    def __repr__(self):
        result = []
        temphead = self.head
        while temphead:
            result.append(str(temphead))
            temphead = temphead.next
        return ' '.join(result)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(M):
        raw = list(map(int, input().split()))
        inp = LinkedList(*raw)
        if i == 0:
            lst = inp
        else:
            for i in range(lst.length()):
                if lst.get(i).data > inp.get(0).data:
                    lst.add(i, inp)
                    break
            else:
                lst.add(lst.length(), inp)
    
    result = []
    i = 1
    while i <= 10 and i <= lst.length():
        result.append(lst.get(lst.length()-i).data)
        i += 1
    
    print('#{0}'.format(t), end=' ')
    print(*result)
