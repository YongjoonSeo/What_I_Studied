# def howmany(k, n):
#     if k == 1:
#         return n * (n+1) // 2
#     return n * (n+1) // 2 + howmany(k-1, n)

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     idx = 0
#     lst = list(range(1,n))

#     while k > 0:
#         # if idx == 0:
            
#         lst = [sum(lst[:x+1]) for x in range(len(lst))]
#         print(lst)
#         result = lst[-1]
#         # idx += 1
#         k -= 1
    
#     print(result)

# 층에 따라 n을 별도로 -> 실패

# def element(k, n):
#     if n == 1:
#         return 1
#     if k == 0:
#         return n
#     # return sum([element(k-1, i) for i in range(1, n+1)])
#     return element(k-1, n) + element(k, n-1)

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     print(element(k,n))

# 좀 더 작은 단위(요소의 값)를 따로 구해주는 함수를 만들어서
# 문제를 약간 더 간소화함. --> 하지만 시간초과. (재귀때문인가 싶음)

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     n = int(input())
#     lst = list(range(1,n+1))
#     templst = [0] * 

#     for i in range(len(lst)):
#         lst[i] = i * (i + 1) // 2


#     idx = 0
#     result = sum(range(1,n+1))

#     while k > 0:
#         result = sum(lst)
#         for i in lst:

        
#         (result = n * (n+1) // 2)
#         k -= 1


T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    whole = [[0 for i in range(1, n+1)] for j in range(k+1)]
    for i in range(k+1):
        for j in range(n):
            if i == 0:
                whole[i][j] = j + 1
            elif j == 0:
                whole[i][j] = 1
            else:
                whole[i][j] = whole[i-1][j] + whole[i][j-1]
    
    print(whole[-1][-1])


