# 0406
# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    answer = 0
    dp1 = [0]*len(money)
    dp2 = [0]*len(money)
    
    dp1[0] = money[0]
    
    for i in range(1, len(money)-1):
        dp1[i] = max(dp1[i-1], dp1[i-2]+money[i])
        
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2]+money[i])
    
    answer = max(dp1[-2], dp2[-1])
    return answer