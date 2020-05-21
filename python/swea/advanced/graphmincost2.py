# 시점 종점이 정해져있으며 최소비용으로 거리 - 다익스트라
# 시점 (0,0) 종점 (N-1, N-1)
# 대각선을 토대로 걸리는 거리만큼 더한 후, 별도의 높이를 저장해둔 부분에서 가중치를 더할땐 빼보자
# 음..보류

def Dijkstra(G, v):


T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [list(map(int, input().split())) for j in range(N)]
    dist = [[i+j for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            field[i][j] += dist[i][j]

    for _ in range(len(field)):
        print(field[_])