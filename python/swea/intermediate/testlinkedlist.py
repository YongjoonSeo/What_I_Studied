class Node: # 노드 클래스 안에는 데이터 필드와 링크 필드가 있다.

    def __init__(self, data):
        self.data = data # 데이터 필드
        self.next = None # 링크 필드
    
    def __repr__(self):
        return str(self.data)

class LinkedList:

    def __init__(self):
        self.head = None # 연결 리스트의 초기 헤드는 None이다. (head)
        self.count = 0

llist = LinkedList()
first = Node(1)
llist.head = first 
second = Node(2)
third = Node(3)

first.next = second
second.next = third

while llist.head:
    print(llist.head.data)
    llist.head = llist.head.next