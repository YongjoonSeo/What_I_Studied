# import sys
# sys.stdin = open('input.txt', 'r')

def BT(k, tot):
    global result, N
    if tot <= result: return
    if k == N:
        if result < tot:
            result = tot
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            BT(k+1, tot * field[k][i])
            visited[i] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    field = [[i/100 for i in list(map(int, input().split()))] for j in range(N)]
    visited = [0 for i in range(N)]
    result = 0
    BT(0, 1)

    print('#{0} {1:0.6f}'.format(t, result*100))

# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     field = [[i/100 for i in list(map(int, input().split()))] for j in range(N)]
#     visitedy = [0 for i in range(N)]
#     visitedx = [0 for i in range(N)]
#     count = N
#     result = 1
    
#     maxval = maxyidx = 0
#     while count:
#         candi = []
#         for i in range(N):
#             if not visitedy[i]:
#                 maxval = maxxidx = 0
#                 for j in range(N):
#                     if not visitedx[j]:
#                         if maxval < field[i][j]:
#                             maxval = field[i][j]
#                             maxxidx = j
#                 candi.append((maxval, i, maxxidx))
#         idx = maxwhole = 0
#         for i in range(len(candi)):
#             if candi[i][0] > maxwhole:
#                 maxwhole = candi[i][0]
#                 idx = i
#         resval, resy, resx = candi[idx]
#         visitedy[resy] = 1
#         visitedx[resx] = 1
#         result *= resval
#         count -= 1
    
#     print('#{0} {1:0.6f}'.format(t, result*100))