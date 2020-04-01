def combinations(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nextelement in combinations(arr[i+1:], r-1):
                yield [arr[i]] + nextelement

def combinations_with_replacements(arr, r):
    for i in range(len(arr)):
        if r == 1:
            yield [arr[i]]
        else:
            for nextelement in combinations_with_replacements(arr[i:], r-1):
                yield [arr[i]] + nextelement

cnt = 0
for i in combinations([1,2,3,4,5], 3):
    cnt += 1
    print(i, end=' ')
print()
print(cnt)

print()
cnt = 0
for j in combinations_with_replacements([1,2,3,4,5], 3):
    cnt += 1
    print(j, end=' ')
print()
print(cnt)

