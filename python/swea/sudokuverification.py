def Sudoku():
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if k == j: pass
                else:
                    if field[i][k] == field[i][j]: return 0
                if k == i: pass
                else:
                    if field[k][j] == field[i][j]: return 0
            sy, sx = i//3*3, j//3*3
            for n in range(sy, sy+3):
                for m in range(sx, sx+3):
                    if n == i and m == j: pass
                    else: 
                        if field[n][m] == field[i][j]: return 0
    return 1

T = int(input())
for t in range(1, T+1):
    field = [list(map(int, input().split())) for j in range(9)]
    print('#{0} {1}'.format(t, Sudoku()))


    # for _ in range(len(field)):
    #     print(field[_])