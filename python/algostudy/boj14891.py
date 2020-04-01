def rotate(arr, num):
    if num == 1: arr.insert(0, arr.pop())
    elif num == -1: arr.append(arr.pop(0))

def check():
    checklist = []
    for i in range(1, 4):
        if magnets[i][2] != magnets[i+1][6]:
            checklist.append((i,i+1))
            checklist.append((i+1,i))
    return checklist

magnets = [0] + [list(map(int, input())) for i in range(4)]
rotates = [0 for i in range(5)]
K = int(input())
for _ in range(K):
    magnet, turn = map(int, input().split())
    s1 = s2 = magnet
    i = magnet + 1
    j = magnet - 1
    checklist = check()
    rotate(magnets[magnet], turn)
    rotates[magnet] = turn
    while i <= 4:
        if rotates[s1] and (s1, i) in checklist:
            rotate(magnets[i], rotates[s1]*(-1))
            rotates[i] = rotates[s1]*(-1)
            s1 = i
            i += 1
        else:
            break
    while j >= 1:
        if rotates[s2] and (s2, j) in checklist:
            rotate(magnets[j], rotates[s2]*(-1))
            rotates[j] = rotates[s2]*(-1)
            s2 = j
            j -= 1
        else:
            break    

result = 0
for i in range(1, 5):
    if magnets[i][0]: result += 2 ** (i-1)

print(result)



# for _ in range(len(magnets)):
#     print(magnets[_])