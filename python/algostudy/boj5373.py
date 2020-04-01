def clockwise(arr):
    return [[arr[i][j] for i in range(-1, -4, -1)] for j in range(3)]

def counterclockwise(arr):
    return [[arr[i][j] for i in range(3)] for j in range(-1, -4, -1)]

def up(clock):
    global U, F, B, L, R
    tempF = F[0][:]
    if clock == '+':
        U = clockwise(U)
        F[0] = R[0][:]
        R[0] = B[2][::-1]
        B[2] = L[0][::-1]
        L[0] = tempF
    else:
        U = counterclockwise(U)
        F[0] = L[0][:]
        L[0] = B[2][::-1]
        B[2] = R[0][::-1]
        R[0] = tempF

def down(clock):
    global D, F, B, L, R
    tempF = F[2][:]
    if clock == '+':
        D = clockwise(D)
        F[2] = L[2][:]
        L[2] = B[0][::-1]
        B[0] = R[2][::-1]
        R[2] = tempF
    else:
        D = counterclockwise(D)
        F[2] = R[2][:]
        R[2] = B[0][::-1]
        B[0] = L[2][::-1]
        L[2] = tempF

def left(clock):
    global L, U, D, F, B
    tempU = [U[j][0] for j in range(3)]
    if clock == '+':
        L = clockwise(L)
        for i in range(3):
            U[i][0] = B[i][0]
            B[i][0] = D[i][0]
            D[i][0] = F[i][0]
            F[i][0] = tempU[i]
    else:
        L = counterclockwise(L)
        for i in range(3):
            U[i][0] = F[i][0]
            F[i][0] = D[i][0]
            D[i][0] = B[i][0]
            B[i][0] = tempU[i]

def right(clock):
    global R, U, D, F, B
    tempU = [U[j][2] for j in range(3)]
    if clock == '+':
        R = clockwise(R)
        for i in range(3):
            U[i][2] = F[i][2]
            F[i][2] = D[i][2]
            D[i][2] = B[i][2]
            B[i][2] = tempU[i]
    else:
        R = counterclockwise(R)
        for i in range(3):
            U[i][2] = B[i][2]
            B[i][2] = D[i][2]
            D[i][2] = F[i][2]
            F[i][2] = tempU[i]

def front(clock):
    global F, U, D, L, R
    tempU = U[2][:]
    if clock == '+':
        F = clockwise(F)
        U[2] = [L[i][2] for i in range(-1, -4, -1)]
        for i in range(3):
            L[i][2] = D[0][i]
        D[0] = [R[i][0] for i in range(-1, -4, -1)]
        for j in range(3):
            R[j][0] = tempU[j]
    else:
        F = counterclockwise(F)
        U[2] = [R[i][0] for i in range(3)]
        for i in range(3):
            R[i][0] = D[0][2-i]
        D[0] = [L[i][2] for i in range(3)]
        for j in range(3):
            L[j][2] = tempU[2-j]

def back(clock):
    global B, U, D, L, R
    tempU = U[0][:]
    if clock == '+':
        B = clockwise(B)
        U[0] = [R[i][2] for i in range(3)]
        for i in range(3):
            R[i][2] = D[2][2-i]
        D[2] = [L[i][0] for i in range(3)]
        for j in range(3):
            L[j][0] = tempU[2-j]
    else:
        B = counterclockwise(B)
        U[0] = [L[i][0] for i in range(-1, -4, -1)]
        for i in range(3):
            L[i][0] = D[2][i]
        D[2] = [R[i][2] for i in range(-1, -4, -1)]
        for j in range(3):
            R[j][2] = tempU[j]

def operation(face, direc):
    if face == 'U': up(direc)
    elif face == 'D': down(direc)
    elif face == 'F': front(direc)
    elif face == 'B': back(direc)
    elif face == 'L': left(direc)
    elif face == 'R': right(direc)

T = int(input())
for t in range(T):
    U = [['w' for i in range(3)] for j in range(3)]
    D = [['y' for i in range(3)] for j in range(3)]
    F = [['r' for i in range(3)] for j in range(3)]
    B = [['o' for i in range(3)] for j in range(3)]
    L = [['g' for i in range(3)] for j in range(3)]
    R = [['b' for i in range(3)] for j in range(3)]
    input()
    orders = list(input().split())
    for order in orders:
        operation(*order)

    for _ in range(3):
        print(''.join(U[_]))

    # for _ in range(3):
    #     print(''.join(D[_]))    
    # for _ in range(3):
    #     print(''.join(F[_]))
    # for _ in range(3):
    #     print(''.join(B[_]))
    # for _ in range(3):
    #     print(''.join(L[_]))
    # for _ in range(3):
    #     print(''.join(R[_]))
    # U = [[1,2,3], [4,5,6], [7,8,9]]
    # F = [[6,6,6], [7,7,7], [8,8,8]]
    # up('+')
    # for _ in range(3):
    #     print(U[_])
    # up('-')
    # for _ in range(3):
    #     print(U[_])
    # up('-')
    # for _ in range(3):
    #     print(U[_])
    # left('+')



# a = [[1,2,3], [4,5,6], [7,8,9]]
# b = clockwise(a)
# c = counterclockwise(a)

# for i in range(3):
#     print(b[i])
# for i in range(3):
#     print(c[i])

