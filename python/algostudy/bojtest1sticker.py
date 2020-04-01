def check(y, x, r, c, arr):
    global N, M, cnt
    changecoor = []
    for i in range(r):
        for j in range(c):
            if i+y < N and j+x < M:
                if arr[i][j]:
                    if field[i+y][j+x]: return
                    else:
                        changecoor.append((i+y, j+x))
            else:
                return
    for coor in changecoor:
        field[coor[0]][coor[1]] = 1
        cnt += 1
    return True

N, M, K = map(int, input().split())
field = [[0 for i in range(M)] for j in range(N)]
cnt = 0

for _ in range(K):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for j in range(R)] 
    
    isFound = False
    for i in range(N):
        for j in range(M):
            if check(i, j, R, C, sticker):
                isFound = True
                break
        if isFound: break
    else:
        for k in range(3):
            isFoundprime = False
            sticker = list(zip(*sticker[::-1]))
            R = len(sticker)
            C = len(sticker[0])
            for i in range(N):
                for j in range(M):
                    if check(i, j, R, C, sticker):
                        isFoundprime = True
                        break
                if isFoundprime: break
            if isFoundprime: break

print(cnt)

    # for _ in range(len(sticker)):
    #     print(sticker[_])





    # test = list(zip(*sticker[::-1]))
    # for _ in range(len(test)):
    #     print(test[_])

# for _ in range(len(field)):
#     print(field[_])

# for _ in range(len(sticker)):
#     print(sticker[_])