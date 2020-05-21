class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def orderadd(self, data):
        if not self.head:
            node = Node(data)
            self.head = node
            return node.data
        elif not self.head.next:
            if data < self.head.data:
                node = Node(data)
                node.next = self.head
                self.head = node
            elif data == self.head.data:
                node = Node(data+1)
                self.head.next = node
            else:
                node = Node(data)
                self.head.next = node
            return node.data
        else:
            temphead = self.head
            if data < temphead.data:
                node = Node(data)
                node.next = self.head
                self.head = node
                return node.data
            elif data == temphead.data:
                data += 1
                while temphead.next and (temphead.next.data == data):
                    temphead = temphead.next
                    data += 1
                node = Node(data)
                nextnode = temphead.next
                temphead.next = node
                node.next = nextnode
                return node.data
            else:
                while temphead.next and (data > temphead.next.data):
                    temphead = temphead.next
                if temphead.next:
                    # print(temphead.next.data, end='<<\n')
                    # if data == 7: print('here')
                    if temphead.next.data == data:
                        while temphead.next and (temphead.next.data == data):
                            data += 1
                            temphead = temphead.next
                        node = Node(data)
                        nextnode = temphead.next
                        temphead.next = node
                        node.next = nextnode
                    else:
                        node = Node(data)
                        nextnode = temphead.next
                        temphead.next = node
                        node.next = nextnode
                    return node.data
                else:
                    if temphead.data == data:
                        node = Node(data+1)
                    else:
                        node = Node(data)
                    temphead.next = node
                    return node.data

def solution(k, room_number):
    answer = []
    rooms = linkedlist()
    for room in room_number:
        val = rooms.orderadd(room)
        answer.append(val)
    return answer

print(solution(10, [1,3,4,1,3,1]))

# a = linkedlist()
# bb = [7,5,1,2,3,1,7,6,2]
# for b in bb:
#     d = a.orderadd(b)
#     print(d)
# print('-------------')
# temphead = a.head
# while temphead:
#     print(temphead.data)
#     temphead = temphead.next