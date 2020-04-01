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


    def addtoFirst(self, node):
        # 1. head를 추가하는 노드로 옮기고 2. 추가하는 node를 본래 head 위치로 링크한다.
        temphead = self.head # 2번 과정을 수행하기 위한 준비과정
        self.head = node # 1번 과정 수행 완료
        self.head.next = temphead # 2번 과정 수행 완료
        self.count = self.count + 1
    

    def addtoLast(self, node):
        # 1. 연결 리스트의 마지막 노드에 접근해서 2. 그 노드를 추가하는 노드에 링크해준다.
        tempcnt = self.count
        temphead = self.head
        while tempcnt > 1:
            temphead = temphead.next
            tempcnt -= 1
        temphead.next = node
        self.count = self.count + 1


    def length(self):
        return self.count


    def get(self, idx):
        assert abs(idx) <= self.count and idx != self.count, IndexError.__name__
        temphead = self.head # 헤드는 바꿔주면 안 된다.
        if idx >= 0:
            while idx > 0:
                temphead = temphead.next
                idx -= 1
        else:
            while idx < -1:
                temphead = self.head
                idx += 1
        return temphead
        # temphead를 들어온 idx만큼 옮겨주고 그 노드에 저장된 데이터를 반환한다.
    

    def add(self, idx, node):
        if idx == 0 or idx < -self.count:
            # 들어오는 idx 값이 0이거나 리스트의 크기의 음수보다 작으면 가장 처음에 원소를 추가한다.
            LinkedList.addtoFirst(self, node)
            return
        elif idx >= self.count: 
            # 들어오는 idx 값이 리스트의 크기보다 크거나 같으면 가장 마지막에 원소를 추가한다.
            LinkedList.addtoLast(self, node)
            return
        else:
            temphead = self.head
            idx -= 1
            if idx >= 0:
                while idx > 0:
                    temphead = temphead.next
                    idx -= 1
            else:
                while idx < -1:
                    temphead = self.head
                    idx += 1
            # 노드를 추가하기 원하는 지점까지 이동한다.
            nextnode = temphead.next 
            # 간단히 말해서 a노드와 b노드 사이에 c노드를 추가하는 상황.
            # a노드: temphead // b노드: nextnode // c노드: node
            temphead.next = node # 이전 노드(a)의 링크를 추가하는 노드(c)로 바꾼다.
            node.next = nextnode # 추가하는 노드(c)의 링크를 이후 노드(b)로 걸어준다.
            self.count = self.count + 1


    def delete(self, idx): 
        # a b c 노드가 있으면 b를 제거한다고 가정했을 때
        # a의 링크를 c로 바꿔주기만 하면 된다.
        assert abs(idx) <= self.count and idx != self.count, IndexError.__name__
        if not self.head:
            print(self.head)
            raise IndexError.__name__
        
        if idx == 0: # idx가 0일 때는 head의 링크만 바꿔주면 된다.
            temp = self.head
            self.head = self.head.next
            self.count = self.count - 1
            return temp

        idx -= 1 # 목표 지점 바로 전 노드를 찾아야 한다.
        temphead = self.head
        if idx >= 0:
            while idx > 0:
                temphead = temphead.next
                idx -= 1
        else:
            while idx < -1:
                temphead = self.head
                idx += 1
        # temphead : a 노드
        temp = temphead.next
        temphead.next = temphead.next.next
        self.count = self.count - 1
        return temp


    def __repr__(self):
        temphead = self.head
        result = []
        while temphead:
            result.append(str(temphead.data))
            temphead = temphead.next
        return '[' + ', '.join(result) + ']'




# first = Node(1)
# second = Node('22')
# third = Node(3)
# fourth = Node('44')
# sample = LinkedList()

# sample.addtoFirst(first)
# print(sample, end='\n\n')

# sample.addtoLast(second)
# print(sample, end='\n\n')

# sample.add(1, third)
# print(sample, end='\n\n')

# print(f'{sample.delete(2)} 삭제', end='\n\n')

# print(sample, end='\n\n')

# print(sample.get(1), end='\n\n')

# print(sample)