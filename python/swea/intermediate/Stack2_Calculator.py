# 중위표기식 -> 후위표기식
def ISP(char): # in-stack priority
    lst = ['(', '+-', '*/', 'blank']
    for i in lst:
        if char in i:
            return lst.index(i)

def ICP(char): # in-coming priority
    lst = ['blank', '+-', '*/', '(']
    for i in lst:
        if char in i:
            return lst.index(i)

def Postfix(expression):
    operands = '0123456789'
    result = ''
    stack = []

    for i in expression:
        if i in operands: # 피연산자
            result += i
        else:             # 연산자와 괄호
            if i == ')':    # 연산자와 괄호 중 ')'
                if not stack:
                    return 'Error'
                else:
                    top = stack.pop()
                    while top != '(':
                        result += top
                        if stack: top = stack.pop()
                        if top != '(' and not stack:
                            return 'Error'
            else:           # 연산자와 괄호 중 ')'을 제외한 것들
                if not stack:
                    stack.append(i)
                elif ISP(stack[-1]) <= ICP(i):
                    if ISP(stack[-1]) == ICP(i):
                        result += stack.pop()
                    stack.append(i)
                else:
                    result += i

    if stack: return 'Error'
    return result

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b: return a // b

def Cal_Postfix(expression):
    stack = []
    operands = '0123456789'

    if expression == 'Error': return '잘못된 입력입니다.'
    else:
        for i in expression:
            if i in operands:
                stack.append(int(i))
            else:
                right = stack.pop()
                left = stack.pop()
                temp = 0
                if i == '+': temp = add(left, right)
                elif i == '-': temp = subtract(left, right)
                elif i == '*': temp = multiply(left, right)
                else: temp = divide(left, right)
                stack.append(temp)
        return stack.pop()

expression = '(6+5*(2-8)/2)'
expression2 = '(6+5*(2-8))/2)'
expression3 = ')(6+5*(2-8)/2)'
expression4 = '((6+5*(2-8)/2)'

print(Postfix(expression))
print(Postfix(expression2))
print(Postfix(expression3))
print(Postfix(expression4))
print()
print(Cal_Postfix(Postfix(expression)))
print(Cal_Postfix(Postfix(expression2)))