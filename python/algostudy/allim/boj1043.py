# 진실을 아는 사람에게도 진실로 말해야하고, 어떤 파티에서 진실을 알게 된 사람에겐 과장된 이야기를 못 한다.
# 즉, 진실을 모르는 사람만 있는 경우에만 과장된 이야기를 할 수 있다.
# 파티에 진실을 아는 사람이 있다 -> 말하지 못한다
# 파티에 오는 사람 번호를 순회하면서, 진실을 아는 사람을 탐색하고
# 한 사람이라도 알면 그 파티의 사람들은 모두 진실을 안다고 체크.
# 모두 돌았는데 진실 아는 사람이 없다면 거짓부렁 파티 개수 +1
#### 순서 상관없이 모두 포함해야한다. -> 진실을 아는 사람이랑 연결되어 있으면 모두 안 된다.
from collections import deque

def check(lst):
    global cnt
    exists_truth = False
    for i in lst:
        if truth[i]:
            exists_truth = True
            break
    else:
        cnt += 1
    if exists_truth:
        for i in lst:
            truth[i] = 1

def combi(arr, start, r):
    for i in range(start, len(arr)-r+1):
        if r == 1:
            yield [arr[i]]
        else:
            for j in combi(arr, i+1, r-1):
                yield [arr[i]] + j

N, M = map(int, input().split())
truth = [0 for i in range(N+1)]
field = [[0 for i in range(N+1)] for j in range(N+1)]
parties = []
know_truth = list(map(int, input().split()))[1:]
cnt = 0
# for person in know_truth:
#     truth[person] = 1

for _ in range(M):
    inp = list(map(int, input().split()))[1:]
    parties.append(inp)
    if len(inp) >= 2:
        for s, e in combi(inp, 0, 2):
            field[s][e] = 1
            field[e][s] = 1

for person in know_truth:
    q = deque([person])
    truth[person] = 1
    while q:
        v = q.popleft()
        for i in range(1, N+1):
            if not truth[i] and field[v][i]:
                q.append(i)
                truth[i] = 1

for party in parties:
    check(party)

# for s,e in combi([1,2,3,4], 0, 2):
#     print(s,e)

# for _ in range(len(field)):
#     print(field[_])

print(cnt)
# print(truth)
# print(len(truth))