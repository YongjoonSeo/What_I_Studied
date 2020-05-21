# 위에서부터 배치하면?
# 한번 지나간 가스관쪽은 다시 못 지나간다.
# 가능한 맨 위의 파이프라인을 Sm이라고 하자
# 만약 최대 개수의 파이프라인 해 집합 A가 있으면 거기서 가장 위의 파이프라인은 Am
# Sm == Am이면 최대 개수에 포함
# Sm != Am이면 Sm과 Am을 바꾸어도 A의 나머지 집합에는 영향을 주지 않는다
# Sm을 배치하면 Sm은 가장 위의 파이프라인이라고 했으므로
# 남은 집합들 중에 최대 개수의 파이프라인을 찾아야 한다.
# -> 그리디 접근 가능: 가장 위에서부터 파이프라인을 설치하며 센다.
# 길 하나하나 찾는 건 백트래킹으로 하자. (루트가 없더라도 그 전에 밑으로 가서 출발하는 식으로는 가능하다.
# 하나 찾으면 모두 리턴.
# <<<< 근데 백트래킹하기엔 너무 시간이 오래 걸리는 것 같다. (x가 많은 경우)

def BT(y, x):
    global C, cnt, isfound
    if x == C:
        cnt += 1
        isfound = True
        return
    dy = [-1, 0, 1]

    for i in range(3):
        ny = y + dy[i]
        if 0 <= ny < R and field[ny][x] == '.':
            temp.append((ny, x))
            BT(ny, x+1)
            if isfound: return
            temp.pop()


R, C = map(int, input().split())
field = [list(input()) for j in range(R)]
dy = [-1, 0, 1]
cnt = 0

for i in range(R):
    temp = []
    isfound = False
    BT(i, 1)
    for y, x in temp:
        field[y][x] = 'x'

print(cnt)

# for _ in range(len(field)):
#     print(field[_])