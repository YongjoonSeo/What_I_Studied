# N --> M
# 최소 몇 번의 연산을 해야 완성되나
# +1, -1, *2, -10 -> BFS로 최소거리를 찾자.
# 백만이 되어버리니 쓸데 없는 것도 너무 많이 찾아서 메모리 터지는듯

from collections import deque

def BFS(n, obj):
    cnt = 0
    q = deque([n])
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            for i in range(4):
                if i == 0:
                    temp = v+1
                elif i == 1:
                    temp = v-1
                elif i == 2:
                    temp = v*2
                else:
                    temp = v-10
                if temp == obj: return cnt
                q.append(temp)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    print('#{0} {1}'.format(t, BFS(N, M)))