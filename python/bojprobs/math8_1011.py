# T = int(input())
# for _ in range(T):
#     x, y = map(int, input().split())
#     length = y - x - 2
#     count = traveled = 0
#     privious = 1
    
#     while traveled - length:
#         templst = [i for i in range(privious-1, privious+2)]
#         for j in templst:
#             if j + traveled == length:
#                 count += 1
#                 traveled += j
#                 break
#         else:
#             traveled += templst[-1]
#             count += 1
    
#     count += 2
#     print(count)

# # 시간 초과 => 케이스 고려 다 못한듯. 
# # (ex. 마지막에 5,6,7만큼 갈 수 있는데 거리가 1 남는 경우)

# 거리 이동   3이하 출력      개수
# 1   1                       1
# 2   11                      2
# 3   111                     3
# 4   121        2^2          3
# 5   1211                    4
# 6   1221         2^2+2      4
# 7   12211                   5
# 8   12221                   5
# 9   12321       3^2         5
# 10  122221                  6
# 11  123221                  6
# 12  123321      3^2+3       6
# 13  1232221                 7    
# 14  1233221
# 15  1233321
# 16  1234321     4^2         7

T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    diff = y - x
    idx = int(diff ** 0.5)
    if diff <= 3:
        print(diff)
    elif diff == idx ** 2:
        print(2*idx - 1)
    elif diff <= idx ** 2 + idx:
        print(2*idx)
    else:
        print(2*idx+1)

# 패턴부터 먼저 찾아야 한다.