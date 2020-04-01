from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

for t in range(1, 11):
    N, start = map(int, input().split())
    field = [[0 for i in range(101)] for j in range(101)]
    visited = [0 for i in range(101)]
    data = list(map(int, input().split()))

    for i in range(0, len(data), 2):
        s, e = data[i], data[i+1]
        field[s][e] = 1
    
    q = deque([start])
    visited[start] = 1

    while q:
        maxnum = 0
        for _ in range(len(q)):
            v = q.popleft()
            for i in range(1, 101):
                if not visited[i] and field[v][i]: 
                    q.append(i)
                    visited[i] = 1
            maxnum = max(maxnum, v)
    
    print('#{0} {1}'.format(t, maxnum))
            


    # for _ in range(len(field)):
    #     print(field[_])