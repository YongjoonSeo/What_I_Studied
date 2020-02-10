# 보류

def KMP(string, target):
    backloc = [0] * len(target)
    backloc[0] = -1



string = 'abcdabcdabcdabcdabcdabcef'
target1 = 'abcdabcef' # 본문에 있는 문자열
target2 = 'abcdabcf' # 본문에 없는 문자열