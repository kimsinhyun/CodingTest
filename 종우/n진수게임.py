# 0126_1
# https://school.programmers.co.kr/learn/courses/30/lessons/17687

def solution(n, t, m, p):
    answer = ''
    nums = '0123456789ABCDEF'
    
    until = t*m
    
    counting = '0'
    i=1
    while len(counting) < until:
        to = i
        converted = ''
        while to > 0:
            converted = nums[to%n] + converted
            to = to//n
        counting = counting + converted
        i += 1
    counting = counting[:until]
    
    for j in range(0, len(counting)):
        if j%m == p-1:
            answer+=counting[j]
    
    return answer