def BT(arr, start, bishop, sumdiag):
    global tempresult
    if start == len(arr) or sumdiag == 0:
        tempresult = max(tempresult, bishop)
    for i in range(start, len(arr)):
        y, x = arr[i]
        if diag1[y-x] and diag2[y+x]:
            diag1[y-x] = 0
            diag2[y+x] = 0
            BT(arr, i+1, bishop+1, sumdiag-1)
            diag1[y-x] = 1
            diag2[y+x] = 1


N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
idxfield = [0 if i&1 else 1 for i in range(N**2)]
idxfield = [idxfield[i:i+N] for i in range(0, N**2, N)]
if not N&1:
    for i in range(1, N, 2):
        for j in range(N):
            if idxfield[i][j]: idxfield[i][j] = 0
            else: idxfield[i][j] = 1

diag1 = [1 for i in range(2*N-1)] # 우하
diag2 = [1 for i in range(2*N-1)] # 우상

odd = []
even = []

for i in range(N):
    for j in range(N):
        if field[i][j]:
            if idxfield[i][j]: odd.append((i,j))
            else: even.append((i,j))

tempresult = 0
BT(odd, 0, 0, sum(diag1))
result = tempresult
tempresult = 0
BT(even, 0, 0, sum(diag1))
result += tempresult

print(result)

# for _ in range(len(idxfield)):
#     print(idxfield[_])