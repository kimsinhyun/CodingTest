def make_result(p, expression):
    from collections import deque
    arr = deque()
    num = ""
    for k in expression:
        if k.isdigit():
            num+=k
        else:
            arr.append(num)
            num = ""
            arr.append(k)
    arr.append(num)
    for op in p:
        stack = []
        while len(arr) != 0:
            temp = arr.popleft()
            if temp == op:
                result = str(eval(stack.pop() + op + arr.popleft()))
                stack.append(result)
            else:
                stack.append(temp)
        arr = deque(stack)
    return int(arr.pop())
    
def solution(expression):
    from itertools import permutations
    answer = 0
    ops = ["+","-","*"]
    for p in list(permutations(ops, 3)):
        answer = max(answer, abs(make_result(p,expression)))
    return answer
