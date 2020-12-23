# M, N = map(int, input().split())
# for i in range(M, N+1):
#     if i == 1:
#         continue
#     for j in range(2, i):
#         if not i % j:
#             break
#     else:
#         print(i)

# # 시간 초과

# M, N = map(int, input().split())
# primes = []
# for i in range(M, N+1):
#     if i == 1:
#         continue
#     for a in range(2, i):
#         if not i % a:
#             break
#     else:
#         primes.append(i)

# for j in primes:
#     if j >= M and j <= N:
#         print(j)

# # 시간 초과

# M, N = map(int, input().split())
# primes = []
# for i in range(M, N+1):
#     if i == 1:
#         continue
#     for a in range(2, i):
#         if not i % a:
#             break
#     else:
#         if i >= M and i <= N:
#             primes.append(str(i))

# print('\n'.join(primes))

# # 시간 초과

# M, N = map(int, input().split())
# raw = [i for i in range(2,1000001)]
# primes = []
# for j in raw:
#     if j == 1:
#         continue
#     for k in range(2,j):
#         if not j % k:
#             break
#     else:
#         primes.append(j)

# for l in range(M, N+1):
#     if l in primes:
#         print(l)

# M, N = map(int, input().split())
# for i in range(M, N+1):
#     if i == 1:
#         continue
#     elif i == 2:
#         print(i)
#     elif not i % 2:
#         continue
#     for j in range(3, i, 2):
#         if not i % j:
#             break
#     else:
#         print(i)

# # 시간 초과

# M, N = map(int, input().split())
# for i in range(M, N+1):
#     if i == 1:
#         continue
#     elif i == 2:
#         print(i)
#     elif not i % 2:
#         continue
#     for j in range(3, int(i**0.5)+1, 2):
#         if not i % j:
#             break
#     else:
#         print(i)

# 틀림

def is_prime(n):
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True

M, N = map(int, input().split())
for i in range(M, N+1):
    if i == 1:
        continue
    elif is_prime(i):
        print(i)

# 따로 함수를 간결하게 만들어서 사용. (판별함수 만들어서 씀) --> 정답!