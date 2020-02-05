chul = [[i for i in list(map(int, input().split()))] for j in range(5)]
ref = []
for _ in range(5):
    ref.extend(list(map(int, input().split())))

cnt = 0
for num in ref:
    dsum_lr = 0
    dsum_rl = 0

    for i in range(5):
        for j in range(5):
            if chul[i][j] == num:
                chul[i][j] = -1
            if i == j:
                dsum_lr += chul[i][j]
            if j == 5 - 1 - i:
                dsum_rl += chul[i][5 - 1 - i]
    
    for i in range(5):
        if sum(chul[i]) == -5:
            cnt += 1
    
    for i in range(5):
        if sum(list(zip(*chul))[i]) == -5:
            cnt += 1
    
    if dsum_rl == -5:
        cnt += 1
    if dsum_lr == -5:
        cnt += 1
    
    if cnt >= 3:
        print(ref.index(num) + 1)
        break
    
        






# print(ref)
# for _ in range(len(chul)):
#     print(chul[_])