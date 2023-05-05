# 0505
# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    answer = -2
    whole = queue1 + queue2
    goal = sum(whole)//2
    
    l = 0
    r = len(queue1)
    
    return answer