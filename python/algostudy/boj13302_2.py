def BT(day, price, cantgo):
    global result, N, coupon, toggle, tempday, tempprice, tempcantgo
    if price > result: return
    if cantgo <= N and cantbool[cantgo]:
        BT(day+1, price, cantgo+1)
    if toggle:
        if toggle == 2:
            tempday, tempprice, tempcantgo = day, price, cantgo
            toggle = 1
        if day >= N: 
            result = min(result, price)
        return True
    if day >= N: 
        result = min(result, price)
        tempday = day
        return

    for i in range(3):
        if i == 0:
            coupon += 2
            TF = BT(day+5, price+37000, cantgo+5)
            coupon -= 2
        elif i == 1:
            coupon += 1
            TF = BT(day+3, price+25000, cantgo+3)
            coupon -= 1
        else:
            if coupon >= 3:
                coupon -= 3
                if coupon == 0: toggle = 2
                TF = BT(day+1, price, cantgo+1)
                coupon += 3
            else:
                TF = BT(day+1, price+10000, cantgo+1)
        if TF: return True

N, M = map(int, input().split())
cant = list(map(int, input().split()))
cantbool = [0 for i in range(N+1)]
for i in cant:
    cantbool[i] = 1
coupon = 0
toggle = tempday = tempprice = 0
tempcantgo = 1
result = 10000*(N-M)
while tempday+1 < N:
    BT(tempday, tempprice, tempcantgo)
    toggle = 0
print(result)