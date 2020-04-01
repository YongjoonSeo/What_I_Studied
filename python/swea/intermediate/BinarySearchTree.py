def Searchidx(val):
    i = 1
    while i < len(lst):
        if lst[i] == val:
            return i
        elif lst[i] == None:
            return False, i
        elif lst[i] < val:
            i = i*2 + 1
        else:
            i = i*2
    else:
        return False

def Insertval(val):
    get = Searchidx(val)
    if type(get) == tuple:
        lst[get[1]] = val
# 확보된 리스트 공간 내에서만 삽입 연산이 가능하다.

lst = [None, 15, 9, 23, 3, 12, 17, 28, None, 8]

print(lst[1:])
print(Searchidx(8))
Insertval(1)
print(lst[1:])
