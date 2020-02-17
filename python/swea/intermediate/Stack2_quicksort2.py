def Quick(lst, start, end):
    if start >= end: return
    pivot = start
    L = start + 1
    R = end

    while L < R:        
        while L <= R and lst[L] < lst[pivot]: L += 1
        while L <= R and lst[R] >= lst[pivot]: R -= 1
        if L < R:
            lst[L], lst[R] = lst[R], lst[L]
    
    if lst[R] <= lst[pivot]:
        lst[R], lst[pivot] = lst[pivot], lst[R]
        pivot = R

    Quick(lst, start, pivot - 1)
    Quick(lst, pivot + 1, end)

target = [3, 5, 8, 1, 2, 9, 4, 7, 6]
Quick(target, 0, len(target)-1)
print(target)