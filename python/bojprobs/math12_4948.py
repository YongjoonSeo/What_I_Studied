# def is_prime(n):
#     if n == 1:
#         return False
#     i = 2
#     while i * i <= n:
#         if not n % i:
#             return False
#         i += 1
#     return True


# while True:
#     n = int(input())
#     if n == 0:
#         break
#     else:
#         cnt = 0
#         for i in range(n+1, 2*n+1):
#             if is_prime(i):
#                 cnt += 1
#         print(cnt)

# 왜 안되지?? -->>> while은 조건문을 빠져나갈 경우를 반드시 만들어야 한다. 함수에서든 어디서든.

# -> 시간초과.. readline으로 해도 시간 초과.

def is_prime(n):
    i = 2
    while i * i <= n:
        if not n % i:
            return False
        i += 1
    return True

primes = [is_prime(i) for i in range(1,246913)]

while True:
    n = int(input())
    cnt = 0
    if n == 0:
        break
    else:
        for j in range(n, 2*n):
            if primes[j]:
                cnt += 1
        print(cnt)

# 범위가 주어져있으니 소수를 미리 구함 -> 시간 안에 풀어짐. 정답.