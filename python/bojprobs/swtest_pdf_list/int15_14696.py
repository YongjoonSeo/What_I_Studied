def who_win(dic1, dic2):
    A = dic1
    B = dic2
    if A.get('4') == B.get('4'):
        if A.get('3') == B.get('3'):
            if A.get('2') == B.get('2'):
                if A.get('1') == B.get('1'):
                    return 'D'
                else:
                    return 'A' if A.get('1') > B.get('1') else 'B'
            else:
                return 'A' if A.get('2') > B.get('2') else 'B'
        else:
            return 'A' if A.get('3') > B.get('3') else 'B' 
    else:
        return 'A' if A.get('4') > B.get('4') else 'B'


N = int(input())
for _ in range(N):
    two = []
    for i in range(2):
        temp = list(input().split())
        dic = dict()
        num = temp[0]
        for j in temp[1:]:
            if j in dic:
                dic[j] += 1
            else:
                dic[j] = 1
        for k in '1234':
            if k not in dic:
                dic[k] = 0
        
        two.append(dic)

    print(who_win(two[0], two[1]))