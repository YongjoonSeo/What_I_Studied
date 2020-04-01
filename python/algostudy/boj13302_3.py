N, M = map(int, input().split())
maxcoupon = (N//5)*2 + (N%5)//3 + 1
cases = [[1000000 for i in range(maxcoupon)] for j in range(N+1)]
cases[0][0] = 0
days = [1 for i in range(N+1)]
if M > 0:
    for i in list(map(int, input().split())):
        days[i] = 0

for i in range(1, N+1):
    for j in range(maxcoupon):
        if cases[i-1][j] < 1000000:
            if days[i]:
                if j >= 3:
                    cases[i][j-3] = min(cases[i][j-3], cases[i-1][j])
                else:
                    cases[i][j] = min(cases[i-1][j]+10000, cases[i][j])
            else:
                cases[i][j] = min(cases[i-1][j], cases[i][j])
            
            if i >= 3:
                if cases[i-3][j] < 1000000:
                    cases[i][j+1] = min(cases[i-3][j]+25000, cases[i][j+1])
            
            if i >= 5:
                if cases[i-5][j] < 1000000:
                    cases[i][j+2] = min(cases[i-5][j]+37000, cases[i][j+2])

print(min(cases[-1]))



