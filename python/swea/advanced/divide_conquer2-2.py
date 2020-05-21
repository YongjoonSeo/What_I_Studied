def partition(arr, s, e):
    pivot = arr[e]
    i = s - 1
    for j in range(s, e):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[e] = arr[e], arr[i+1]
    return i+1

def quicksort(arr, s, e):
    pivot = partition(arr, s, e)
    if s < pivot-1:
        quicksort(arr, s, pivot-1)
    if e > pivot:
        quicksort(arr, pivot+1, e)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    quicksort(lst, 0, N-1)
    print('#{0} {1}'.format(t, lst[N//2]))