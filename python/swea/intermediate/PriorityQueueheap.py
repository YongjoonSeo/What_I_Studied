from heapq import heappush, heappop
# 리스트를 힙처럼 사용할 수 있게 하는 함수들이다.

h = []
recipe = [
    [4, '베이컨을 볶는다.'],
    [2, '파기름을 낸다.'],
    [3, '파기름에 계란을 볶는다.'],
    [6, '먹는다.'],
    [1, '대파와 베이컨을 잘게 썬다.'],
    [5, '찬밥을 넣고 볶는다.'],
]

for i in recipe:
    print(i)
print('-------------------------------')
for j in recipe:
    heappush(h, j)

for k in recipe:
    print(heappop(h))