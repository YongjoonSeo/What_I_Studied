def permutations(resultset, start, r):
    if len(resultset) == r:
        yield resultset
    else:
        for move in range(start, len(arr)):
            arr[move], arr[start] = arr[start], arr[move]
            for result in permutations(resultset + [arr[start]], start+1, r):
                yield result
            arr[move], arr[start] = arr[start], arr[move]
# resultset의 원소의 개수가 r이 되는 순간 내부적으로 resultset을 전달해주고,
# 외부로는 result를 반환한다.

arr = [1,2,3,4,5]
r = 3
for perm in permutations([], 0, r):
    print(perm, end=' ')