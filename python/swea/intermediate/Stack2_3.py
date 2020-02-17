def Win(num1, card1, num2, card2):
    if card1 == card2:
        if num1 < num2: return num1
        else: return num2
    elif (card1 == 1 and card2 == 2) or (card1 == 2 and card2 == 3) or (card1 == 3 and card2 == 1):
        return num2
    else:
        return num1

def Game(start, end):
    if start >= end: return
    mid = (start + end) // 2
    
    if end - start == 1:
        return Win(start, cards[start], end, cards[end])
    if end - start == 2:
        temp = Game(start, mid)
        return Win(temp, cards[temp], end, cards[end])
    
    result1 = Game(start, mid)
    result2 = Game(mid+1, end)
    return Win(result1, cards[result1], result2, cards[result2])

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))
    result = Game(0, len(cards)-1)
    print('#{0} {1}'.format(t, result+1))