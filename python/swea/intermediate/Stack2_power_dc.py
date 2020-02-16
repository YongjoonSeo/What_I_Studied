def Power(num, n):
    global cnt1
    cnt1 += 1
    if n == 0: return 1
    return num * Power(num, n-1)

def Power_DC(num, n):
    global cnt2
    cnt2 += 1
    if n // 2:
        prev = Power_DC(num, n//2)
        if n & 1: return prev * prev * num
        else: return prev * prev
    else:
        if n & 1: return num
        else: return 1

cnt1 = 0
print(Power(2, 3))
print(f'세는 횟수: {cnt1}')
cnt1 = 0
print(Power(2, 10))
print(f'세는 횟수: {cnt1}')

cnt2 = 0
print(Power_DC(2, 3))
print(f'세는 횟수: {cnt2}')

cnt2 = 0
print(Power_DC(2, 10))
print(f'세는 횟수: {cnt2}')