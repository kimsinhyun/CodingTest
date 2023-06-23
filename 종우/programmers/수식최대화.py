# 연산자 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/67257

from collections import deque

from collections import deque

def solution(expression):
    
    answer = 0
    
    operands = []
    operators = []
    
    def calc(prio):
        operandsQ = deque(operands)
        operatorsQ = deque(operators)
        final = 0
        
        for p in prio:
            tmpOperands = deque()
            tmpOperators = deque()
            if p == "*":
                for o in operatorsQ:
                    if o == "*":
                        o1 = operandsQ.popleft()
                        o2 = operandsQ.popleft()
                        operandsQ.appendleft(o1*o2)
                    else:
                        tmpOperands.append(operandsQ.popleft())
                        tmpOperators.append(o)
                tmpOperands.append(operandsQ.popleft())
                operandsQ = tmpOperands
                operatorsQ = tmpOperators
            elif p == "+":
                for o in operatorsQ:
                    if o == "+":
                        o1 = operandsQ.popleft()
                        o2 = operandsQ.popleft()
                        operandsQ.appendleft(o1+o2)
                    else:
                        tmpOperands.append(operandsQ.popleft())
                        tmpOperators.append(o)
                tmpOperands.append(operandsQ.popleft())
                operandsQ = tmpOperands
                operatorsQ = tmpOperators
            elif p == "-":
                for o in operatorsQ:
                    if o == "-":
                        o1 = operandsQ.popleft()
                        o2 = operandsQ.popleft()
                        operandsQ.appendleft(o1-o2)
                    else:
                        tmpOperands.append(operandsQ.popleft())
                        tmpOperators.append(o)
                tmpOperands.append(operandsQ.popleft())
                operandsQ = tmpOperands
                operatorsQ = tmpOperators
        return operandsQ.popleft()
    
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
        res = abs(calc(prio))
        if res > answer:
            answer = res
        
    print(answer)
    return answer