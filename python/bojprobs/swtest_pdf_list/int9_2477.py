# K = int(input())
# l = []
# locs = []
# complocs = [4, 2, 3, 1, 3, 1]
# for i in range(6):
#     loc, leng = map(int, input().split())
#     l.append(leng)
#     locs.append(loc)
#
# for _ in range(6):
#     if locs == complocs:
#         break
#     else:
#         temp = locs.copy()
#         for j in range(6):
#             locs[j] = temp[(j+1) % 6]
# else:
#     l.reverse()
#
#
# l_idx = l.index(max(l))
# if l[(l_idx + 1) % 6] == l[l_idx]:
#     l_idx = (l_idx + 1) % 6
#
# l_1st = (l_idx + 1) % 6
# l_2nd = (l_idx + 2) % 6
# l_3rd = (l_idx + 3) % 6
#
# area = (l[l_idx] * (l[l_1st] + l[l_3rd])) - (l[l_2nd] * l[l_3rd])
# print(area * K)

def Idxplus(idx):
    return (idx + 1) % 6

K = int(input())
direc = []
leng = []
for i in range(6):
    d, l = map(int, input().split())
    direc.append(d)
    leng.append(l)

longidx = []
for i in range(6):
    if direc.count(direc[i]) == 1:
        longidx.append(i)

idx = longidx[0]
while direc.count(direc[idx]) == 1:
    idx = Idxplus(idx)

shortidx = [Idxplus(idx), Idxplus(Idxplus(idx))]

area = leng[longidx[0]] * leng[longidx[1]] - leng[shortidx[0]] * leng[shortidx[1]]
print(area*K)