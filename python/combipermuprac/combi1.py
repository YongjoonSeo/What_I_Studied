def Combination(arr, start, r):
    for i in range(start, len(arr)-r+1):
        if r - 1 == 0:
            yield [arr[i]]
        else:
            for j in Combination(arr, i+1, r-1):
                yield [arr[i]] + j

a = [1,2,3,4,5]

for i in Combination(a, 0, 3):
    print(i)