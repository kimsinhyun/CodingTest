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
        if t not in r:
            r[t] = 0
        r[t] += 1
    
    for t in topping:
        if t not in l:
            l[t] = 0
        r[t] -= 1
        # l[t] += 1
        if r[t] == 0:
            del l[t]
        if len(r[t]) == len(l[t]):
            answer +=1
        if len(r[t]) < len(l[t]):
            break
        

    return answer

# just using numbers to compare
def solution(topping):
    answer = 0
    l = {}
    r = {}
    
    for t in topping:
        if t not in r:
            r[t] = 0
        r[t] += 1
    
    for t in topping:
        if t not in l:
            l[t] = 0
        r[t] -= 1
        if r[t] == 0:
            del r[t]
        if len(r) == len(l):
            answer +=1
        if len(r) < len(l):
            break
        

    return answer