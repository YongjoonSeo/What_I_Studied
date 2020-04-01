def solution(stones, k):
    answer = 0
    while True:
        answer += 1
        cnt = 0
        maxval = -1
        if stones[0]: stones[0] -= 1
        else: cnt += 1
        for i in range(1, len(stones)):
            if stones[i]: stones[i] -= 1
            if stones[i] == 0:
                if stones[i-1] == 0: 
                    cnt += 1
                    if cnt >= k:
                        maxval = cnt
                        break
                else:
                    maxval = max(maxval, cnt)
                    cnt = 1
        if maxval >= k: break
                
    return answer

stone =	[1]
k = 1
print(solution(stone, k))