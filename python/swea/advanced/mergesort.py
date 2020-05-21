def mergesort(arr):
    if len(arr) == 1: return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
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


a = [69, 10, 30, 2, 16, 8, 7, 31, 22]
b = mergesort(a)
print(b)