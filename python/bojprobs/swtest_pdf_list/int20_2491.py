# N = int(input())
# lst = list(map(int, input().split()))
# result = 1
# result2 = 1

# s = lst[0]
# temp = 1
# for i in range(1, len(lst)+1):
#     if i == len(lst):
#         result = temp
#         break
#     elif lst[i] >= s:
#         temp += 1
#     else:
#         if result <= temp:
#             result = temp
#             temp = 1
#     s = lst[i]

# # result2 = 1
# # rlst = lst[::-1]
# # s2 = rlst[0]  
# # temp = 1  
# # for i in range(1, len(rlst)+1):
# #     if i == len(rlst):
# #         result2 = temp   
# #         break
# #     elif rlst[i] >= s2:
# #         temp += 1
# #     else:
# #         if result2 <= temp:
# #             result2 = temp
# #             temp = 1
# #     s2 = rlst[i]   

# s = lst[0]
# temp = 1
# for i in range(1, len(lst)+1):
#     if i == len(lst):
#         result2 = temp
#         break
#     elif lst[i] <= s:
#         temp += 1
#     else:
#         if result2 <= temp:
#             result2 = temp
#             temp = 1
#     s = lst[i]


# print(result) if result >= result2 else print(result2)
# # print(result2)
# # 미리 풀이법이 맞는지 검증부터 하고 코드를 짜자....


# N = int(input())
# lst = list(map(int, input().split()))
# result = 1

# for i in range(2):
#     comp = [0, 0]
#     temp = 1
#     s = lst[0]
#     if i == 0:
#         for j in range(len(lst)):
#             if lst[j] >= s:
#                 temp += 1
#                 s = lst[j]
#             else:
#                 if result <= temp:
#                     result = temp
#                 s = lst[j]
#                 temp = 1
#         comp[i] = result
#     if i == 1:
#         for j in range(len(lst)):
#             if lst[j] <= s:
#                 temp += 1
#                 s = lst[j]
#             else:
#                 if result <= temp:
#                     result = temp
#                 s = lst[j]
#                 temp = 1
#         comp[i] = result
#     result = max(comp)
            
# print(result)

N = int(input())
lst = list(map(int, input().split()))
result = [0,0]

length = 1
for i in range(1, len(lst)+1):
    if i == len(lst):
        if result[0] < length:
            result[0] = length
    elif lst[i] >= lst[i-1]:
        length += 1
    else:
        if result[0] < length:
            result[0] = length
        length = 1

length = 1
for i in range(1, len(lst)+1):
    if i == len(lst):
        if result[1] < length:
            result[1] = length
    elif lst[i] <= lst[i-1]:
        length += 1
    else:
        if result[1] < length:
            result[1] = length
        length = 1

print(max(result))

# 정답. 문제에서 구하는 조건을 (이번에는 세어가는 방향) 정확히 적용한다.