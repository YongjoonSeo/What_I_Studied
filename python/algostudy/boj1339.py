# N개 단어로 이루어져있음, 대문자로 이루어져있다
# 각 알파벳 숫자를 0~9 숫자중 하나로 바꿔서 N개의 수를 합한다.
# 출력: 단어 합의 최댓값

# 1. 모두 입력 받고 가장 길이가 긴 알파벳의 첫 글자가 가장 큰 수여야 한다.
# -> 길이 차이 날 때는 가장 먼저있는 알파벳이 가장 큰 수가 되면 된다.
# 2. 자릿수가 같을 때

N = int(input())
lst = []
maxl = 0
for n in range(N):
    temp = input()
    lst.append(temp)
    maxl = max(len(temp), maxl)
lst.sort(key=lambda x: len(x), reverse=True)

order = dict()
mul = 10 ** (maxl-1)
for i in range(-maxl,0):
    for char in lst:
        try:
            if order.get(char[i]):
                order[char[i]] += 1 * mul
            else:
                order[char[i]] = 1 * mul
        except:
            pass
    else:
        mul //= 10

orderlist = list(order.items())
orderlist.sort(key=lambda x: x[1], reverse=True)
resultdict = dict()
idx = 9
for letter, val in orderlist:
    resultdict[letter] = idx
    idx -= 1

result = 0
for word in lst:
    temp = 0
    for letter in word:
        temp *= 10
        temp += resultdict.get(letter)
    result += temp

print(result)



# print(maxl)
# print(lst)
# print(order)