# 0508
# https://school.programmers.co.kr/learn/courses/30/lessons/67258#

from collections import Counter

def solution(gems):
    cntl = Counter(gems)
    cntr = cntl.copy()
    ll = 0
    rl = len(gems)-1
    while cntl[gems[rl]] > 1:
        cntl[gems[rl]] -= 1
        rl -= 1
    while cntl[gems[ll]] > 1:
        cntl[gems[ll]] -= 1
        ll += 1
    
    
    lr = 0
    rr = len(gems)-1
    while cntr[gems[lr]] > 1:
        cntr[gems[lr]] -= 1
        lr += 1
    while cntr[gems[rr]] > 1:
        cntr[gems[rr]] -= 1
        rr -= 1
    
    if rl - ll <= rr - lr:
        return [ll+1, rl+1]
    return [lr+1, rr+1]


# two pointers that take into account all ranges
def solution(gems):
    answer = []
    
    counter = {}
    ranges = []
    
    start = 0
    end = 0
    
    for g in set(gems):
        counter[g] = 0
    
    while True:
        if end == len(gems):
            break
        counter[gems[end]] += 1
        if 0 not in counter.values():
            while True:
                counter[gems[start]] -= 1
                start += 1
                if counter[gems[start-1]] == 0:
                    ranges.append([start, end+1])
                    break
        end += 1
    
    answer = ranges[0]
    for r in ranges:
        if r[1] - r[0] < answer[1] - answer[0]:
            answer = r
    
    return answer