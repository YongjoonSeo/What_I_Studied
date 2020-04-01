def Six(num):
    temp = num
    cnt = 0
    while temp // 10 or temp % 10:
        if temp % 10 == 6:
            cnt += 1
            if cnt == 3:
                break
        else:
            cnt = 0
        temp //= 10
    if cnt >= 3: return True
    return False        

N = int(input())
idx = 0
num = 666
while idx != N:
    idx += 1
    if idx == N:
        print(num)
        break
    else:
        num += 1
        while not Six(num):
            num += 1
