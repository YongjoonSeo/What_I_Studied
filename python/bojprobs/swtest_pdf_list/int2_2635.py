N = int(input())
a = int(2 * N / (1 + (5**.5)))
result = []
string = ''

for i in range(a-1, a+3):
    lst = [N, i]
    idx = 2
    while lst[idx-2] - lst[idx-1] >= 0:
        lst.append(lst[idx-2] - lst[idx-1])
        idx += 1
    result.append(lst)

for j in max(result, key=len):
    string += str(j) + ' '

print(len(max(result, key=len)))
print(string[:-1])