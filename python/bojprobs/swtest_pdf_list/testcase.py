# f = open('./test.txt', 'w')

def Nums(num, depth, leng):
    global h
    if depth == 0: return
    for i in range(leng):
        h.append(Nums(i, depth-1, leng))
    


l = list(range(6))
h = []
Nums(3, 3, 3)
print(h)
print(len(h))


# for i in range(6):
#     data = f'{l[i]} {h[i]}\n'
#     f.write(data)
# f.close()