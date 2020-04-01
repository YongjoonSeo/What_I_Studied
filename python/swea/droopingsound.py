T = int(input())
for t in range(1, T+1):
    text = [''] + list(input())
    H = int(input())
    addidx = list(map(int, input().split()))
    for idx in addidx:
        text[idx] += '-'

    print('#{0} {1}'.format(t,''.join(text)))