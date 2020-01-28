# T = int(input())
# for _ in range(T):
#     H, W, N = map(int, input().split())
#     rest = N // H
#     Y_idx = N % H
#     if Y_idx == 0:
#         Y_idx = H
#         X_idx = rest
#     else:
#         X_idx = rest + 1

#     if X_idx < 10:
#         X_idx = '0' + str(X_idx)
#     print('{0}{1}'.format(Y_idx, X_idx))

# # 네이밍 조심
# # 케이스 체크 제대로

# 다른 코드
T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    N -= 1
    print('{0}{1:0>2}'.format(N % H + 1, N // H + 1))

# 시작점을 컴퓨터에서 보통 하듯이 0부터 하도록 맞춰서 마지막에 보정.