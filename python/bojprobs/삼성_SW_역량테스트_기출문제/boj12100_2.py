N = int(input())

field = [list(map(int, input().split())) for j in range(N)]

for _ in range(len(field)):
    print(field[_])