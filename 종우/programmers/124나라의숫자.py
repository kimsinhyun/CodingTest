# 0427
# https://school.programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ''
    ternary = ['1', '2', '4']
    
    while n != 0:
        mod = n%3
        answer = ternary[mod-1] + answer
        n = (n-1)//3            
    
    return answer