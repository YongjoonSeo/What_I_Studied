# 연산 중에 백만 넘어가는 건 제끼자
# 아ㅏㅏㅏㅏㅏㅏ니ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ
# 기본적인 BFS도 제대로 못하고 있었다.... visited 사용해서 한번 간 곳은 다시 안가야하는데 그러지 못했음.

from collections import deque

def BFS(n, obj):
    cnt = 0
    q = deque([n])
    visited[n] = 1
    while q:
        cnt += 1
        for _ in range(len(q)):
            v = q.popleft()
            for i in range(4):
                if i == 0:
                    if v+1 <= 1000000:
                        temp = v+1
                elif i == 1:
                    if v-1 > 0:
                        temp = v-1
                elif i == 2:
                    if v*2 <= 1000000:
                        temp = v*2
                else:
                    if v-10 > 0:
                        temp = v-10
                if temp == obj: return cnt
                if not visited[temp] and temp:
                    visited[temp] = 1
                    q.append(temp)


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    visited = [0 for i in range(1000001)]
    print('#{0} {1}'.format(t, BFS(N, M)))