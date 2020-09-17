n = 4
whole = []
a = b = 0
dx = 0; dy = 1
for i in range(n):
    whole.append([0 for j in range(i+1)])
whole[a][b] = 1
for num in range(n * (n + 1) // 2):
    if a + dy >= n or whole[a + dy][b] != 0:
        dx = 1; dy = 0
    elif b + dx >= len(whole[a]) or b + dx <= 0 or whole[a][b + dx] != 0:
        dx = -1; dy = -1
    else:
        dy = 1; dx = 0
    print('a + dy', a + dy)
    print('b + dx', b + dx)
    whole[a + dy][b + dx] = num
    a += dy
    b += dx
        
for i in range(len(whole)):
    print(whole[i])