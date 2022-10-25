# 1005_3.py
# 괄호 회전하기
# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    nrot = len(s)
    for i in range(nrot):
        if iscor(s):
            answer += 1
        s = lrot(s)
    return answer

def lrot(s):
    return s[1:] + s[0]

def iscor(s):
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in s:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            if len(stack) < 1:
                return False
            pos = close_list.index(i)
            if open_list[pos] == stack[len(stack)-1]:
                stack.pop()
    if len(stack) == 0:
        return True
    return False
        
    