import sys
sys.stdin = open('input.txt', 'r')

def DFS(s, count):
    for i in range(1, 101):
        if field[s][i] and not visited[i]:
            visited[i] = 1
            DFS(i, count+1)
            visited[i] = 0
    else:
        if count < resultdata[s]:
            resultdata[s] = count

for t in range(1, 11):
    N, start = map(int, input().split())
    field = [[0 for i in range(101)] for j in range(101)]
    visited = [0 for i in range(101)]
    resultdata = [101 for i in range(101)]
    data = list(map(int, input().split()))

    for i in range(0, len(data), 2):
        field[data[i]][data[i+1]] = 1
    
    visited[start] = 1
    DFS(start, 1)
    
    maxcnt = result = 0
    for i in range(1, 101):
        if resultdata[i] != 101 and maxcnt < resultdata[i]:
            maxcnt = resultdata[i]
            result = i
        elif maxcnt == resultdata[i]:
            result = i

    print('#{0} {1}'.format(t, result))