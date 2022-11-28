# 1128_1
# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    sol = 0
    around = a
    bround = b
    
    #1,2->1 | 3,4->2 | 5,6->3
    while around != bround:
        if around % 2 == 0:
            around = around/2
        else:
            around = (around+1)/2
            
        if bround % 2 == 0:
            bround = bround/2
        else:
            bround= (bround+1)/2
        sol+=1
    return sol

    return answer