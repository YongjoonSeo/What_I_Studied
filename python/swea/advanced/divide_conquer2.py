def partition(arr, s, e):
    pivot = arr[s]
    i = s + 1
    j = e
    while i <= j:
        while i <= j and arr[i] <= pivot: i += 1
        while i <= j and arr[j] >= pivot: j -= 1
        if i < j: # i와 j가 교차하기 전에는 i는 pivot보다 큰 값, j는 pivot보다 작은 값을 가리키게 된다.
            arr[i], arr[j] = arr[j], arr[i]
        # i와 j가 교차하게 되면 그 지점을 중심으로 왼쪽은 pivot보다 작은 값, 오른쪽은 pivot보다 큰 값이 모인다.
    arr[s], arr[j] = arr[j], arr[s] # pivot을 그 경계에 집어넣는다.
    return j

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