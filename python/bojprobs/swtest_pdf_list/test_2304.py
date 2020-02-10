N = 10

def Loc(lst, k):
    return lst[k][0]

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


# 정답
# -------------
# 오답

raw2 = []
area2 = 0

for i in range(N):
    temp = tuple(map(int, input().split()))
    raw2.append(temp)
raw2.sort(key=lambda x: x[0])

h = [i[1] for i in raw2]

maxh2 = max(h)
max_idx = h.index(maxh2)
# max_loc = Loc(raw2, max_idx)

tempidx2 = 0
for i in range(1, max_idx + 1):
    if h[tempidx2] < h[i]: ## 바꾼부분 ('='추가)
        area2 += (Loc(raw2, i) - Loc(raw2, tempidx2)) * h[tempidx2]
        tempidx2 = i

if h.count(maxh2) >= 2:
    while tempidx2 != len(h) and h[tempidx2] == maxh2:
        tempidx2 += 1
    rmax_idx = tempidx2 -1
    area2 += (Loc(raw2, rmax_idx) - Loc(raw2, max_idx) + 1) * maxh2
else:
    rmax_idx = tempidx2
    area2 += maxh2

tempidx2 = -1
for j in range(-2, rmax_idx - len(h) -1, -1):
    if h[j] > h[tempidx2]:
        area2 += (Loc(raw2, tempidx2) - Loc(raw2, j)) * h[tempidx2]
        tempidx2 = j




if area != area2:
    print('정답:{0}'.format(area))
    print('오답: {0}'.format(area2))
    print(raw)
    print(raw2)
else:
    print('일치')

