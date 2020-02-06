def test(lst):
    tes = lst
    tes[0][0] = 23

def test2(lst):
    tes = lst[:]
    tes[0][0] = 24

def test3(lst):
    tes = lst.copy()
    tes[0][0] = 25

a = [[1,2], [2,3], [3,4]]
a2 = [[1,2], [2,3], [3,4]]
a3 = [[1,2], [2,3], [3,4]]

test(a)
test2(a2)
test3(a3)

print(a)
print(a2)
print(a3)

b = [[1,2], [3,4]]
c = b[:]
print(id(b))
print(id(c))
print(id(b[0]))
print(id(c[0]))