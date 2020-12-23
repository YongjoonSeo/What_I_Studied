def wholesum(lst):
    sum = 0 
    for i in lst:
        sum += i
    return sum

a = [1, 2, 42, 1, 25, 7]
print(wholesum(a))