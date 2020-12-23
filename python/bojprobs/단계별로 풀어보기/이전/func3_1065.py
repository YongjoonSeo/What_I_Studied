def is_han(num):
    if num < 100:
        return True
    else:
        rawlist = [int(i) for i in str(num)]
        templist = [rawlist[j]-rawlist[j-1] for j in range(1, len(rawlist))]
        index = 1
        while index < len(templist):
            if templist[index] != templist[index - 1]:
                return False
            index += 1
        return True

N = int(input())
idx = 1
num = 0
while idx <= N:
    if is_han(idx) == True:
        num += 1
    idx += 1
print(num)
