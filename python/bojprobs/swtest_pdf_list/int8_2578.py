# chul = [[i for i in list(map(int, input().split()))] for j in range(5)]
# ref = []
# for _ in range(5):
#     ref.extend(list(map(int, input().split())))

# cnt = 0
# for num in ref:
#     dsum_lr = 0
#     dsum_rl = 0

#     for i in range(5):
#         for j in range(5):
#             if chul[i][j] == num:
#                 chul[i][j] = -1
#             if i == j:
#                 dsum_lr += chul[i][j]
#             if j == 5 - 1 - i:
#                 dsum_rl += chul[i][5 - 1 - i]
    
#     for i in range(5):
#         if sum(chul[i]) == -5:
#             cnt += 1
    
#     for i in range(5):
#         if sum(list(zip(*chul))[i]) == -5:
#             cnt += 1
    
#     if dsum_rl == -5:
#         cnt += 1
#     if dsum_lr == -5:
#         cnt += 1
    
#     if cnt >= 3:
#         print(ref.index(num) + 1)
#         break


# # print(ref)
# # for _ in range(len(chul)):
# #     print(chul[_])

def Numcheck(doublst, k):
    for i in range(5):
        for j in range(5):
            if doublst[i][j] == k:
                doublst[i][j] = -1
                break

def Bingocheck(doublst):
    cnt = 0
    digsum1 = digsum2 = 0
    for i in range(5):
        h_sum = 0
        for j in range(5):
            if i == j: digsum1 += doublst[i][j]
            if i+j == 4: digsum2 += doublst[i][j]
            h_sum += doublst[i][j]
        if h_sum == -5:
            cnt += 1
    
    if digsum1 == -5: cnt += 1
    if digsum2 == -5: cnt += 1

    for i in range(5):
        v_sum = 0
        for j in range(5):
            v_sum += doublst[j][i]
        if v_sum == -5:
            cnt += 1
    
    if cnt >= 3:
        return True

field = [[i for i in list(map(int, input().split()))] for j in range(5)]
referee = []
for i in range(5):
    referee.extend(list(map(int, input().split())))

for res in range(25):
    Numcheck(field, referee[res])
    if Bingocheck(field):
        print(res+1)
        break





