from heapq import heappush, heappop

lst = [69, 10, 30, 2, 16, 8, 31, 22]
heap = []
result = []

for element in lst:
    heappush(heap, element)

for element in range(len(heap)):
    result.append(heappop(heap))

print(result)
