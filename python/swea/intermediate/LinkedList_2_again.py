class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self, *args):
        self.length = 0
        if args:
            for i in range(len(args)):
                if i == 0:
                    self.head = Node(args[i])
                    temphead = self.head
                else:
                    temphead.next = Node(args[i])
                    temphead = temphead.next
                self.length += 1
        else:
            self.head = None
    
    def get(self, idx):
        if abs(idx) > self.length or idx == self.length:
            raise IndexError('list index out of range')
        elif idx < 0:
            idx -= -self.length
        temphead = self.head
        for i in range(idx):
            temphead = temphead.next
        return temphead

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    seq = linkedlist(*list(map(int, input().split())))
    
    for i in range(M-1):
        inp = linkedlist(*list(map(int, input().split())))
        inphead = inp.head
        inptail = inp.get(-1)
        seqtarget = seq.head
        seqprev = None
        while seqtarget:
            if seqtarget.data > inphead.data:
                break
            seqprev = seqtarget
            seqtarget = seqtarget.next
        if not seqprev:
            inptail.next = seq.head
            seq.head = inphead
        else:
            seqprev.next = inphead
            inptail.next = seqtarget
        seq.length += inp.length
    
    result = []
    val = seq.get(-10)
    while val:
        result.append(val.data)
        val = val.next
    result.reverse()
    print('#{0}'.format(t), end=' ')
    print(*result)