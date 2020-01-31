def swap(lst,n):
    temp = lst.copy()
    if n == 1:
        temp[0], temp[-1] = temp[-1], temp[0]
    elif n == 2:
        temp[5], temp[3], temp[0], temp[1] = temp[1], temp[5], temp[3], temp[0]
    elif n == 3:
        temp[5], temp[4], temp[0], temp[2] = temp[2], temp[5], temp[4], temp[0]
    elif n == 4:
        temp[5], temp[3], temp[0], temp[1] = temp[3], temp[0], temp[1], temp[5]
    elif n == 5:
        temp[5], temp[2], temp[0], temp[4] = temp[4], temp[5], temp[2], temp[0]
    else:
        pass
    return temp

# a = [1,2,3,4,5,6]
# for i in range(1,7):
#     temp = a.copy()
#     temp = swap(temp,i)
#     print(temp)

num = int(input())
first_dice = list(map(int, input().split()))
result = [max(swap(first_dice, 6)[1:5]), max(swap(first_dice, 1)[1:5]), max(swap(first_dice, 2)[1:5]), max(swap(first_dice, 3)[1:5]), max(swap(first_dice, 4)[1:5]), max(swap(first_dice, 5)[1:5])]
prev = [swap(first_dice, 6), swap(first_dice, 1), swap(first_dice, 2), swap(first_dice, 3), swap(first_dice, 4), swap(first_dice, 5)]
for _ in range(num-1): # 나머지 입력
    this = list(map(int, input().split()))
    for case in range(6): # 처음 주사위 케이스 6개
        thiscopy = this.copy()
        for j in range(1, len(thiscopy)+1):
            if prev[case][0] == thiscopy[j-1]:
                thiscopy = swap(thiscopy, j)
                break
        result[case] += max(thiscopy[1:5])
        prev[case] = thiscopy

print(max(result))

# # 풀이법이 틀렸나? -> 첫번째 주사위를 카운트하지 않았다.......

