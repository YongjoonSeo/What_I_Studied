# def Inbox(lst, y, x, c, r):
#     if x >= 1 and x < c+1 and y >= 1 and y < r+1:
#         if lst[y][x] == 0: return True
#     return False

# C, R = map(int, input().split())
# field = [[1 for i in range(C+2)] for j in range(R+2)]
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
# x, y = 1, R
# idx = 0

# for j in range(1, R+1):
#     for i in range(1, C+1):
#         field[j][i] = 0

# for i in range(1,C*R + 1):
#     field[y][x] = i
#     if not Inbox(field, y+dy[idx], x+dx[idx], C, R):
#         idx = (idx + 1) % 4
#     x += dx[idx]
#     y += dy[idx]

# result = [[i for i in field[j][1:C+1]] for j in range(1, R+1)]
# person = int(input())

# if person > C*R:
#     print(0)
# else:
#     for j in range(R):
#         for i in range(C):
#             if result[j][i] == person:
#                 print('{0} {1}'.format(i+1, R - j))
#                 break
       

# for _ in range(len(field)):
#     print(field[_])

# for _ in range(len(result)):
#     print(result[_])


# 2
def Within(lst, y, x, c, r):
    if x >= 0 and x < c and y >= 0 and y < r:
        if lst[y][x] == 0: return True
    return False

C, R = map(int, input().split())
person = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
idx = 0
x, y = 0, R-1
field = [[0 for i in range(C)] for j in range(R)]


for i in range(C*R):
    field[y][x] = i+1
    if person > C*R:
        print(0)
        break    
    elif i+1 == person:
        print('{0} {1}'.format(x+1, R-y))
        break
    if not Within(field, y+dy[idx], x+dx[idx], C, R):
        idx = (idx + 1) % 4
    x += dx[idx]
    y += dy[idx]

# for l in range(len(field)):
#     print(field[l])