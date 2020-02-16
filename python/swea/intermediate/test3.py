a = [[1,2,3], [4,5,6], [7,8,9]]
b = [[i for i in list(zip(*a))[j]] for j in range(3)]

for _ in range(3):
    print(a[_])

for _ in range(3):
    print(b[_])