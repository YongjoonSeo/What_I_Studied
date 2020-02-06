# N = int(input())
# lefts = [0] * N
# heights = [0] * N
# area = 0

# for i in range(N):
#     lefts[i], heights[i] = map(int, input().split())
# highest = max(heights)
# temp_h = ''.join([str(i) for i in heights])
# l_end = lefts[temp_h.find(str(highest))]
# r_end = lefts[temp_h.rfind(str(highest))]

# if l_end == r_end:
#     base = 1
# else:
#     base = r_end - l_end + 1

# base_l = lefts[0]
# base_r = lefts[-1]
# idx = 1
# prevh_l = heights[0]
# prevh_r = heights[-1]

# while heights[idx] <= highest:
#     if heights[idx] == highest or heights[idx-1] == highest:
#         idx += 1
#         break
#     elif heights[idx] > prevh_l:
#         base_l = lefts[idx] - base_l
#         area += base_l * prevh_l
#         base_l = lefts[idx]
#         prevh_l = heights[idx]
#         idx += 1
#     else:
#         idx += 1
#         continue

# idx = -2

# while heights[idx] <= highest:
#     if heights[idx] == highest or heights[idx+1] == highest:
#         break
#     elif heights[idx] > prevh_r:
#         base_r = base_r - lefts[idx]
#         area += base_r * prevh_r
#         base_r = lefts[idx]
#         prevh_r = heights[idx]
#     else:
#         continue
#     idx -= 1

# area += base * highest

# print(area)

# N = int(input())
# area = 0
# temp = []

# for i in range(N):
#     inp = tuple(map(int, input().split()))
#     temp.append(inp)
# temp.sort(key=lambda x:x[0])    
# # print(temp)
# loc = [a[0] for a in temp]
# h = [b[1] for b in temp]
# # print(loc, h)
# highest = max(h)
# loc2 = loc[::-1]
# h2 = h[::-1]

# i = 0
# temploc = loc[0]
# temph = h[0]
# while i < h.index(highest):
#     if i == 0:
#         pass
#     elif h[i] > h[i-1]:
#         area += temph * (loc[i] - temploc)
#         temploc = loc[i]
#         temph = h[i]
#     i += 1

# j = 0
# temploc2 = loc2[0]
# temph2 = h2[0]
# while j < h2.index(highest):
#     if j == 0:
#         pass
#     elif h2[j] > h2[j-1]:
#         area += temph2 * (temploc2 - loc[j])
#         temploc2 = loc2[j]
#         temph2 = h2[j]
#     j += 1

# if h.count(highest) > 1:
#     area += (loc2[h2.index(highest)] - loc[h.index(highest)] + 1) * highest
# else:
#     area += highest

# print(area)


# N = int(input())
# whole = []
# for _ in range(N):
#     temp = tuple(map(int, input().split()))
#     whole.append(temp)
# whole.sort(key=lambda x: x[0])
# base = whole[-1][0] - whole[0][0] + 1
# h = [i[1] for i in whole]
# l_lst = [i[0] for i in whole]
# r_lst = l_lst[::-1]
# maxh = max(h)

# i = 0
# temph = min(h)
# while temph < maxh:

# N = int(input())
# whole = []
# for _ in range(N):
#     temp = tuple(map(int, input().split()))
#     whole.append(temp)
# whole.sort(key=lambda x:x[0])
# h = [i[1] for i in whole]
# std = h.index(max(h))

def Loc(lst, k):
    return lst[k][0]

N = int(input())
raw = []
area = 0

for i in range(N):
    temp = tuple(map(int, input().split()))
    raw.append(temp)
raw.sort(key=lambda x: x[0])

h = [i[1] for i in raw]

maxh = max(h)
max_idx = h.index(maxh)
# max_loc = Loc(raw, max_idx)

tempidx = 0
for i in range(1, max_idx + 1):
    if h[tempidx] <= h[i]: ## 바꾼부분 ('='추가)
        area += (Loc(raw, i) - Loc(raw, tempidx)) * h[tempidx]
        tempidx = i

if h.count(maxh) >= 2:
    while tempidx != len(h) and h[tempidx] == maxh:
        tempidx += 1
    rmax_idx = tempidx -1
    area += (Loc(raw, rmax_idx) - Loc(raw, max_idx) + 1) * maxh
else:
    rmax_idx = tempidx
    area += maxh

tempidx = -1
for j in range(-2, rmax_idx - len(h) -1, -1):
    if h[j] >= h[tempidx]:
        area += (Loc(raw, tempidx) - Loc(raw, j)) * h[tempidx]
        tempidx = j

print(area)

# print(h)
# print(raw)

# 인덱스를 고려해야 하는 경우가 많아서 모든 케이스를 집어내기 힘들었다
# ==> 시점, 종점, 최대 값을 가지는 점.

# N = int(input())
# raw = []
# area = 0
# for i in range(N):
#     temp = tuple(map(int, input().split()))
#     raw.append(temp)
# raw.sort(key=lambda x: x[0])

# maxidx = raw.index(max(raw, key=lambda x: x[1]))

# lmaxidx = maxidx
# while lmaxidx >= 0:
    


# # print(maxidx)
# # print(raw)