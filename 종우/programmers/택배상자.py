# 0504
# https://school.programmers.co.kr/learn/courses/30/lessons/131704

from collections import deque

def solution(order):
    answer = 0
    n = len(order)
    q = deque()
    cnt = 0
    for i in range(1, n+1):
        if i != order[cnt]:
            q.append(i)
        else:
            answer += 1
            cnt += 1
        while q:
            if q[-1] == order[cnt]:
                answer += 1
                cnt += 1
                q.pop()
            else:
                break
    
    return answer