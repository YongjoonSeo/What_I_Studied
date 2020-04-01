import sys
sys.stdin = open('sample_input.txt','r')

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

def mini(total, start):
    global minval
    # if total > minval and not operators[1] and not operators[3]: return
    if start == len(lst):
        if total < minval:
            minval = total
        return
    for i in range(4):
        if not operators[i]:
            continue
        if i == 3 and lst[start] == 0:
            return
        temp = oper(total, lst[start], i)
        operators[i] -= 1
        mini(temp, start + 1)
        operators[i] += 1

def maxi(total, start):
    global maxval
    # if total < maxval and not operators[0] and not operators[2]: return
    if start == len(lst):
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
        maxi(temp, start + 1)
        operators[i] += 1

T = int(input())
for t in range(1, T+1):
    N = int(input())
    operators = list(map(int, input().split()))
    lst = list(map(int, input().split()))
    minval = 1000000001
    maxval = -1000000001

    mini(lst[0], 1)
    maxi(lst[0], 1)
    print('#{0} {1}'.format(t, maxval-minval))