def oper(num1, num2, idx):
    if idx == 0:
        return num1 + num2
    elif idx == 1:
        return num1 - num2
    elif idx == 2:
        return num1 * num2
    else:
        if num1 < 0 and num2 > 0:
            return - (abs(num1) // num2)
        elif num1 > 0 and num2 < 0:
            return - (num1 // abs(num2))
        else:
            return num1 // num2

def minimaxi(total, start):
    global minval, maxval
    if start == len(lst):
        if total < minval:
            minval = total
        if total > maxval:
            maxval = total
        return
    for i in range(4):
        if not operators[i]:
            continue
        if i == 3 and lst[start] == 0:
            return
        temp = oper(total, lst[start], i)
        operators[i] -= 1
        minimaxi(temp, start + 1)
        operators[i] += 1

N = int(input())
lst = list(map(int, input().split()))
operators = list(map(int, input().split()))
minval = 1000000001
maxval = -1000000001

minimaxi(lst[0], 1)
print(maxval)
print(minval)