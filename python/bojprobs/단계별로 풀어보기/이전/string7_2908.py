# rawA, rawB = input().split()
# A = list(rawA)
# B = list(rawB)
# A.reverse()
# B.reverse()
# A = int(''.join(A))
# B = int(''.join(B))
# if A >= B:
#     print(A)
# else:
#     print(B)

lst = list(input().split())
for i in range(len(lst)):
    lst[i] = list(lst[i])
    lst[i].reverse()
    lst[i] = int(''.join(lst[i]))
    
if lst[0] >= lst[1]:
    print(lst[0])
else:
    print(lst[1])