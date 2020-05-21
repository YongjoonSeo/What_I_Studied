class Node:
    def __init__(self, val):
        self.parent = self
        self.next = None
        self.data = val

    def __repr__(self):
        return self.data

class linkedlist:
    def __init__(self, val):
        self.head = Node(val)
        self.length = 1
        self.tail = self.head

    def union(self, llist):
        assert self.length >= llist.length
        self.tail = llist.head
        temphead = llist.head
        while temphead:
            temphead.parent = self.head
            temphead = temphead.next
        self.length += llist.length

    def find(self):
        return self.head.parent

elements1 = ['a', 'd', 'e']
elements2 = ['b', 'f']

linkedlist1 = linkedlist(elements1[0])
linkedlist1.union(linkedlist(elements1[1]))
linkedlist1.union(linkedlist(elements1[2]))

linkedlist2 = linkedlist(elements2[0])
linkedlist2.union(linkedlist(elements2[1]))

print('before union')
print(linkedlist1.find())
print('length:', linkedlist1.length)

linkedlist1.union(linkedlist2)

print('after union')
print(linkedlist1.find())
print('length:', linkedlist1.length)