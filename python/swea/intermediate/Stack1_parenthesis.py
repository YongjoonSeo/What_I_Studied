def BracketCheck(string):
    charlst = [0] * 128
    charlst[ord(')')] = '('
    charlst[ord('}')] = '{'
    charlst[ord(']')] = '['
    stack = []

    for char in string:
        if char == '(' or char == '{' or char =='[':
            stack.append(char) # 2-1
        elif char == ')' or char == '}' or char == ']': # 2-2
            if len(stack) == 0: return False # 2-2-1
            check = stack.pop()
            if check != charlst[ord(char)]: return False # 2-2-2
    
    if len(stack) > 0: return False # 2-2-3
    return True


print(BracketCheck("print('{} {}'.format(1, 2))"))
print(BracketCheck("N, M = map(int, input().split())"))
print(BracketCheck("print('#{} {}'.format(tc, find())"))

