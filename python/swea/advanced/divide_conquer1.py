def mergesort(arr):
    global cnt
    if len(arr) == 1: return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    if left[-1] > right[-1]: cnt += 1
    result = []
    i = j = 0
    while not (i == len(left) and j == len(right)):
        if i == len(left):
            result.append(right[j])
            j += 1
        elif j == len(right):
            result.append(left[i])
            i += 1
        elif left[i] >= right[j]:
            result.append(right[j])
            j += 1
        else:
            result.append(left[i])
            i += 1
    return result

T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0

    print('#{0} {1} {2}'.format(t, mergesort(lst)[N//2], cnt))