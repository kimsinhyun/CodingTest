# 0525
# https://school.programmers.co.kr/learn/courses/30/lessons/64062

# 효율성 x 
def solution(stones, k):
    answer = 0
    while check(stones, k):
        answer += 1
        subtract(stones)
    return answer

def subtract(stones):
    for i in range(len(stones)):
        stones[i] = stones[i]-1

def check(stones, k):
    skip = 0
    for s in stones:
        if s < 1:
            skip += 1
        else:
            skip = 0
        if skip == k:
            return False
    return True

# binary search

def solution(stones, k):
    l, r = 1, 200_000_000
    
    while l <= r:
        m = (r + l) // 2
        cnt = 0
        for i in range(len(stones)):
            if stones[i] - m <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= k:
                break
                
        if cnt >= k:
            r = m-1
        else:
            l = m+1
    return l
