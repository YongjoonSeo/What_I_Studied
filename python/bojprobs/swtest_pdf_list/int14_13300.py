N, K = map(int, input().split())
g = []
b = []
for _ in range(N):
    temp = tuple(map(int, input().split()))
    if temp[0] == 0:
        g.append(temp)
    else:
        b.append(temp)

count = 0
for i in range(1,7):
    g_lst = []
    b_lst = []
    
    try:
        for j in g:
            if j[1] == i:
                g_lst.append(j)

        for k in b:
            if k[1] == i:
                b_lst.append(k)
            
        if len(g_lst) == 0:
            pass
        elif len(g_lst) % K:
            count += (len(g_lst) // K) + 1
        else:
            count += (len(g_lst) // K)

        if len(b_lst) == 0:
            pass
        elif len(b_lst) % K:
            count += (len(b_lst) // K) + 1
        else:
            count += (len(b_lst) // K)

    except:
        continue

print(count)

# 런타임 에러

N, K = map(int, input().split())
g = []
b = []
for _ in range(N):
    temp = tuple(map(int, input().split()))
    if temp[0] == 0:
        g.append(temp)
    else:
        b.append(temp)

count = 0
for i in range(1,7):
    g_lst = []
    b_lst = []
    

    for j in g:
        if j[1] == i:
            g_lst.append(j)

    for k in b:
        if k[1] == i:
            b_lst.append(k)
        
    if len(g_lst) == 0:
        pass
    elif len(g_lst) % K:
        count += (len(g_lst) // K) + 1
    else:
        count += (len(g_lst) // K)

    if len(b_lst) == 0:
        pass
    elif len(b_lst) % K:
        count += (len(b_lst) // K) + 1
    else:
        count += (len(b_lst) // K)


print(count)

# 인덱스 ㅡㅡ 어이가 없네 ㅡ.ㅡ