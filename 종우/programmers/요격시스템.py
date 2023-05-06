# 0506
# https://school.programmers.co.kr/learn/courses/30/lessons/181188

def solution(targets):
    answer = 0
    targets.sort()
    
    lowestend = 0
    for target in targets:
        if target[0] >= lowestend:
            answer += 1
            lowestend = target[1]
        elif target[1] < lowestend:
            lowestend = target[1]
    
    
    return answer