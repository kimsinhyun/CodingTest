# 0525
# https://school.programmers.co.kr/learn/courses/30/lessons/64062
# 다시풀기

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

# binary search solution
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

# max heap solution
import heapq
def solution(stones, k):
    answer = 200_000_000
    pq = []

    for i in range(k):
        heapq.heappush(pq, (-stones[i], i))
    
    for i in range(k, len(stones)):
        heapq.heappush(pq, (-stones[i], i))
        while(pq[0][1] < i-k+1):
            heapq.heappop(pq)
        answer = min(answer, -pq[0][0])
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))