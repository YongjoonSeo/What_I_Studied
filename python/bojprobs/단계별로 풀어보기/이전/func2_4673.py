def d(n):
    result = n
    for i in str(n):
        result += int(i)
    return result

wholenum = set(i for i in range (1,10001))
inits = set()
index = 1
while index <= 10000:
    temp = d(index)
    while temp <= 10000:
        inits.add(temp)
        temp = d(temp)
    index += 1

result = sorted(list(wholenum - inits))
for j in result:
    print(j)