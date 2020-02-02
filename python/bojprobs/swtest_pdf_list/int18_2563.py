n = int(input())
whole = set()
for _ in range(n):
    x, y = map(int, input().split())
    temp = {(i, j) for i in range(y, y+10) for j in range(x, x+10)}
    whole |= temp

print(len(whole))