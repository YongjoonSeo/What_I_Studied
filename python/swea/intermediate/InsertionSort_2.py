from LinkedList import *

class LinkedListArgs(LinkedList):

    def __init__(self, *args):
        super().__init__()
        prevnode = None
        for arg in args:
            node = Node(arg)
            if not self.head:
                self.head = node
            else:
                prevnode.next = node
            prevnode = node
            self.count = self.count + 1

lst = LinkedListArgs(69, 10, 30, 2, 16, 8, 31, 22)

for i in range(1, lst.length()):
    idx = i
    while idx >= 0:
        if idx == 0:
            lst.addtoFirst(lst.delete(i))
        elif lst.get(idx-1).data <= lst.get(i).data:
            lst.add(idx, lst.delete(i))
            break
        idx -= 1

print(lst)