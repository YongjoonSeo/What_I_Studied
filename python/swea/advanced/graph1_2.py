# 숫자가 더 클때 작을 때로 나눠보자.
# 백트래킹 하는게 더 나을듯 -> 아님.
# bfs로 더 작을 때는 늘어나게 더 클때는 줄어들게 해보자.
# -> 잘못된 접근방식인듯.

from collections import deque

def BFS(n, obj):
    cnt = 0
    q = deque([n])
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            if v < obj:
                if v * 2 <= 1000000:
                    temp1 = v * 2
                if v + 1 <= 1000000:
                    temp2 = v + 1
            elif v > obj:
                if v-10 > 0:
                    temp1 = v - 10
                if v - 1 > 0:
                    temp2 = v - 1
            if temp1 == obj or temp2 == obj: return cnt
            if temp1: q.append(temp1)
            if temp2: q.append(temp2)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    print('#{0} {1}'.format(t, BFS(N, M)))