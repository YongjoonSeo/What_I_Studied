def BT(day, price, cantgo):
    global result, N, coupon
    if price > result: return
    if cantgo <= N and cantbool[cantgo]:
        BT(day+1, price, cantgo+1)
    if day >= N: 
        result = min(result, price)
        return
    for i in range(3):
        if i == 0:
            coupon += 2
            BT(day+5, price+37000, cantgo+5)
            coupon -= 2
        elif i == 1:
            coupon += 1
            BT(day+3, price+25000, cantgo+3)
            coupon -= 1
        else:
            if coupon >= 3:
                coupon -= 3
                BT(day+1, price, cantgo+1)
                coupon += 3
            else:
                BT(day+1, price+10000, cantgo+1)

N, M = map(int, input().split())
cant = list(map(int, input().split()))
cantbool = [0 for i in range(N+1)]
for i in cant:
    cantbool[i] = 1
coupon = 0
result = 10000*(N-M)
BT(0, 0, 1)
print(result)

# N, M = map(int, input().split())
# rawcant = list(map(int, input().split()))
# coupon = 0
# result = [0 for i in range(N+1)]
# cant = [0 for i in range(N+1)]
# for i in rawcant:
#     cant[i] = 1

# for i in range(1, N+1):
#     if i < 3:
#         if cant[i]:
#             result[i] = result[i-1]
#         else:
#             result[i] = result[i-1] + 10000
#     elif i < 5:
#         ifd, ifd3 = result[i-1] + 10000, result[i-3] + 25000
#         if cant[i]:
#             if min(result[i-1], ifd3) == result[i-1]:
#                 result[i] = result[i-1]
#             else:
#                 result[i] = ifd3
#                 coupon += 1
#         else:
#             if min(ifd, ifd3) == ifd:
#                 result[i] = ifd
#             else:
#                 result[i] = ifd3
#                 coupon += 1
#     else:
#         ifd, ifd3, ifd5 = result[i-1] + 10000, result[i-3] + 25000, result[i-5] + 37000
#         if cant[i]:
#             if min(result[i-1], ifd3, ifd5) == result[i-1]:
#                 result[i] = result[i-1]
#             elif min(result[i-1], ifd3, ifd5) == ifd3:
#                 result[i] = ifd3
#                 coupon += 1
#             else:
#                 result[i] = ifd5
#                 coupon += 2
#         else:
#             temp = coupon // 3
#             rest = cant[i+1:]
#             compare = len(rest)- sum(rest)
#             if temp > compare:
#                 result[i] = result[i-1]
#                 coupon -= 3
#             else:
#                 if min(ifd, ifd3, ifd5) == ifd:
#                     result[i] = ifd           
#                 elif min(ifd, ifd3, ifd5) == ifd3:
#                     result[i] = ifd3
#                     coupon += 1
#                 else:
#                     result[i] = ifd5
#                     coupon += 2

# print(result[-1])