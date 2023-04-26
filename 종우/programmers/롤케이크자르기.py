# 0426
# https://school.programmers.co.kr/learn/courses/30/lessons/132265

# 시간초과
def fair(l, r):
    lc = 0
    rc = 0
    for t in l:
        if l[t] > 0:
            lc +=1
        if r[t] > 0:
            rc +=1
    if lc == rc:
        return True
    return False

def solution(topping):
    answer = 0
    l = {}
    r = {}
    
    for t in topping:
        if t not in l:
            l[t] = 0
            r[t] = 0
        r[t] += 1
    
    for t in topping:
        l[t] += 1
        r[t] -= 1
        if fair(l, r):
            answer += 1
    
    return answer