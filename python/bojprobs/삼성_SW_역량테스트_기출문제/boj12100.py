# 상 하 좌 우 4가지 경우를 5번(중복포함) 고르는 것
# def 상 하 좌 우에 대해서 글자를 합치는 것 & 글자를 옮기는 것 -> 동시에 해도 될듯 - 그때마다 맥스값 경신하자
# 0-우 1-하 2-좌 3-상
# 한번 합쳐진 건 다시 합치지 않는다. <<<<<<<
# 순서 고려해야한다!!!!!!!! <<<<<
# 순열로 풀면 안되는건가? 어디가 잘못된거지


def permu_with_replacement(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for j in permu_with_replacement(arr, r-1):
                yield [arr[i]] + j

def move(direc, arr):
    global N
    maxval = 0
    if direc == 0:
        for i in range(N):
            k = 0
            for j in range(N-1, -1, -1):
                if arr[i][j]:
                    while j+1 < N and not arr[i][j+1]:
                        arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                        j += 1
                    if j+1 == N-k: k -= 1
                    elif j+1 < N-k:
                        if arr[i][j+1] == arr[i][j]:
                            arr[i][j+1] *= 2
                            arr[i][j] = 0
                            k += 1
                    k += 1
                    if not arr[i][j]: maxval = max(maxval, arr[i][j+1])
                    else: maxval = max(maxval, arr[i][j])
    elif direc == 1:
        for i in range(N):
            k = 0
            for j in range(N-1, -1, -1):
                if arr[j][i]:
                    while j+1 < N and not arr[j+1][i]:
                        arr[j][i], arr[j+1][i] = arr[j+1][i], arr[j][i]
                        j += 1
                    if j + 1 == N - k: k -= 1
                    elif j+1 < N-k:
                        if arr[j+1][i] == arr[j][i]:
                            arr[j + 1][i] *= 2
                            arr[j][i] = 0
                            k += 1
                    k += 1
                    if not arr[j][i]: maxval = max(maxval, arr[j+1][i])
                    else: maxval = max(maxval, arr[j][i])
    elif direc == 2:
        for i in range(N):
            k = 0
            for j in range(N):
                if arr[i][j]:
                    while j-1 >= 0 and not arr[i][j-1]:
                        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
                        j -= 1
                    if j + 1 == N - k: k -= 1
                    elif j-1 >= 0+k:
                        if arr[i][j-1] == arr[i][j]:
                            arr[i][j - 1] *= 2
                            arr[i][j] = 0
                            k += 1
                    k += 1
                    if not arr[i][j]: maxval = max(maxval, arr[i][j-1])
                    else: maxval = max(maxval, arr[i][j])
    else:
        for i in range(N):
            k = 0
            for j in range(N):
                if arr[j][i]:
                    while j-1 >= 0 and not arr[j-1][i]:
                        arr[j][i], arr[j-1][i] = arr[j-1][i], arr[j][i]
                        j -= 1
                    if j + 1 == N - k: k -= 1
                    elif j-1 >= 0+k:
                        if arr[j-1][i] == arr[j][i]:
                            arr[j - 1][i] *= 2
                            arr[j][i] = 0
                            k += 1
                    k += 1
                    if not arr[j][i]: maxval = max(maxval, arr[j-1][i])
                    else: maxval = max(maxval, arr[j][i])
    return maxval

def check(arr):
    global result, N
    maxval = 0
    for lst in permu_with_replacement(range(4), 5):
        newarr = [[arr[i][j] for j in range(N)] for i in range(N)]
        for direc in lst:
            maxval = max(maxval, move(direc, newarr))

    return maxval


N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
print(check(field))

# move(1, field)

# cnt = 0
# for i in permu_with_replacement([1,2,3], 3):
#     print(i)
#     cnt += 1
# print(cnt)

# for _ in range(N):
#     print(field[_])