# 비숍은 홀수 칸, 짝수 칸에만 서로 영향을 줄 수 있다. (사실 정확히 홀수 짝수칸은 아니긴 하다)
# -> 좌표를 따로 모아두고 해보자.
# 그 두 가지 경우를 각각 따지는 게 경우의 수를 훨씬 줄일 수 있다.
# 1. def route 좌표 input -> 필드 바꾸고 카운트 줄여가면서 yield 바꾸는 좌표
# 2. 백트래킹 -> 이때 홀수 짝수 나눌 수 있도록 하기
# -> 홀수 번째 칸 최대 개수 + 짝수 번째 칸 최대 개수
# 홀수 번째 칸 개수 == N // 2 (짝수) N//2+1 (홀수)
# 짝수 번째 칸 개수 == N // 2

def route(y, x):
    global N
    m = n = a = b = 1
    while y+m < N and x+m < N:
        yield (y+m, x+m)
        m += 1
    while y-n >= 0 and x-n >= 0:
        yield (y-n, x-n)
        n += 1
    while y+a < N and x-a >= 0:
        yield (y+a, x-a)
        a += 1
    while y-b >= 0 and x+b < N:
        yield (y-b, x+b)
        b += 1

def BT(inpset, bishop):
    global tempresult
    if len(inpset) == 0:
        tempresult = max(tempresult, bishop)
    save = []
    for n, m in inpset:
        save.append((n,m))
        inpset.remove((n,m))
        for y, x in route(n, m):
            try:
                inpset.remove((y,x))
                save.append((y,x))
            except:
                pass
        BT(inpset, bishop+1)
        for i, j in save:
            inpset.add((i,j))

N = int(input())
field = [list(map(int, input().split())) for j in range(N)]
odd = set()
even = set()
idx = 1
for i in range(N):
    for j in range(N):
        if field[i][j]:
            if idx == 1: odd.add((i, j))
            else: even.add((i, j))
        idx *= (-1)

tempresult = -1
BT(odd, 0)
result = tempresult
tempresult = -1
BT(even, 0)
result += tempresult

print(result)
# for _ in range(len(field)):
#     print(field[_])