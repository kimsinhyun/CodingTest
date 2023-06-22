# 연산자 계산
from itertools import permutations

def solution(expression):
    
    answer = 0
    
    operands = []
    operators = []
    
    def calc(prio):
        tmp_operands = [:]
        tmp_operators = [:]
        final = 0
        
        
        
        for p in prio:
            if p == "*":
                for tmp_operators:
                    
                
    
    tmp = ""
    for e in expression:
        if e == "*":
            operators.append("*")
            operands.append(int(tmp))
            tmp = ""
        elif e == "+":
            operators.append("+")
            operands.append(int(tmp))
            tmp = ""
        elif e == "-":
            operators.append("-")
            operands.append(int(tmp))
            tmp = ""
        else:
            tmp += e
    operands.append(int(tmp))
    
    answer = 0
    priority = [('*', '+', '-'), ('*', '-', '+'), ('+', '*', '-'), ('+', '-', '*'), ('-', '*', '+'), ('-', '+', '*')]
    
    for prio in priority:
        calc(prio)
    
    return answer