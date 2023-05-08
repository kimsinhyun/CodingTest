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
    