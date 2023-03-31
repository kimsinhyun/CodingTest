# 0113_2
# https://school.programmers.co.kr/learn/courses/30/lessons/12927#

import heapq

def solution(n, works):
    if n > sum(works): return 0
    
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)
    
    for i in range(n):
        m = heapq.heappop(works)
        m += 1
        heapq.heappush(works, m)
    
    fatigue = 0
    for i in list(works):
        fatigue += i**2
    
    return fatigue