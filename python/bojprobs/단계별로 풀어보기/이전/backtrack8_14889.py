def facto(n):
    if n == 1: return 1
    else: return n * facto(n-1)

def Pick(arr, idx, r):
    global N, halfnum, picknum
    if halfnum == picknum: return
    if r == N//2:
        candi.append(arr[:])
        picknum += 1
        return
    templst = arr
    for i in range(idx, N-(N//2) + 1 + r):
        templst.append(i)
        Pick(templst, i+1, r+1)
        if halfnum == picknum: return
        templst.remove(i)

def Search(arr):
    global result
    startteam = linkteam = 0
    for i in range(len(arr)-1):
        visited[arr[i]] = 1
        for j in range(i+1, len(arr)):
            visited[arr[j]] = 1
            startteam += field[arr[i]][arr[j]] + field[arr[j]][arr[i]]
    linklst = []
    for i in range(len(visited)):
        if not visited[i]: linklst.append(i)
    for i in range(len(linklst)-1):
        for j in range(i+1, len(linklst)):
            linkteam += field[linklst[i]][linklst[j]] + field[linklst[j]][linklst[i]]
    if abs(startteam-linkteam) < result:
        result = abs(startteam-linkteam)    

N = int(input())
halfnum = facto(N) // (facto(N//2) * facto(N//2)) // 2
picknum = 0
field = [list(map(int, input().split())) for i in range(N)]
candi = []
result = 50000
Pick([], 0, 0)

for case in candi:
    visited = [0 for i in range(N)]
    Search(case)
print(result)


# Pick([], 0)
# print(candi)
# for _ in range(len(field)):
#     print(field[_])