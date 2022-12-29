# 1229_2
# https://school.programmers.co.kr/learn/courses/30/lessons/42747#

def solution(citations):
    npaper = len(citations)
    citations.sort()
    for i, cit in enumerate(citations):
        if cit >= (npaper-i):
            return npaper-i
    return 0