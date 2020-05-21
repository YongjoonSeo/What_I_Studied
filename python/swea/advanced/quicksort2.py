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


a = [69, 10, 30, 2, 16, 8, 7, 31, 22]
quicksort(a, 0, len(a)-1)
print(a)