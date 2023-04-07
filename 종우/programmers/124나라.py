# 0407
# https://school.programmers.co.kr/learn/courses/30/lessons/12899#

# initial solve
def solution(n):
    answer = ''
    n -= 1
    dig = ['1', '2', '4']
    
    if n < 3:
        return dig[n]
    
    while n >= 3:
        last = n%3
        answer = dig[last] + answer
        n = n//3
        n -=1
    
    return answer

