T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    field = [[i for i in input()] for j in range(N)]
    field2 = list(zip(*field))

    for j in range(N):
        for i in range(N - M + 1):
            if field[j][i:i+M] == field[j][-(N-(i+M))-1:-(N-i)-1:-1]:
                result = field[j][i:i+M+1]
            elif field2[j][i:i+M] == field2[j][-(N-(i+M))-1:-(N-i)-1:-1]:
                result = field2[j][i:i+M+1]

    print('#{0} {1}'.format(t, ''.join(result)))

    # for _ in range(N):
    #     print(field[_])
    # for _ in range(N):
    #     print(field2[_])