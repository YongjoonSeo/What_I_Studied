def DFS(infomap, vertex): # 연결 정보, 검색 시작점
    visited = [0] * len(field)
    stack = []
    v = vertex # 1. DFS 호출되는 시점에 방문 시작 정점이 주어진다.
    visited[v] = 1 # 2. v를 visited에 방문했다고 표시한다.
    print(v, end=' ')
    w = 1    
    
    while w:
        for i in range(len(infomap)):
            if infomap[v][i] == 1 and visited[i] == 0:
            # 3. v와 인접한 정점 중 방문하지 않은 정점을 visited 리스트를 통해 찾는다.
                w = i # --> 이 중 하나의 정점을 선택해서 변수 w에 할당.
                break
        else:
            if stack:
                v = stack.pop() # b-4. w가 빈 값이면 stack에서 pop하여 v에 저장한다.
                continue
            else: # b-6. Stack에서 pop하려 할 때 v가 빈 값이면 함수를 종료한다.
                return

        stack.append(v) # a-4. 방문한 정점의 정보(v)를 stack에 저장. (=이후 되돌아 올 정점 정보)
        visited[w] = 1 # a-5. w를 방문, visited에 방문했다고 표시한다.
        print(w, end=' ')
        v = w # a-6. w를 v변수에 할당하고 3~5 과정을 반복한다.

V, E = map(int, input().split())
edges = list(map(int, input().split()))
field = [[0 for i in range(V+1)] for j in range(V+1)]

for i in range(E):
    s, e = edges[2*i], edges[2*i+1]
    field[s][e] += 1
    field[e][s] += 1

DFS(field, 1)

# for _ in range(V):
#     print(field[_])

# 인접한 정점 정보 -> field로 주기
# 7 8
# 1 2 1 3 2 5 2 4 3 5 4 6 5 6 6 7