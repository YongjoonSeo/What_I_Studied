A = [['{0:2d}'.format(i) for i in range(j, j+5)] for j in range(1, 26, 5)]

for i in range(5):
    print(*A[i])

# # 행 우선 탐색
# for i in range(5):
#     for j in range(5):
#         print(A[i][j], end=' ')
# print()

# # 열 우선 탐색
# for i in range(5):
#     for j in range(5):
#         print(A[j][i], end=' ')
# print()

# # 지그재그 탐색 - 행
# for i in range(5):
#     for j in range(5):
#         print(A[i][j + (5 - 1 - 2 * j) * (i % 2)], end=' ')
#         # 5 = 행의 길이
# print()

# # 지그재그 탐색 - 열
# for i in range(5):
#     for j in range(5):
#         print(A[j + (5 - 1 - 2 * j) * (i % 2)][i], end=' ')
# print()

# # 델타를 이용한 탐색 - 달팽이
# def Inbox(lst, y, x, xmax, ymax): 
#     # 0 <= x < xmax, 0 <= y < ymax 일때 True 반환. IndexError를 방지할 수 있다.
#     if x >= 0 and x < xmax and y >= 0 and y < ymax:
#         if lst[y][x] == 0:
#             return True
#     return False

# result = [[0 for i in range(5)] for j in range(5)]

# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# idx = 0
# x, y = 0, 0

# for i in range(1, 26):
#     result[y][x] = '{0:2d}'.format(i)
#     if not Inbox(result, y+dy[idx], x+dx[idx], 5, 5):
#         idx = (idx + 1) % 4
#     x, y = x + dx[idx], y + dy[idx]

# for _ in range(len(result)):
#     print(*result[_])

# # 전치행렬 (1) - 새로운 2차원 List에 할당
# transA = [[0 for i in range(5)] for j in range(5)]

# for i in range(5):
#     for j in range(5):
#         transA[j][i] = A[i][j]

# for _ in range(5):
#     print(*transA[_])

# # 전치행렬 (2) - 기존 List에서 자리 재배치
# for i in range(5):
#     for j in range(i):
#         A[i][j], A[j][i] = A[j][i], A[i][j]

# for i in range(5):
#     print(*A[i])

# 전치행렬 (3) - zip 함수 사용
transA = list(zip(*A))
# A의 각 행이 언패킹되어 zip 함수의 인자로 들어간다.
# 다시 zip함수에 의해 패킹된 요소는 튜플 형식으로 transA에 들어간다.
print(transA)
print(type(transA[0]))
# for i in range(5):
#     print(*transA[i])


# # 델타를 이용한 탐색 (2) - 계단
# def Inbox2(y, x, xmax, ymax): 
#     # 0 <= x < xmax, 0 <= y < ymax 일때 True 반환. IndexError를 방지할 수 있다.
#     if x >= 0 and x < xmax and y >= 0 and y < ymax:
#         return True
#     return False

# dx = [-1, 0]
# dy = [0, 1]
# idx = 0
# x, y = len(A)-1, 0

# for i in range(10):
#     print(A[y][x], end=' ')
#     if not Inbox2(y+dy[idx], x+dx[idx], 5, 5):
#         idx = (idx + 1) % 2
#     if y + dy[idx] > y:
#         print()
#     x, y = x + dx[idx], y + dy[idx]