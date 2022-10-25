# 1012_1
# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = []
    
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    if len(stack) == 0:
        return 1
    else:
        return 0