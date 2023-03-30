# 0105_2
# https://school.programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    if s<n: return [-1]
    mid = s//n
    res = s%n
    answer.extend([mid]*(n-res))
    answer.extend([mid+1]*res)
    return answer