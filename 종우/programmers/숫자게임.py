# 0422
# https://school.programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    # win as many = win at lowest
    # count how many aren't above
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    stack = []
    for a in A:
        if a < B[0]:
            answer += 1
            B.pop(0)
        
    return answer