def MergeSort(lst):
    half = len(lst) // 2
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        return lst
    else:
        resultlst = []
        lst1 = MergeSort(lst[:half])
        lst2 = MergeSort(lst[half:])
        i, j = -len(lst1), -len(lst2)
        while i < 0 or j < 0:
            if i == 0:
                resultlst.append(lst2[j])
                j += 1
            elif j == 0:
                resultlst.append(lst1[i])
                i += 1
            else:
                if lst1[i] < lst2[j]:
                    resultlst.append(lst1[i])
                    i += 1
                else:
                    resultlst.append(lst2[j])
                    j += 1
        return resultlst

lst = [69, 10, 30, 2, 16, 8, 31, 22]
print(MergeSort(lst))