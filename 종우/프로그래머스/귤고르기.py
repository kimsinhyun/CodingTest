# 0113_1
# https://school.programmers.co.kr/learn/courses/30/lessons/138476

# 내 풀이
from collections import Counter

def solution(k, tangerine):
    ctr = Counter(tangerine)
    ctrl = sorted([ctr[i] for i in ctr], reverse=True)
    sm = 0
    ct = 0
    for i in ctrl:
        sm += i
        ct += 1
        if sm >= k:
            return ct
    return 0