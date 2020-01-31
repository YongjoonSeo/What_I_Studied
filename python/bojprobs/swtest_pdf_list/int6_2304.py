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

N = int(input())
lfts = [0] * N
heights = [0] * N
for i in range(N):
    lfts[i], heights[i] = map(int, input().split())
highest_idx = heights.index(max(heights))





