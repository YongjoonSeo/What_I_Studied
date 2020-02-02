w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())
dx = dy = 1

for _ in range(t % (w*2)):
    x += dx
    if x == w:
        dx = -1
    elif x == 0:
        dx = 1
    
for _ in range(t % (h*2)):
    y += dy
    if y == h:
        dy = -1
    elif y == 0:
        dy = 1

print(x, y)