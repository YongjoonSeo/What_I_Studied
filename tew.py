def move(arr, n):
    for rep in range(n):
        last = arr[-1]
        for i in range(-1, -len(arr), -1):
            arr[i] = arr[i-1]
        arr[0] = last
        print(arr)

line = list(map(int, input().split()))
n = line[0]
arr = line[1:]

move(arr, n)
# print(arr)