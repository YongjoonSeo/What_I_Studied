def Permutation(arr, start, r):
    for i in range(start, len(arr)):
        arr[start], arr[i] = arr[i], arr[start]
        if r - 1 == 0:
            yield [arr[start]]
        else:
            for j in Permutation(arr, start+1, r-1):
                yield [arr[start]] + j
        arr[start], arr[i] = arr[i], arr[start]
        




a = [1,2,3,4,5]
cnt = 0
for i in Permutation(a, 0, 3):
    cnt+=1
    print(i, end=' ')
print()
print(cnt)