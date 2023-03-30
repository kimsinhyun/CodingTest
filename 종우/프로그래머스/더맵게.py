# 0116_1
# https://school.programmers.co.kr/learn/courses/30/lessons/42626

# 내 풀이

import heapq

def solution(scoville, K):
    mixes = 0
    heapq.heapify(scoville)
    
    while True:
        low = heapq.heappop(scoville)
        if low >= K:
            return mixes
        try:
            nlow = heapq.heappop(scoville)
        except IndexError:
            return -1
        mixed = low + (nlow*2)
        heapq.heappush(scoville, mixed)
        mixes += 1


# 다른 풀이
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer