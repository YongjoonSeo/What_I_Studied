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

ㄱ자모양 90 180 270도 회전
한 모퉁이에서 출발 (꼭짓점에서 출발)!!!!
반시계방향

입력
변의 방향과 길이 동 1 서 2 남 3 북 4

전체 참외개수 = 면적 * 1평방미터 참외 개수
