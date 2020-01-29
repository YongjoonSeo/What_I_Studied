whole = set()
for _ in range(4):
    rec_inp = list(map(int, input().split()))
    y2 = rec_inp[-1]
    y1 = rec_inp[1]
    x1 = rec_inp[0]
    x2 = rec_inp[-2]
    rec = [(i, j) for i in range(x1, x2) for j in range(y1, y2)]
    whole.update(rec)

print(len(whole))