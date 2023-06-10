# 0610
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

# my solution
from collections import deque

def solution(p):
    answer = ''
    
    def makeProper(p):
        if not p:
            return p
        
        o, c = 0, 0
        u, v = '', ''
        for i, par in enumerate(p):
            if par == '(':
                o += 1
            else:
                c += 1
            if o == c:
                u = p[:i+1]
                v = p[i+1:]
                break
        if isProper(u):
            mp = makeProper(v)
            return u + mp
        else:
            tmp = "("
            tmp += makeProper(v)
            tmp += ")"
            fu = flip(u)`
            return tmp + fu
            
            
    def isProper(p):
        q = deque()
        
        for par in p:
            if par == "(":
                q.append(par)
            else:
                if len(q) == 0 or q.pop() != "(":
                    return False
        return True
    
    def flip(u):
        u = u[1:-1]
        tmp = ""
        for you in u:
            if you == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp
    
    answer = makeProper(p)
    
    return answer

