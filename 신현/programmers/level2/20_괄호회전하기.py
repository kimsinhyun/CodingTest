def solution(s):
    from collections import deque
    s = deque(s)
    answer=0
    for i in range(len(s)):
        stack = deque([])
        for j in range(len(s)):
                if len(stack)>0:
                    if s[j] == "}" and stack[-1] == "{":
                        stack.pop()
                    elif s[j] == "]" and stack[-1] == "[":
                        stack.pop()
                    elif s[j] == ")"and stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(s[j])
                        
                else:
                    stack.append(s[j])
        if(len(stack) == 0):
            answer+=1
        s.rotate(-1)
    return answer