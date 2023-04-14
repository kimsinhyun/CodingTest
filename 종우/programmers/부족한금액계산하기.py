# 0414
# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    answer = -1
    cost = 0
    
    for i in range(1, count+1):
        cost += i * price
    
    if money > cost:
        return 0
    
    answer = cost - money
    return answer