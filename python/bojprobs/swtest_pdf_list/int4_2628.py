# W, H = map(int, input().split())
# times = int(input())
# hor = [0] * W
# ver = [0] * H
# # horcount = [0]
# # vercount = [0]

# for i in range(times):
#     cut = list(map(int, input().split()))
#     if cut[0]: # 세로로 자른다
#         hor.insert(cut[1], 1)
#         # horcount.append(0)
#     else:
#         ver.insert(cut[1], 1)
#         # vercount.append(0)

# horizon = ''.join([str(i) for i in hor])
# vertical = ''.join([str(j) for j in ver])
# horcount = horizon.split('1')
# vercount = vertical.split('1')

# idx = 0
# while idx < len(hor):
#     for j in range(len(horcount)):
#         if hor[idx] == 0:

# for j in range(len(horcount)): 
#     for k in hor[horcount[j-1]:]:
#         if k == 0:
#             horcount[j] += 1
#         else:
#             break

# for j in range(len(vercount)): 
#     for k in ver[vercount[j-1]:]:
#         if k == 0:
#             vercount[j] += 1
#         else:
#             break
# print(hor, ver)
# print(horcount, vercount)

# print(result)

# 처음에 그냥 리스트'로만' 하려고 해서 안된듯.
# 적절한 함수 쓸 수 있게 문자열과 리스트 모두 같이 써보자.

# W, H = map(int, input().split())
# times = int(input())
# hor = [0] * W
# ver = [0] * H

# horreps = 0
# verreps = 0
# horprev = 0
# verprev = 0
# for i in range(times):
#     cut = list(map(int, input().split()))
#     if cut[0]:
#         if cut[1] >= horprev:
#             hor.insert(cut[1]+horreps, 1)
#         else:
#             hor.insert(cut[1], 1)
#         horprev = cut[1] + horreps
#         horreps += 1
#     else:
#         if cut[1] >= verprev:
#             ver.insert(cut[1]+verreps, 1)
#         else:
#             ver.insert(cut[1], 1)
#         verprev = cut[1] + verreps
#         verreps += 1

# horizon = ''.join([str(i) for i in hor])
# vertical = ''.join([str(j) for j in ver])
# horcount = horizon.split('1')
# vercount = vertical.split('1')

# # print(horizon, vertical)
# # print(horcount, vercount)

# result = [len(i)*len(j) for i in horcount for j in vercount]
# # print(result)
# print(max(result))

# # 틀림 -> 케이스에 따라 리스트 크기를 제대로 조절하기 힘들었음.


W, H = map(int, input().split())
times = int(input())
hor = '0' * W
ver = '0' * H
opr = []
for _ in range(times):
    opr.append(tuple(map(int, input().split())))
opr.sort(key=lambda x: x[1], reverse=True)
for i in opr:
    if i[0]: 
        hor = hor[:i[1]] + ' ' + hor[i[1]:]
    else:
        ver = ver[:i[1]] + ' ' + ver[i[1]:]

ho_re = hor.split()
ve_re = ver.split()
result = [len(j) * len(k) for j in ho_re for k in ve_re]
print(max(result))

#--> 리스트 크기 제대로 조절하고 나서는 성공. 