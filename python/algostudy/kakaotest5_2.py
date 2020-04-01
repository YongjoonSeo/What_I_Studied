def solution(stones, k):
    answer = 0
    maxval = -1
    isTrue = False
    while True:
        answer += 1
        zeros = []
        minval = 200000001
        for i in stones:
            if i > 0 and minval > i:
                minval = i
        for i in range(len(stones)):
            if stones[i]:
                stones[i] -= minval
                if not stones[i]: zeros.append(i)
            else:
                zeros.append(i)
        print(stones)
        print(zeros)
        cnt = 1
        for i in range(1, len(zeros)):
            if zeros[i] == zeros[i-1] + 1:
                cnt += 1
                if cnt >= k:
                    print(cnt)
                    isTrue = True
                    break
            else:
                maxval = max(cnt, maxval)
                cnt = 1
        print(maxval)
        if isTrue or maxval >= k: break
        
                
    return answer

stone =	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stone, k))