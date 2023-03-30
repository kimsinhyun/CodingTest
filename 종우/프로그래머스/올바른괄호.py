# 1006_3
# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

from collections import deque

def solution(s):
    stack = deque()
    for i in s:
        if i == "(":
            stack.appendleft(i)
        else:
            try:
                if not(stack.popleft() == "("):
                    stack.leftappend(i)
            except IndexError:
                return False
    if len(stack) == 0:
        return True
    return False