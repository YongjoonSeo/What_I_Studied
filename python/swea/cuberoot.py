# T = int(input())
# for t in range(1, T+1):
#     N = int(input())
#     for i in range(int(N**0.3), int(N**0.35+1)):
#         if i**3 == N:
#             print('#{0} {1}'.format(t, i))
#             break
#     else:
#         print('#{0} {1}'.format(t, -1))

T = int(input())
for t in range(1, T+1):
    N = int(input())
    i = round(N ** 0.333333333333333333333333333333)
    if i**3 == N:
        print('#{0} {1}'.format(t, i))
    else:
        print('#{0} {1}'.format(t, -1))