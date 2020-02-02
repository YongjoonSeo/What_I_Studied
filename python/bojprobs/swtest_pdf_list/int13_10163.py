# def diff(lst, n, i):
#     if n == -1:
#         return lst[-1]
#     if len(lst[n]) == 0:
#         return set()
#     if i % 2: 
#         return lst[n] - diff(lst, n+1, i+1)
#     return diff(lst, n+1, i+1) - lst(n)

# N = int(input())
# whole = []
# for _ in range(N):
#     s, e, w, h = map(int, input().split())
#     temp = {(i, j) for i in range(s, s+w) for j in range(e, e+h)}
#     whole.append(temp)

# result = [diff(whole, i, 1) for i in range(-len(whole), 0)]
# for i in result:
#     if i == set():
#         print(0)
#     else:
#         print(len(i))


N = int(input())
save = set()
whole = []
for i in range(N):
    x, y, w, h = map(int, input().split())
    cp = {(i,j) for i in range(x, x+w) for j in range(y, y+h)}
    whole.append(cp)

result = []
for j in range(-1, -len(whole)-1, -1):
    if j == -1:
        result.append(len(whole[j]))
        save = whole[j]
    else:
        result.append(len(whole[j]-save))
        save = whole[j] | save - (whole[j] & save)

for k in range(len(result)):
    print(result[-k-1])