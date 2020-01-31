# N, K = map(int, input().split())
# result = []
# tempa = list(map(int, input().split()))
# for i in range(N-K):
#     result.append(sum(tempa[i:i+K]))
# print(max(result))

# # 시간 초과 ;;

# N, K = map(int, input().split())
# result = -100 * K
# tempa = list(map(int, input().split()))
# for i in range(N-K):
#     maxval = sum(tempa[i:i+K])
#     if maxval >= result:
#         result = maxval
# print(result)

# # 시간 초과 ;;;;

N, K = map(int, input().split())
tempa = list(map(int, input().split()))
result = sum(tempa[:K])
val = result
for i in range(K, N):
    if tempa[i] > tempa[i-K]:
        val += tempa[i] - tempa[i-K]
        if val > result:
            result = val
    else:
        val += tempa[i] - tempa[i-K]
print(result)

# sum(tempa[i:i+K])를 없애보았다. (k번 만큼 없애보려고) --> 성공!
# 계산을 최소화하면 시간은 줄어든다.